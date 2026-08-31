# Report Carousel v3.3 — Text First, Audience Clean

```yaml
profile: report-carousel-v3.3-text-first-audience-clean
status: active
canvas: 1080x1350
reference: japan_marathon_fulltext_20_v2
```

## 1. 시각 기준

승인된 텍스트 중심 보고서형을 유지한다. 제목·본문의 우선순위를 사진 중심 광고형으로 되돌리지 않는다. 제작자가 넣은 `FULL TEXT` 헤더와 원문 파일 안내 푸터는 제거한다. `ELITE REPORT`, 페이지 번호, 승인 계정 표기는 유지한다.

## 2. 스타일 잠금

실제 승인 렌더러의 style.json이 있으면 먼저 읽고 계승한다. 다음은 신규 작업 기본값이다.

```yaml
background: '#FAF9F6'
ink: '#121212'
muted: '#505050'
rule: '#BEBEBE'
accent: '#FFD300'
margin_x: 70
content_width: 940
label_x: 104
label_y: 104
bar: [70, 96, 12, 56]
title_x: 70
title_y: 205
footer_rule_y: 1220
footer_text_y: 1244
body_bottom: 1190
main_title: {size: 56, line_height: 66, weight: 800}
section_title: {size: 36, line_height: 47, weight: 700}
subtitle: {size: 30, line_height: 41, weight: 700}
body: {size: 26, line_height: 39, weight: 400}
caption: {size: 18, line_height: 27, weight: 400}
table: {size: 18, line_height: 27, weight: 400}
reference: {size: 12, line_height: 18, weight: 400}
page_number: {size: 30, weight: 700}
credit: {size: 22, weight: 400}
```

폰트는 Pretendard → Noto Sans CJK KR → Noto Sans KR 순으로 사용할 수 있는 실제 폰트를 고정한다. 폰트 파일을 사용자에게 배포하지 않는다. 기존 승인본 재작업 시 table/reference는 실제 승인값을 유지한다. 페이지마다 더 작은 프리셋을 선택하지 않는다.

## 3. 텍스트 중심 타입

- `text-report`: 제목 + 원문 본문. 기본 타입.
- `text-photo-support`: 본문 전부 + 남는 영역의 관련 사진.
- `text-side-note`: 원문 본문과 짧은 독자용 설명의 분리. 내용 추가가 승인된 경우만.
- `table-report`: 원문 표·도입·각주. 사진 없음.
- `text-chart-support`: 원문 본문을 유지한 뒤 보조 그래프.
- `text-evidence-support`: 원문 본문 + 실제 근거 캡처.
- `source-highlight`: 원문 구절을 제자리에서 강조. 단독 요약으로 본문을 대체하지 않음.
- `cover` / `conclusion`: 승인 제목·본문을 지킨 범위의 표지·엔딩.

이전 photo-hero/photo-stack/chart-report 타입은 명시적 사진 중심 편집 요청에서만 사용한다. 원문 전체 보존 작업의 기본이 아니다.

## 4. 텍스트 측정

제목 → 부제목 → 본문 → 원문 표 → 각주/필수 출처 순으로 실제 폰트 메트릭을 측정한다. 고정 헤더·푸터를 제외한 가용 영역 안에 모든 원문이 들어가는지 먼저 확인한다.

본문이 들어간 뒤에만 보조 시각물의 공간을 계산한다. 일반 장의 보조 이미지 면적은 가용 본문 영역의 약 35% 이하를 출발점으로 삼되 강제 목표는 아니다. 사진 없이 끝내도 된다. 표지 사진은 원문이 밀리지 않는 경우만 더 크게 쓸 수 있다.

## 5. 사진과 표

전경 사진은 contain, 원본 비율, 무크롭. 텍스트와 전경 사진의 사각형이 겹치지 않아야 한다. 블러 배경을 사용해도 전경 위의 글자 가림을 정당화하지 않는다.

표는 원문 열·행·값 유지, 얇은 선, 같은 역할의 폰트 고정. 행 높이는 실제 셀 텍스트에 맞춘다. 줄 수가 많아도 118px 상한 때문에 잘리지 않게 한다. 표를 시각화로 대체하지 않는다.

## 6. 여백과 잘림

큰 빈 띠는 검토 경고이지 무조건 실패가 아니다. 제목 길이, 문단 종료, 표 분할로 생긴 의미 있는 여백은 허용한다. 사진·문장을 억지로 반복하거나 행간을 늘려 공간을 채우지 않는다.

모든 텍스트의 실제 glyph 경계, CSS overflow, clipping mask, 도형·사진 가림, 우측 끝, 하단 안전 영역을 확인한다. 매니페스트에만 있는 문장은 실제 페이지에 들어간 것으로 보지 않는다.

## 7. 공개층

템플릿의 헤더·푸터·캡션·table note에도 `audience=public` 규칙을 적용한다. 스킬명, 모드명, 버전, FULL TEXT, 첨부파일 안내, QA 결과는 production 문서에만 둔다. 필요한 연구 한계·사진 권리·데이터 출처는 public에 남긴다.
