---
name: io-magazine-report-carousel
description: Render Korean Instagram report carousels as complete text-first PNG file sets. Preserve the selected source in full when requested; photos, charts and diagrams supplement rather than replace text. Use the approved large-type layout, measure text before assigning image space, keep tables photo-free, and separate public slide content from production reports and internal logs. Never print FULL TEXT, source-file notices, QA or manifest status on audience-facing slides. Research and attribute real image assets, validate every visible text node, and deliver the requested page count in one rendering job.
version: 3.4
status: active
---

# IO MAGAZINE — Text-first Report Carousel v3.4

현재 활성 프로필: `report-carousel-v3.4-text-first-audience-clean`.

## 0. 이번 승인 기준

사용자가 승인한 `japan_marathon_fulltext_20_v2`의 텍스트 중심 제작 수준을 기준으로 한다. 본문을 요약해 그래프로 바꾸던 이전 축약본과 생성형 포스터는 기준이 아니다.

이번 변경의 대상은 **결과 안내문이 아니라 실제 게시용 슬라이드 안에 그려지는 문구**다. 위쪽의 `풀 텍스트 / FULL TEXT`, 아래쪽의 `원문은 파일에 수록되어 있습니다` 등 제작자가 추가한 메타 문구를 제거한다. 원문·검수·첨부파일 설명은 제작 보고서, 첨부 문서, 전달 메시지에 남겨도 된다.

## 1. 실행 방식

- `스킬대로`, `렌더링`, `파일로`, `20장 전체`, `원문 빠짐없이`, `앞 장에 이어서`는 전체 파일 렌더링 요청이다.
- Python/Pillow, HTML/CSS, SVG 등으로 요청한 장수를 하나의 프로젝트에서 제작한다. 생성 이미지 개수 제한을 파일 렌더링에 적용하지 않는다.
- 최종 레이아웃, 한국어 본문, 표, 그래프 레이블, 페이지 번호는 생성형 이미지에 맡기지 않는다.
- 사용자가 이미지 생성 기능을 금지하면 별도 보조 생성 에셋도 사용하지 않는다. 코드로 그리는 표·그래프와 생성형 AI 이미지는 다른 종류다.
- 이번 스킬 업데이트만으로 과거 PNG가 수정되었다고 말하지 않는다. 실제 재렌더링이 필요하다.

## 2. 우선순위와 절대 규칙

1. 선택된 원문의 모든 내용과 순서를 보존한다. 요약본·예전 매니페스트로 슬쩍 교체하지 않는다.
2. 잘림·겹침·가림 없이 읽히게 한다.
3. 같은 역할의 글자는 전 장에서 폰트·크기·굵기·행간을 고정한다.
4. 사진·새 그래프·새 도식은 **보조**다. 원문의 문장이나 원래 표를 대체할 수 없다.
5. 텍스트를 먼저 실측한다. 남은 공간에 관련 이미지를 배치하며, 공간이 없으면 이미지를 뺀다.
6. 전경 사진은 원본 비율을 유지하고 크롭하지 않는다. 텍스트 패널로 얼굴·동작을 가리는 것도 실패다.
7. 표 페이지에는 사진을 넣지 않는다. 원문 표와 참고문은 모두 남긴다.
8. 사용 이미지의 실제 파일, 중복 여부, 출처와 권리 상태를 확인한다. 한 사진은 기본 1회 사용이다.
9. 게시용 슬라이드에는 독자가 읽을 콘텐츠와 필요한 출처·권리 표기만 넣는다. 제작 상태·파일 안내·QA를 넣지 않는다.
10. 자료 조사, 이미지 확보, 파일 제작, 검사에 성공한 범위만 완료라고 보고한다.

## 3. 반드시 읽을 문서

- `references/audience-content-boundary.md` — 슬라이드 노출층과 제작 메타정보 분리
- `references/copy-guard.md` — 원문 무삭제·원문 선택·순서 검사
- `references/report-carousel-v3.md` — 승인된 텍스트 중심 규격
- `references/adaptive-density.md` — 본문 우선 공간 배분
- `references/image-research-and-placement.md` — 이미지 조사·선별·배정·권리
- `references/asset-intake-and-visual-fallback.md` — 입력 형식·대체 시각물
- `references/request-routing.md` — 짧은 지시 해석
- `references/production-workflow.md` — 실제 제작 공정
- `references/qa-checklist.md` — 완료 기준
- `references/cover-and-closing-slides.md` — 인스타 첫 장의 강한 텍스트 표지와 마지막 CTA 규칙
- `examples/2026-09-running-biomechanics-session.md` — 팔치기·리듬 카드뉴스 반복 수정에서 확정된 사례와 실패/개선 기록

현재 사용자 지시가 최우선이며 환경의 상위 지침과 안전 규칙을 따른다. 위 문서가 충돌하면 원문 보존과 노출층 분리 원칙을 먼저 적용한다. 충돌을 이유로 원문을 자동 삭제하지 않는다. v2~v3.2의 사진 우선·작은 본문·축약 예시는 과거 참고일 뿐 현재 기본값이 아니다.

## 4. 원문 작업 모드

### `preserve-exact` — 전체 유지 요청의 기본

`source.txt`의 원본 바이트·해시를 보존하고 모든 제목·문단·표 셀·각주·URL을 페이지에 실제 배치한다. 파일에 원문을 넣어 두는 것으로 슬라이드 누락을 보완하지 않는다. 줄바꿈과 페이지 분할만 허용하며 원문 순서는 유지한다.

