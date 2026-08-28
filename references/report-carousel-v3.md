# Report Carousel v3 — Render-first Visual System

## 상태

```yaml
profile: report-carousel-v3-render-first
status: active
legacy_profile: report-carousel-v2
canvas: 1080x1350
aspect_ratio: 4:5
```

이 문서는 고정 보고서 타이포그래피와 사진 중심 무크롭 편집을 결합한 공식 시각 명세다.

## 1. 기본 색상

```yaml
warm_white: "#FAF9F6"
ink: "#121212"
muted: "#505050"
hairline: "#BEBEBE"
table_grid: "#CBCBCB"
accent_yellow: "#FFD300"
dark_panel: "#111318"
dark_panel_opacity: 0.82
light_panel_opacity: 0.96
```

- 표·본문 페이지는 warm_white를 기본으로 한다.
- 사진 페이지 패널은 warm_white 또는 dark_panel 중 하나를 사용한다.
- 장마다 무작위 색상을 만들지 않는다.
- 그림자, 광택, 네온, 과도한 그라디언트는 금지한다.

## 2. 고정 캔버스와 여백

```yaml
width: 1080
height: 1350
margin_left: 70
margin_right: 70
content_width: 940
header_top: 92
footer_rule_y: 1220
footer_text_y: 1244
footer_bottom_safe: 46
```

### 공통 헤더

```yaml
label_bar:
  x: 70
  y: 96
  width: 12
  height: 56
label_text:
  x: 104
  y: 104
```

- 기본 라벨: `ELITE REPORT`
- 같은 데크에서 라벨은 하나로 고정한다.
- 사진 페이지에서는 흰색 라벨, 밝은 페이지에서는 검정 라벨을 쓸 수 있다.
- 노란 바 위치는 바뀌지 않는다.

### 공통 푸터

- 좌하단: `01 / 20`
- 우하단: `@io_magazine / 장호준 코치`
- 푸터는 모든 장에서 동일한 베이스라인을 쓴다.
- 사진 페이지에서는 충분한 대비를 확보한다.

## 3. 타이포그래피

폰트 우선순위:

1. Pretendard
2. Noto Sans CJK KR
3. Noto Sans KR
4. 시스템 산세리프

1080×1350 기준:

```yaml
label:
  size: 28
  weight: 700
  line_height: 34
title:
  size: 50
  weight: 800
  line_height: 62
section_title:
  size: 31
  weight: 750
  line_height: 42
subtitle:
  size: 27
  weight: 700
  line_height: 38
body:
  size: 17
  weight: 400
  line_height: 27
body_compact:
  size: 16
  weight: 400
  line_height: 25
caption:
  size: 14
  weight: 400
  line_height: 21
table:
  size: 11
  weight: 400
  line_height: 16
table_header:
  size: 11
  weight: 700
  line_height: 16
reference:
  size: 9
  weight: 400
  line_height: 13
page_number:
  size: 30
  weight: 700
credit:
  size: 24
  weight: 400
```

강제 규칙:

- 같은 역할의 폰트 크기는 전 장에서 고정한다.
- `body_compact`는 사전에 지정된 고밀도 페이지 타입에서만 쓴다. 오버플로가 생겼다고 임의 적용하지 않는다.
- 제목은 크기를 줄이지 않고 줄바꿈한다.
- 본문은 넘치면 다음 장으로 넘긴다.

## 4. 밝은 보고서 페이지

### `body`

```yaml
title:
  x: 70
  y: 205
body:
  x: 70
  y: dynamic_after_title
  width: 940
  bottom: 1190
```

- 장문 보고서용
- 1열을 기본으로 하며 필요할 때 2열 사용 가능
- F-시선보다 문단 안정성을 우선한다.

### `table`

- 사진 사용 금지
- warm_white 배경
- 제목 + 짧은 도입 + 표
- 검정 상단선, 회색 내부선, 검정 하단선
- 표 셀은 가운데 정렬 기본, 긴 비고는 좌측 정렬 가능
- 행 높이는 텍스트에 맞춰 늘린다.
- 표 폰트는 모든 표 페이지에서 동일하다.

## 5. 사진 페이지 공통 규칙

전경 사진:

- contain 방식
- 원본 비율 유지
- 얼굴, 머리, 손, 발, 결승선, 허들, 배턴 등 핵심 요소 보존
- 무크롭이 기본

배경 사진:

- 동일 이미지를 cover로 확대 가능
- blur 18~36px
- 밝기 35~65%
- 필요 시 색온도와 채도를 낮춘다.
- 배경은 전경 사진의 빈 공간 채움용이다.

텍스트:

- 장문을 사진에 바로 얹지 않는다.
- 패널의 최소 불투명도는 밝은 패널 0.94, 어두운 패널 0.78이다.
- 사진과 텍스트의 경계가 명확해야 한다.

## 6. 사진 페이지 프리셋

### `cover-photo`

- 전면 블러 배경 + 중앙 무크롭 전경 사진
- 제목 패널은 하단 또는 좌측에 둔다.
- 표지에서 본문은 1문단 이하가 기본이다.

### `photo-bottom-panel`

패널 프리셋:

```yaml
small:
  panel_top: 895
medium:
  panel_top: 790
large:
  panel_top: 660
```

- 사진이 상단과 배경의 주인공이다.
- 패널 높이는 텍스트에 따라 small/medium/large 중 선택한다.
- 패널 내부 글자를 줄여 맞추지 않는다.

### `photo-top-report`

```yaml
photo_top: 0
photo_height_options: [430, 520, 610]
report_top: dynamic
```

- 가로 사진과 장문에 적합하다.
- 사진 아래 본문은 1열 또는 2열이다.
- 전경 사진 전체가 보이도록 letterbox를 허용한다.

### `photo-split`

```yaml
left:
  x: 40
  width: 500
right:
  x: 570
  width: 470
```

- 세로 사진 + 짧거나 중간 길이 본문에 사용한다.
- 가로 사진을 좁은 세로 칸에 억지로 넣지 않는다.

### `photo-duo`

- 두 사진을 동일한 시각 무게로 배치한다.
- 눈높이 또는 주 동작 위치를 맞춘다.
- 같은 장면의 중복 사진은 사용하지 않는다.

### `photo-stack`

- 2~3장의 사진을 위아래로 쌓는다.
- 각 사진은 무크롭 contain을 유지한다.
- 사진 사이 간격은 2~6px로 통일한다.
- 여러 선수·여러 종목의 시간적 전개에 적합하다.

## 7. 사진 선택 규칙

- 사진 내용과 해당 페이지 원문이 연결돼야 한다.
- 선수 소개에는 해당 선수 단독 또는 명확히 식별 가능한 사진을 쓴다.
- 경쟁 구도 페이지에는 함께 나온 경기 사진을 우선한다.
- 허들 전향 설명에는 허들 사진을 우선한다.
- 표 페이지에 남는 사진을 억지로 배치하지 않는다.
- 한 데크 안에서 같은 사진은 기본 1회 사용이다.

## 8. 빈 공간 규칙

`빈 공간을 최대한 없게`라는 요청은 다음처럼 해석한다.

- 사진 페이지는 사진 또는 패널이 캔버스를 충분히 채우게 한다.
- 의미 없는 큰 여백을 만들지 않는다.
- 그러나 표·장문 보고서 페이지에서는 가독성을 위한 여백을 유지한다.
- 원문을 억지로 늘리거나 장식 요소로 공간을 채우지 않는다.

## 9. 출처 페이지

- 긴 URL은 2열로 구성할 수 있다.
- reference 폰트는 9px 고정
- 출처 목록이 넘치면 별도 페이지로 분할한다.
- 이미지 출처는 본문 출처와 별도의 `IMAGE_SOURCES.md`에도 기록한다.

## 10. 실패 기준

- 사진 전경이 fill-crop되어 얼굴·발·동작이 잘림
- 표 뒤에 사진이 있음
- 장문이 사진 위에 직접 올라가 읽히지 않음
- 페이지마다 제목 위치와 크기가 달라짐
- 같은 사진이 승인 없이 반복됨
- 패널 높이를 맞추려고 본문 폰트를 축소함
- 푸터가 사진이나 패널에 따라 이동함
- 콘택트시트에서 서로 다른 템플릿처럼 보임
