# IO MAGAZINE — Text-first Report Carousel

**ACTIVE / v3.3 / `report-carousel-v3.3-text-first-audience-clean`**

긴 원문을 빠짐없이 읽히게 조판하고 실제 사진을 보조로 배치하는 인스타그램 4:5 파일 렌더링 스킬입니다. 승인 기준은 `japan_marathon_fulltext_20_v2`의 텍스트 중심 제작 수준입니다.

## 이번 변경

수정 대상은 결과 안내문이 아니라 **슬라이드 안에 보이는 불필요한 제작 문구**입니다.

- 슬라이드: 독자용 제목·본문·표·캡션·필요한 출처만 노출.
- 제작 보고서와 전달 메시지: 원문 포함 여부, 파일 목록, QA 설명 허용.
- 내부 로그: 매니페스트, 오프셋, 폰트 측정, 자산 감사 보관.

`FULL TEXT`, `원문은 파일에 수록`, `검수본`, `manifest`, `QA report` 같은 제작 태그를 게시용 이미지에 붙이지 않습니다. 연구 방법·기간·표본 기준이나 필요한 사진 크레딧은 유지합니다.

## 기본 제작 규칙

- 요청 전체 장수를 PNG로 한 번에 파일 렌더링. 10장 생성 제한 적용 없음.
- 본문 26px/39px를 새 기본으로 사용하고 같은 역할의 규격은 전 장 고정.
- 본문과 원래 표를 먼저 확보. 그래프·사진으로 본문을 대체하지 않음.
- 사진은 관련성이 있는 실제 파일만, 전경 무크롭, 기본 1회 사용.
- 표 페이지에는 사진 없음.
- 이미지 조사 → 후보 선별 → 권리·해상도 확인 → 중복 검사 → 남은 공간 배정.
- 원문에 의심점이 있어도 무단 교정하지 않고 별도 검토 메모로 분리.

## 실행 문서

`SKILL.md`부터 읽습니다. 핵심 세부 문서는 아래와 같습니다.

- `references/audience-content-boundary.md`
- `references/copy-guard.md`
- `references/report-carousel-v3.md`
- `references/adaptive-density.md`
- `references/image-research-and-placement.md`
- `references/asset-intake-and-visual-fallback.md`
- `references/request-routing.md`
- `references/production-workflow.md`
- `references/qa-checklist.md`

## 게시 문구 검사

```bash
python scripts/lint_public_surface.py examples/report-carousel-v3.sample.json
python -m unittest discover -s tests -v
```

제작 시에는 실제 `render-surface.json`에 검사기를 실행합니다. 검사기는 문자를 삭제하지 않고 검토할 위치를 반환합니다. 픽셀 잘림·원문 완전성 검사는 별도로 수행해야 합니다. 저장소에 검사기를 추가한 것만으로 과거 PNG가 고쳐지는 것은 아닙니다.

## 산출물 분리

`01.png`부터 마지막 PNG, `preview.jpg/png`, 전체 ZIP을 전달합니다. 원문, 매니페스트, 자산 출처, 감사·검수 보고서는 `production/` 아래에 보관하며 그 파일 안내를 슬라이드에 넣지 않습니다.

## 호출 예시

> 스킬대로 20장 전체 렌더링해. 원문은 전부 사용하고, 사진은 보조로. 슬라이드에는 독자용 콘텐츠만 넣어.

이 저장소는 재사용 가능한 규칙 원본이며 새 채팅의 자동 실행을 보장하지 않습니다. 사용할 때 저장소의 최신 SKILL.md를 읽도록 합니다. v2~v3.2 예시는 과거 참고용입니다.