### `reorder-without-rewrite` — 명시적으로 구조 변경을 허용했을 때만

원문 블록을 이동할 수 있으나 문장을 다시 쓰지 않는다. 이동 전후 블록 ID와 원문 범위를 기록하고 각 블록이 정확히 한 번 쓰였는지 검사한다. 일반 원문 보존 요청만으로 재배열을 허용하지 않는다.

### `edit-approved` — 요약·축약을 명시적으로 허용했을 때만

승인된 편집본을 별도 원문으로 잠근다. 사용자가 이후 전문 사용을 재지시하면 이 모드를 중지한다. 초기 보고서와 편집본이 혼재하면 최신 지시에서 가리킨 자료를 도구로 확인한다.

## 5. 타이포그래피와 이미지

- 기준 캔버스: 1080×1350, 4:5.
- 승인본 스타일 파일이 있으면 실제 폰트·좌표를 계승한다. 새 기본 본문은 **26px / 행간 39px**, 제목 56px, 부제목 36px이다.
- 페이지별 축소 금지. 먼저 보조 이미지·그래프를 축소 또는 제외하고 문단 분배·열 구성을 조정한다.
- 20장 고정과 원문·고정 폰트가 실제로 충돌할 때만 제약을 알린다. 몰래 요약하거나 21px 프리셋으로 후퇴하지 않는다.
- 여백은 재조판의 판단 자료이지 원문 삭제·무의미한 사진 추가의 근거가 아니다.
- 이미지 조사는 페이지별 설명 목적에서 시작한다. 자료를 모은 뒤 억지로 페이지를 만드는 방식을 피한다.

## 6. 공개·제작·내부 3층

- `public`: 제목, 부제, 본문, 원문 표, 보조 시각물의 라벨, 필요한 출처·사진 크레딧, 승인 브랜드와 페이지 번호.
- `production`: 원문 포함 여부, 전달 파일 목록, 작업 방식, 수정 내역, QA 요약. 보고서와 전달 메시지에는 허용한다.
- `internal`: 원문 오프셋, 해시, 중복 검사, 후보 탈락 사유, 폰트 측정, 오류 로그.

렌더러는 `audience=public`인 허용 역할만 그린다. `production`과 `internal` 문자열은 픽셀에 그리지 않는다. 필드가 없으면 임의로 public으로 간주하지 않는다.

### 슬라이드 금지 예시

`풀 텍스트`, `FULL TEXT`, `원문은 파일에 수록`, `첨부파일에서 원문 확인`, `원문 보존본`, `검수본`, `text-manifest`, `QA_REPORT`, `렌더링 완료` 등 제작자가 붙인 문구.

단어 차단기가 아니다. 실제 콘텐츠에 있는 `본 보고서는`, 조사 기간, 표본 기준, 연구 방법, 논문 제목, 사진 라이선스는 유지한다. 예외는 출처·역할·사유를 기록해 승인하고 자동 삭제하지 않는다.

## 7. 필수 제작 순서

1. 선택 원문과 승인 스타일 잠금.
2. public/production/internal 분리.
3. 전체 본문·원문 표부터 분할·실측.
4. 이미지 필요도 정의 → 조사 → 다운로드/실제 캡처 → 권리·중복·품질 확인 → 배정.
5. 보조 이미지가 본문을 밀면 보조 이미지를 제거하고 전체 순서 재검사.
6. 렌더링 전 `scripts/lint_public_surface.py`로 게시 문구 검사.
7. 요청 전체 PNG 렌더링. 모든 텍스트 draw call을 `render-surface.json`에 기록.
8. 실제 draw log에 동일 검사 재실행. 원문 대조와 텍스트 경계·가림 검사를 별도로 수행.
9. 모든 장을 개별·모바일·콘택트시트로 검토한 뒤 ZIP 생성.

검사기는 원문·데이터를 변경하지 않는다. 메타 문구가 원문 자체에 있으면 원문 보존과 공개 범위를 확인한 뒤 처리한다.

## 8. 기본 산출물

```text
<slug>/
  01.png ... 20.png
  preview.jpg
  preview.png
  production/
    source.txt
    text-manifest.txt
    page-map.json
    asset-map.json
    style.json
    render-surface.json
    PUBLIC_SURFACE_QA.json
    ASSET_AUDIT.md
    VISUAL_FALLBACK_LOG.md
    IMAGE_SOURCES.md
    CONTENT_REVIEW_NOTES.md
    QA_REPORT.md
<slug>.zip
```

제작 문서에는 필요한 설명을 충분히 남긴다. 슬라이드와 미리보기에는 그 설명을 인쇄하지 않는다. 출처·라이선스의 독자 노출 의무까지 없애지 않는다.

## 9. 실패 기준

원문 누락/대체, 표 셀 손실, 장별 본문 축소, 잘림·가림, 표 뒤 사진, 무관한 사진 반복, 허위 다운로드 주장, 생성형 페이지 조판, 슬라이드 속 제작 메타정보 중 하나라도 있으면 완료 처리하지 않는다.

## 10. 저장소 운영

피드백은 실행 문서·예시·검수에 함께 반영하고 GitHub 커밋 후 다시 읽어 확인한다. 저장소 업로드와 새 채팅 자동 로드는 같은 기능이 아니다. 새 작업에서 이 저장소의 SKILL.md를 실제 읽고 적용하며, 읽지 못했으면 적용했다고 말하지 않는다.
