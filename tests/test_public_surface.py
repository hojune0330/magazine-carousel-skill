import copy
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("guard", ROOT / "scripts/lint_public_surface.py")
GUARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARD)


def payload(text="일본의 선수층을 비교한다.", **overrides):
    node = {"id": "p1-body-1", "audience": "public", "role": "body", "provenance": "source", "text": text}
    node.update(overrides)
    return {"pages": [{"page": 1, "text_nodes": [node]}]}


class PublicSurfaceTests(unittest.TestCase):
    def test_public_body(self):
        self.assertEqual(GUARD.validate_surface(payload())["status"], "pass")

    def test_fulltext_label_is_blocked(self):
        self.assertEqual(GUARD.validate_surface(payload("FULL TEXT", role="brand", provenance="brand"))["status"], "fail")

    def test_korean_label_is_blocked(self):
        self.assertEqual(GUARD.validate_surface(payload("풀 텍스트"))["status"], "fail")

    def test_source_file_footer_is_blocked(self):
        self.assertEqual(GUARD.validate_surface(payload("원문은 별도 파일에 수록되어 있습니다.", role="caption"))["status"], "fail")

    def test_multiline_meta_is_blocked(self):
        self.assertEqual(GUARD.validate_surface(payload("전체 텍스트는\n첨부 파일에서\n확인하세요."))["status"], "fail")

    def test_methodology_is_allowed(self):
        self.assertEqual(GUARD.validate_surface(payload("원문 자료와 데이터 파일을 분석했다. 분석 기간: 2020~2025년.", role="method-note"))["status"], "pass")

    def test_research_report_sentence_is_allowed(self):
        self.assertEqual(GUARD.validate_surface(payload("본 보고서는 선수별 최고 기록을 분석한다."))["status"], "pass")

    def test_credit_and_source_allowed(self):
        self.assertEqual(GUARD.validate_surface(payload("사진: 촬영자 / CC BY 4.0. 출처: 공식 경기 결과.", role="source-citation", provenance="citation"))["status"], "pass")

    def test_private_layer_cannot_render(self):
        self.assertEqual(GUARD.validate_surface(payload("본문", audience="production"))["status"], "fail")

    def test_missing_audience_fails_closed(self):
        data = payload()
        del data["pages"][0]["text_nodes"][0]["audience"]
        self.assertEqual(GUARD.validate_surface(data)["status"], "fail")

    def test_renderer_generated_meta_blocked(self):
        self.assertEqual(GUARD.validate_surface(payload("문구", provenance="renderer-metadata"))["status"], "fail")

    def test_file_label_in_chart_is_blocked(self):
        self.assertEqual(GUARD.validate_surface(payload("QA_REPORT.md", role="chart-label"))["status"], "fail")

    def test_original_quote_can_be_reviewed(self):
        data = payload("논문 제목: Full text retrieval", role="source-citation", provenance="citation", public_exception={"approved": True, "reason": "인용 논문의 실제 제목", "approval_ref": "editor-review-001"})
        result = GUARD.validate_surface(data)
        self.assertEqual(result["status"], "pass")
        self.assertEqual(len(result["approved_exceptions"]), 1)

    def test_exception_without_reason_fails(self):
        data = payload("FULL TEXT", public_exception={"approved": True, "reason": "", "approval_ref": "request"})
        self.assertEqual(GUARD.validate_surface(data)["status"], "fail")

    def test_invalid_and_empty_input_fails(self):
        for data in (None, [], {}, {"pages": []}, {"pages": [{"page": 1}]}):
            self.assertEqual(GUARD.validate_surface(data)["status"], "fail")

    def test_duplicate_ids_fail(self):
        data = payload()
        data["pages"][0]["text_nodes"] *= 2
        self.assertEqual(GUARD.validate_surface(data)["status"], "fail")

    def test_source_never_mutated(self):
        data = payload("원문은 파일에 수록되어 있습니다.")
        before = copy.deepcopy(data)
        GUARD.validate_surface(data)
        self.assertEqual(data, before)


if __name__ == "__main__":
    unittest.main()
