#!/usr/bin/env python3
"""Check visible carousel text; never rewrite or delete source content.

Input: {"pages": [{"page": 1, "text_nodes": [...]}]}.
Every draw call must export a text node (including table cells and footers).
Run before rendering and again on the renderer's actual emitted surface log.
This is a text-boundary check, not a visual or source-coverage validator.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

PUBLIC_ROLES = frozenset({
    "title", "subtitle", "section-title", "body", "source-quote",
    "table-header", "table-cell", "chart-label", "chart-value",
    "caption", "source-citation", "source-note", "method-note",
    "brand", "page-number",
})
PUBLIC_PROVENANCE = frozenset({"source", "approved-editorial", "citation", "brand"})
PATTERNS = (
    ("full-text-label", re.compile(r"풀\s*텍스트|\bfull[\s-]*text\b", re.I)),
    ("source-file-message", re.compile(r"(?:원문|전체\s*(?:텍스트|내용|본문)).{0,36}(?:파일|첨부).{0,24}(?:수록|포함|참조|확인|있|보관)", re.I)),
    ("production-file", re.compile(r"(?:text[-_ ]?manifest|page[-_ ]?map|asset[-_ ]?map|qa[-_ ]?report|asset[-_ ]?audit|visual[-_ ]?fallback[-_ ]?log|source\.txt|style\.json)", re.I)),
    ("production-status", re.compile(r"(?:원문\s*보존본|검수(?:용|본|\s*완료)|누락\s*0\s*(?:건|자)|렌더링\s*(?:완료|버전)|제작\s*메모)", re.I)),
    ("english-production-message", re.compile(r"(?:\bsource\s+file\s+included\b|\btext\s+preserved\b|\brendered\s+version\b)", re.I)),
)


def validate_surface(payload: Any) -> dict[str, Any]:
    """Return an audit report; a match is a review gate, never a deletion rule."""
    issues: list[dict[str, Any]] = []
    exceptions: list[dict[str, Any]] = []
    checked = 0
    if not isinstance(payload, dict) or not isinstance(payload.get("pages"), list) or not payload["pages"]:
        return {"status": "fail", "checked_text_nodes": 0, "issues": [{"code": "invalid-pages"}], "approved_exceptions": []}
    seen_pages: set[int] = set()
    seen_ids: set[str] = set()
    for page_index, page in enumerate(payload["pages"], 1):
        if not isinstance(page, dict):
            issues.append({"page_index": page_index, "code": "invalid-page"})
            continue
        number = page.get("page")
        if type(number) is not int or number < 1 or number in seen_pages:
            issues.append({"page_index": page_index, "code": "invalid-page-number"})
        else:
            seen_pages.add(number)
        nodes = page.get("text_nodes")
        if not isinstance(nodes, list) or not nodes:
            issues.append({"page": number, "code": "missing-surface-text"})
            continue
        for index, node in enumerate(nodes):
            location = {"page": number, "node_index": index}
            if not isinstance(node, dict):
                issues.append({**location, "code": "invalid-node"})
                continue
            node_id = node.get("id")
            if not isinstance(node_id, str) or not node_id.strip() or node_id in seen_ids:
                issues.append({**location, "code": "invalid-node-id"})
            else:
                seen_ids.add(node_id)
            if node.get("audience") != "public":
                issues.append({**location, "code": "non-public-node", "id": node_id})
            role = node.get("role")
            if role not in PUBLIC_ROLES:
                issues.append({**location, "code": "unapproved-role", "id": node_id})
            provenance = node.get("provenance")
            if provenance not in PUBLIC_PROVENANCE:
                issues.append({**location, "code": "unapproved-provenance", "id": node_id})
            text = node.get("text")
            if not isinstance(text, str) or not text.strip():
                issues.append({**location, "code": "invalid-text", "id": node_id})
                continue
            checked += 1
            compact = re.sub(r"\s+", " ", text)
            matches = [name for name, pattern in PATTERNS if pattern.search(compact)]
            if not matches:
                continue
            exception = node.get("public_exception")
            approved = (
                isinstance(exception, dict)
                and exception.get("approved") is True
                and isinstance(exception.get("reason"), str)
                and bool(exception["reason"].strip())
                and isinstance(exception.get("approval_ref"), str)
                and bool(exception["approval_ref"].strip())
                and node.get("audience") == "public"
                and role in {"body", "source-quote", "source-citation", "method-note"}
                and provenance in {"source", "approved-editorial", "citation"}
            )
            item = {**location, "id": node_id, "matches": matches, "text": text}
            if approved:
                exceptions.append({**item, "reason": exception["reason"], "approval_ref": exception["approval_ref"]})
            else:
                issues.append({**item, "code": "production-meta-or-review-needed"})
    return {
        "status": "pass" if not issues else "fail",
        "checked_text_nodes": checked,
        "issues": issues,
        "approved_exceptions": exceptions,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("surface", type=Path)
    parser.add_argument("--report", type=Path, help="Write an internal JSON audit; never embed it on slides.")
    args = parser.parse_args()
    try:
        report = validate_surface(json.loads(args.surface.read_text(encoding="utf-8")))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    result = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(result, encoding="utf-8")
    print(result, end="")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
