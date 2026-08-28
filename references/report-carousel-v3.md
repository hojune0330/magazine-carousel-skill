# Report Carousel v3.2 — Large Type Adaptive Assets

## 상태

```yaml
profile: report-carousel-v3.2-large-type-adaptive-assets
status: active
canvas: 1080x1350
aspect_ratio: 4:5
legacy_profile: report-carousel-v3.1-large-type-adaptive-fill
```

이 문서는 고정 보고서 타이포그래피, 큰 본문, 텍스트 실측형 동적 패널, 실제 사진 무크롭 편집, 그래프·캡처·도식·저불쾌감 보조 시각물을 결합한 공식 시각 명세다.

핵심 원칙:

> **텍스트를 먼저 크게 조판하고, 사진·패널·표·그래프·캡처 레이어를 텍스트와 정보 성격에 맞춘다.**

> **이미지가 부족하면 장식이 아니라 근거가 있는 시각물로 해결한다.**

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
chart_primary: "#17191D"
chart_secondary: "#8A8E94"
```

- 표·본문 페이지는 warm_white를 기본으로 한다.
- 사진 페이지 패널은 warm_white 또는 dark_panel을 사용한다.
- 차트는 검정·회색·옐로 포인트를 기본으로 한다.
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

공통 헤더:

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
- 같은 데크에서 라벨을 고정한다.
- 사진·어두운 캡처 페이지는 흰색 라벨, 밝은 페이지는 검정 라벨을 쓸 수 있다.
- 노란 바 좌표는 고정한다.

공통 푸터:

- 좌하단: `01 / 20`
- 우하단: `@io_magazine / 장호준 코치`
- 모든 장에서 동일한 베이스라인을 사용한다.

## 3. 타이포그래피

폰트 우선순위:

1. Pretendard
2. Noto Sans CJK KR
3. Noto Sans KR
4. 시스템 산세리프

### `reading-large`

```yaml
label: 28/34, 700
main_title: 56/66, 800
section_title: 36/47, 750
subtitle: 30/41, 700
body: 23/35, 400
caption: 18/27, 400
table: 15/22, 400
table_header: 15/22, 700
chart_label: 15/21, 500
chart_value: 18/24, 700
reference: 11/16, 400
page_number: 30, 700
credit: 22, 400
```

### `source-dense-large`

```yaml
label: 28/34, 700
main_title: 56/66, 800
section_title: 36/47, 750
subtitle: 30/41, 700
body: 21/32, 400
caption: 17/25, 400
table: 14/20, 400
table_header: 14/20, 700
chart_label: 14/20, 500
chart_value: 17/23, 700
reference: 11/16, 400
page_number: 30, 700
credit: 22, 400
```

강제 규칙:

- 한 데크는 하나의 프리셋을 사용한다.
- 일반 본문은 20px 미만으로 내려가지 않는다.
- 장마다 본문 폰트 크기를 바꾸지 않는다.
- 제목은 줄바꿈으로 해결한다.
- 오버플로는 페이지 경계·시각물 면적·열 구성으로 해결한다.

## 4. 텍스트 실측형 레이어

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

- 텍스트가 적으면 패널을 줄이고 시각물을 키운다.
- 텍스트가 많으면 시각물을 줄인다.
- 시각물 의미가 사라질 정도로 작아지면 body-balanced로 전환한다.

## 5. 채움 지표

```yaml
normal_vertical_fill: 0.86~0.97
cover_vertical_fill: 0.72~0.94
panel_utilization: 0.72~0.92
table_vertical_fill: 0.72~0.92
chart_vertical_fill: 0.70~0.92
```

재조판 조건:

- 140px 이상 연속된 의도하지 않은 빈 띠
- usable height의 10% 이상 무의미한 빈 영역
- 본문 끝과 푸터 사이 180px 이상 공백
- panel utilization 0.65 미만 또는 0.96 초과

표지·챕터 오프닝의 의도적 여백은 예외다.

## 6. 밝은 보고서 페이지

### `body-balanced`

- 장문 보고서용
- 1열 기본, 필요 시 2열
- 본문이 짧으면 다음 페이지의 완전 문단을 당긴다.
- 그래도 짧으면 source-highlight, chart-report, diagram-explainer 중 내용에 맞는 타입으로 전환한다.

### `table-balanced`

- 사진 사용 금지
- warm_white 배경
- 제목 + 짧은 도입 + 표
- 검정 상단선, 회색 내부선, 검정 하단선
- 행 높이 64~118px
- 표 폰트는 전 장 동일
- 표가 상단에 몰리고 하단이 비면 행 높이와 위치를 재배분한다.

## 7. 실제 사진 공통 규칙

전경 사진:

- contain
- 원본 비율 유지
- 얼굴, 머리, 손, 발, 결승선, 허들, 배턴 등 핵심 요소 보존
- 무크롭

배경 사진:

- 동일 이미지를 cover로 확대 가능
- blur 18~36px
- 밝기 35~65%
- 필요 시 색온도·채도 감소

텍스트:

- 장문을 사진에 직접 올리지 않는다.
- 밝은 패널 0.94 이상, 어두운 패널 0.80 이상
- 패널 높이는 텍스트 실측값으로 결정한다.

## 8. 사진 페이지 타입

### `cover-photo`

- 전면 블러 배경 + 중앙 무크롭 사진
- 제목 패널은 하단 또는 좌측
- 본문 1문단 이하 권장

### `photo-bottom-panel`

- 사진이 상단과 배경의 주인공
- 패널은 텍스트 실측형
- 짧은 본문에 큰 고정 패널을 쓰지 않는다.

### `photo-top-report`

- 가로 사진 + 하단 1열/2열 보고서
- 사진 높이 300~720px 범위에서 계산
- letterbox 허용

### `photo-split`

- 세로 사진 + 짧거나 중간 본문
- 가로 사진을 좁은 세로 칸에 억지로 넣지 않는다.

### `photo-duo`

- 두 사진을 동일 시각 무게로 배치
- 눈높이 또는 주 동작 위치를 맞춘다.

### `photo-stack`

- 2~3장 사진을 위아래로 배치
- 각 사진 무크롭 contain
- 시간적 전개·선수 비교에 사용

## 9. 데이터 시각화 타입

### `chart-report`

구성:

- 제목
- 핵심 그래프 1개
- 1~3문장 해석
- 축·단위·기간·출처

허용:

- 가로/세로 막대
- 선 그래프
- slope chart
- 기록 타임라인
- 순위·기록 ladder
- 구간 페이스 비교

금지:

- 실제 값 없는 그래프
- 3D 그래프
- 장식성 원형 차트 남발
- 축을 잘라 차이를 과장하는 구성

그래프 레이블과 수치는 코드로 조판한다.

## 10. 실제 캡처 타입

### `evidence-capture`

구성:

- 실제 웹/PDF/영상/앱 캡처
- 출처 캡션
- 짧은 해설

규칙:

- 원본 맥락이 식별될 정도의 주변 정보를 남긴다.
- URL, 페이지 제목, 날짜, PDF 페이지 또는 영상 시간코드를 기록한다.
- 개인정보는 제거한다.
- 데이터·문구는 변조하지 않는다.
- 긴 기사 전체나 유료 콘텐츠 전체를 복제하지 않는다.

## 11. 도식 타입

### `diagram-explainer`

- 타임라인, 흐름도, 트랙 구조, 훈련 주기, 원인→적응→결과
- 원문에 없는 인과관계를 만들지 않는다.
- 선·화살표·수치·캡션은 코드로 조판한다.

### `icon-grid`

- 2~4개 의미형 아이콘 + 짧은 설명
- 6개 이상 장식 아이콘 남발 금지
- 아이콘은 같은 선 굵기와 스타일을 사용한다.

### `character-explainer`

- 친근한 2D 캐릭터 또는 스포츠 실루엣
- 초보 설명·가벼운 개념에 사용
- 실제 인물 대체나 사실 증명 용도로 사용하지 않는다.

## 12. 저불쾌감 보조 시각 프로필

```yaml
style: clean-flat-2d
mood: healthy-calm-friendly
realism: low-to-medium
uncanny_level: very-low
discomfort_level: very-low
violence: none
gore: none
medical_invasiveness: none
sexualization: none
facial_distortion: none
anatomy_distortion: none
```

금지:

- 실제 선수의 가짜 경기·수상 사진
- 포토리얼 가짜 사건
- 기괴한 얼굴·손·신체
- 부상 클로즈업, 피, 주사, 수술, 체액
- 공포·과도한 통증
- 성적 대상화
- 저작권 캐릭터·브랜드 모방
- 생성 이미지 내부의 긴 한국어 본문·표·페이지 번호

보조 자산만 생성하고 최종 페이지는 코드로 렌더링한다.

## 13. source-highlight

- 원문 속 문장·숫자·기록을 36~52px로 승격
- 새로운 주장을 만들지 않는다.
- 본문과 중복하지 않는다.
- text manifest에는 한 번만 기록한다.

## 14. 빈 공간 해결 순서

1. 패널을 텍스트 높이에 맞게 줄인다.
2. 실제 사진을 남은 영역까지 확대한다.
3. 다음 페이지 완전 문단을 앞당긴다.
4. 관련 사진을 photo-duo/photo-stack으로 추가한다.
5. 실제 캡처·그래프·표·도식 중 내용에 맞는 시각물을 사용한다.
6. 저불쾌감 보조 아이콘·캐릭터·일러스트를 마지막 수단으로 사용한다.
7. source-highlight 또는 body-balanced로 전환한다.

금지:

- 의미 없는 장식 아이콘·박스
- 실제 데이터 없는 가짜 그래프
- 문장 반복
- 장별 폰트 축소

## 15. 시각물 선택 규칙

```text
실제 인물·경기·제품 → 실제 사진
공식 결과·발표·문서 → 실제 캡처
숫자·순위·변화 → 그래프 또는 표
시간 순서·과정 → 타임라인·흐름도
복잡한 개념 → 도식·아이콘
초보 설명·가벼운 개념 → 낮은 불쾌감 2D 캐릭터
적합한 시각 근거 없음 → source-highlight
```

- 같은 사진은 기본 1회 사용
- 표 페이지에 사진을 억지로 넣지 않는다.
- 생성 보조 이미지를 실제 증거처럼 사용하지 않는다.

## 16. 출처 페이지

- 긴 URL은 2열 가능
- reference 폰트 11px
- 넘치면 별도 페이지로 분할
- 이미지·캡처·그래프·생성 자산 출처는 IMAGE_SOURCES.md와 asset-map에 기록

## 17. 실패 기준

- 일반 본문 20px 미만
- 장마다 본문 크기가 다름
- 큰 의도하지 않은 빈 띠
- 패널 활용률 기준 위반
- 사진 전경 fill-crop으로 핵심 피사체 잘림
- 표 뒤 사진 사용
- 장문이 사진 위에 직접 올라감
- 같은 사진 승인 없이 반복
- 출처 없는 캡처
- 실제 데이터 없는 그래프
- 생성 보조 이미지를 실제 사건의 증거로 사용
- 불쾌감·왜곡이 큰 아이콘·캐릭터
- 사용자가 생성 기능을 금지했는데 generated-* 자산 사용
- 푸터 이동
- 콘택트시트에서 서로 다른 템플릿처럼 보임

## 18. 공식 선언

**본문을 먼저 크게 조판하고 사진·패널·표·그래프·캡처 레이어를 텍스트와 정보 근거에 맞춘다.**

**이미지가 부족하면 실제 자료와 실제 데이터 기반 시각물을 우선하며, 보조 생성 이미지는 매우 낮은 불쾌감의 마지막 수단으로만 사용한다.**
