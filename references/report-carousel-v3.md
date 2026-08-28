# Report Carousel v3.1 — Large Type Adaptive Fill

## 상태

```yaml
profile: report-carousel-v3.1-large-type-adaptive-fill
status: active
canvas: 1080x1350
aspect_ratio: 4:5
legacy_profile: report-carousel-v3-render-first
```

이 문서는 고정 보고서 타이포그래피, 사진 중심 무크롭 편집, 큰 본문, 텍스트 실측형 동적 패널을 결합한 공식 시각 명세다.

핵심 원칙은 하나다.

> **텍스트를 먼저 크게 조판하고, 사진·패널·표 레이어를 그 텍스트에 맞춘다.**

## 1. 기본 색상

```yaml
warm_white: "#FAF9F6"
ink: "#121212"
muted: "#505050"
hairline: "#BEBEBE"
table_grid: "#CBCBCB"
accent_yellow: "#FFD300"
dark_panel: "#111318"
dark_panel_opacity: 0.84
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
- 사진 페이지에서는 흰색, 밝은 페이지에서는 검정 라벨을 쓸 수 있다.
- 노란 바 좌표는 고정한다.

### 공통 푸터

- 좌하단: `01 / 20`
- 우하단: `@io_magazine / 장호준 코치`
- 모든 장에서 동일한 베이스라인을 사용한다.

## 3. 큰 본문 타이포그래피

폰트 우선순위:

1. Pretendard
2. Noto Sans CJK KR
3. Noto Sans KR
4. 시스템 산세리프

### `reading-large` — 기본

```yaml
label: 28/34, 700
main_title: 56/66, 800
section_title: 36/47, 750
subtitle: 30/41, 700
body: 23/35, 400
caption: 18/27, 400
table: 15/22, 400
table_header: 15/22, 700
reference: 11/16, 400
page_number: 30, 700
credit: 22, 400
```

### `source-dense-large`

원문 전체 보존 + 고정 장수 + 장문이 동시에 필요한 경우에만 데크 전체에 적용한다.

```yaml
label: 28/34, 700
main_title: 56/66, 800
section_title: 36/47, 750
subtitle: 30/41, 700
body: 21/32, 400
caption: 17/25, 400
table: 14/20, 400
table_header: 14/20, 700
reference: 11/16, 400
page_number: 30, 700
credit: 22, 400
```

강제 규칙:

- 한 데크는 렌더링 전에 하나의 프리셋을 선택한다.
- 장마다 본문 폰트 크기를 바꾸지 않는다.
- 일반 본문은 20px 미만으로 내려가지 않는다.
- 제목은 크기를 줄이지 않고 줄바꿈한다.
- 오버플로는 페이지 경계·사진 면적·열 구성으로 해결한다.

## 4. 텍스트 실측형 패널

패널은 fixed small/medium/large만으로 결정하지 않는다.

```text
required_panel_height
= top_padding
+ title_height
+ title_body_gap
+ body_height
+ bottom_padding
```

8px 그리드로 반올림한다.

```yaml
panel_min_height: 330
panel_max_height: 930
panel_padding_x: 34~48
panel_padding_top: 28~40
panel_padding_bottom: 28~40
title_body_gap: 20~28
```

`photo-bottom-panel`:

```text
panel_top = floor_to_8(footer_safe_top - required_panel_height)
photo_height = panel_top - photo_top - gap
```

- 텍스트가 적으면 패널을 줄이고 사진을 키운다.
- 텍스트가 많으면 사진을 줄인다.
- 사진이 의미를 잃을 정도로 작아지면 `body-balanced`로 전환한다.

## 5. 채움 지표

```yaml
normal_vertical_fill: 0.86~0.97
cover_vertical_fill: 0.72~0.94
panel_utilization: 0.72~0.92
table_vertical_fill: 0.72~0.92
```

재조판 조건:

- 140px 이상 연속된 의도하지 않은 빈 띠
- usable height의 10% 이상인 무의미한 빈 영역
- 본문 끝과 푸터 사이 180px 이상 공백
- panel utilization 0.65 미만 또는 0.96 초과

표지와 챕터 오프닝의 의도적 여백은 예외다.

## 6. 밝은 보고서 페이지

### `body-balanced`

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
- 1열 기본, 필요 시 2열
- 본문이 짧으면 다음 페이지의 완전한 문단을 당겨 채운다.
- 그래도 짧으면 source-highlight 또는 큰 사진형으로 전환한다.

### `table-balanced`

- 사진 사용 금지
- warm_white 배경
- 제목 + 짧은 도입 + 표
- 검정 상단선, 회색 내부선, 검정 하단선
- 행 높이 64~118px
- 표 폰트는 선택 프리셋으로 전 장 동일
- 표가 상단에 몰리고 하단이 비면 행 높이와 표 위치를 재배분한다.

## 7. 사진 공통 규칙

전경 사진:

- contain 방식
- 원본 비율 유지
- 얼굴, 머리, 손, 발, 결승선, 허들, 배턴 등 핵심 요소 보존
- 무크롭

배경 사진:

- 동일 이미지를 cover로 확대 가능
- blur 18~36px
- 밝기 35~65%
- 필요 시 색온도와 채도 감소

텍스트:

- 장문을 사진에 직접 올리지 않는다.
- 밝은 패널 0.94 이상, 어두운 패널 0.80 이상 불투명도
- 패널 높이는 텍스트 실측값으로 결정한다.

## 8. 사진 페이지 타입

### `cover-photo`

- 전면 블러 배경 + 중앙 무크롭 전경 사진
- 제목 패널은 하단 또는 좌측
- 본문 1문단 이하 권장

### `photo-bottom-panel`

- 사진이 상단과 배경의 주인공
- 패널은 텍스트 실측형
- 짧은 본문인데 큰 고정 패널을 쓰지 않는다.

### `photo-top-report`

- 가로 사진 + 하단 1열/2열 보고서
- 사진 높이는 300~720px 범위에서 텍스트에 따라 계산
- letterbox 허용

### `photo-split`

- 세로 사진 + 짧거나 중간 길이 본문
- 가로 사진을 좁은 세로 칸에 억지로 넣지 않는다.

### `photo-duo`

- 두 사진을 동일한 시각 무게로 배치
- 눈높이 또는 주 동작 위치를 맞춘다.

### `photo-stack`

- 2~3장의 사진을 위아래로 쌓는다.
- 각 사진은 무크롭 contain
- 시간적 전개·선수 비교에 사용

### `source-highlight`

- 원문 속 문장·숫자·기록을 36~52px로 크게 승격
- 새로운 주장을 만들지 않는다.
- 본문과 중복하지 않는다.
- text manifest에는 한 번만 기록한다.

## 9. 빈 공간 해결 순서

1. 패널을 텍스트 높이에 맞게 줄인다.
2. 사진을 남은 영역까지 확대한다.
3. 다음 페이지의 완전한 문장·문단을 앞당긴다.
4. 관련 사진을 photo-duo/photo-stack으로 추가한다.
5. 원문 구절을 source-highlight로 승격한다.
6. 1열/2열을 바꾼다.
7. 적합한 사진이 없으면 body-balanced로 전환한다.

금지:

- 의미 없는 아이콘·박스·가짜 그래프로 공간 채우기
- 문장 반복
- 장별 폰트 축소

## 10. 사진 선택 규칙

- 사진 내용과 해당 페이지 원문이 연결돼야 한다.
- 선수 소개에는 해당 선수 단독 또는 명확한 식별 사진
- 경쟁 구도에는 함께 나온 경기 사진
- 허들 전향에는 허들 사진
- 표 페이지에 남는 사진을 억지로 배치하지 않는다.
- 같은 사진은 기본 1회 사용

## 11. 출처 페이지

- 긴 URL은 2열 구성 가능
- reference 폰트 11px
- 넘치면 별도 페이지로 분할
- 이미지 출처는 `IMAGE_SOURCES.md`에 별도 기록

## 12. 실패 기준

- 일반 본문 20px 미만
- 장마다 본문 크기가 다름
- 140px 이상 의도하지 않은 빈 띠
- 패널 활용률 0.65 미만 또는 0.96 초과
- 본문이 짧은데 패널이 화면 절반 이상
- 사진 전경 fill-crop으로 핵심 피사체 잘림
- 표 뒤 사진 사용
- 장문이 사진 위에 직접 올라가 읽히지 않음
- 같은 사진 승인 없이 반복
- 패널을 맞추려고 본문 폰트 축소
- 푸터 이동
- 콘택트시트에서 서로 다른 템플릿처럼 보임

## 13. 공식 선언

**본문을 먼저 크게 읽히게 조판하고, 사진·패널·표 레이어를 텍스트 실측값에 맞춘다.**

**폰트는 레이어에 맞추지 않고, 레이어가 텍스트에 맞춘다.**
