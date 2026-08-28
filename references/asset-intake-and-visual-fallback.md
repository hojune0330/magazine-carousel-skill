# Asset Intake & Visual Fallback — 이미지 업로드 형식과 부족 자산 대응

이 문서는 캐러셀 제작에 필요한 이미지가 부족하거나, 업로드된 이미지의 비율·화질·내용이 페이지 구성과 맞지 않을 때 사용할 **입력 규격, 자산 점검, 대체 시각물 우선순위, 캡처·그래프·표·보조 생성 이미지 규칙**을 정의한다.

핵심 원칙은 다음과 같다.

> **사진이 부족하다고 의미 없는 장식을 넣지 않는다. 페이지의 정보 성격에 가장 맞는 시각 근거를 선택한다.**

> **실제 사진·실제 데이터·실제 화면 캡처를 우선하고, 생성형 보조 이미지는 가장 마지막 단계에서만 쓴다.**

---

## 1. 이미지 업로드 형식

### 1.1 권장 래스터 이미지

우선순위:

1. `JPG` / `JPEG` — 경기·인물·현장 사진
2. `PNG` — 투명 배경 로고·도식·스크린샷
3. `WebP` — 고화질 사진·그래픽

조건부 허용:

- `HEIC` / `HEIF` — 렌더링 전 sRGB JPG 또는 PNG로 변환
- `TIFF` — 렌더링 전 sRGB PNG/JPG로 변환
- `BMP` — 품질 확인 후 PNG로 변환
- `GIF` — 정지 이미지가 필요하면 지정 프레임 또는 첫 유효 프레임 추출

### 1.2 벡터·문서·데이터

- `SVG` — 로고, 아이콘, 선형 도식
- `PDF` — 공식 보고서, 차트, 표, 경기 결과 문서. 필요한 페이지만 캡처하거나 벡터로 추출
- `CSV`, `XLSX`, `JSON` — 그래프·표 생성용 원본 데이터
- `PPTX`, `DOCX` — 참고 레이아웃이나 내부 표·이미지 추출용

### 1.3 동영상 프레임

- `MP4`, `MOV`, `WebM`은 사용자가 경기 장면 캡처를 허용했을 때만 사용한다.
- 프레임은 해당 장면의 시간코드와 함께 기록한다.
- 흔들림·모션블러가 심한 프레임은 사용하지 않는다.

### 1.4 ZIP 일괄 업로드

이미지가 많으면 ZIP을 권장한다.

```text
assets/
  photos/
  screenshots/
  logos/
  documents/
  data/
  asset-notes.csv
```

`asset-notes.csv` 권장 열:

```text
filename,subject,event,date,source_url,author,license,preferred_page,notes
```

### 1.5 해상도 권장값

- 전면 또는 대형 사진: 짧은 변 1600px 이상, 권장 2400px 이상
- 절반 폭 사진: 짧은 변 1000px 이상
- 스크린샷: 가로 1440px 이상 또는 2× 캡처
- 투명 로고: SVG 또는 1200px 이상 PNG
- 1080×1350보다 작은 사진은 업스케일을 기본 해결책으로 쓰지 않는다. 작은 슬롯으로 전환한다.

### 1.6 색상·방향·투명도

- 기본 색공간은 sRGB로 통일한다.
- CMYK, Display-P3는 sRGB로 변환한다.
- EXIF 방향을 실제 픽셀에 반영한 뒤 메타데이터 방향값을 정리한다.
- 투명 PNG는 알파 채널을 유지한다.
- 파일명은 가능하면 `01_subject_event.jpg`처럼 의미 있게 정리한다.

---

## 2. 업로드 직후 자산 감사

모든 업로드는 렌더링 전에 다음 항목을 검사한다.

```yaml
file_exists: true
format_supported: true
width: N
height: N
orientation: portrait|landscape|square
color_space: sRGB
has_alpha: true|false
sha256: "..."
perceptual_hash: "..."
subject: "..."
quality: high|medium|low
rights_status: user-upload|verified|needs-review
```

### 중복 검사

- SHA-256 동일: 완전 중복
- perceptual hash 근접: 리사이즈·재압축·색보정된 동일 이미지 가능성
- 같은 순간을 연속 촬영한 근접 중복: 콘택트시트에서 수동 확인
- 기본 사용 횟수는 한 이미지당 1회

### 페이지 적합성 검사

각 자산은 다음 태그를 가진다.

- 선수/인물
- 경기/현장
- 제품/장비
- 데이터/차트
- 화면/문서
- 로고/브랜드
- 개념/도식

페이지 원문과 태그가 연결되지 않으면 억지로 배치하지 않는다.

---

## 3. 이미지가 충분한지 판단하는 법

페이지마다 사진이 필요한 것은 아니다. 먼저 페이지 역할을 구분한다.

```yaml
photo_required:
  - cover-photo
  - athlete-profile
  - event-moment
photo_preferred:
  - photo-bottom-panel
  - photo-top-report
photo_optional:
  - body-balanced
  - source-highlight
photo_forbidden:
  - table-balanced
  - dense-sources
```

자산 부족은 단순히 `페이지 수 > 사진 수`로 판단하지 않는다.

다음 중 하나면 부족 상태다.

- 사진 필수 페이지에 관련 사진이 없음
- 같은 사진을 2회 이상 써야만 구성이 가능함
- 사진 비율이 슬롯과 맞지 않아 핵심 피사체가 지나치게 작아짐
- 해상도가 모바일 게시 품질을 충족하지 못함
- 원문과 사진의 의미 연결이 약함
- 라이선스나 출처를 확인할 수 없음

이 경우 `VISUAL_FALLBACK_LOG.md`에 부족 원인과 선택한 대체 수단을 기록한다.

---

## 4. 시각 자산 부족 시 우선순위

### Tier 1 — 사용자 제공 실제 이미지

- 가장 먼저 사용한다.
- 전경은 무크롭 contain.
- 같은 이미지의 블러 배경은 별도 사용 횟수로 보지 않는다.

### Tier 2 — 실제 원본 이미지 추가 확보

- 사용자 지정 링크, 공식 기관, 대회 주최사, 선수·팀 공식 채널, Wikimedia Commons 등에서 실제 원본을 다운로드한다.
- 검색 썸네일이나 HTML 캡처를 원본 사진처럼 쓰지 않는다.
- 출처·작가·라이선스·다운로드 날짜를 기록한다.

### Tier 3 — 실제 화면·문서·영상 캡처

페이지 내용이 기록표, 공식 발표, 경기 결과, 제품 화면, 논문 도표와 직접 연결되면 실제 캡처가 사진보다 낫다.

허용:

- 공식 웹페이지의 결과표 일부
- PDF의 차트·표·그림
- 공식 영상의 경기 프레임
- 앱·서비스 화면
- 기사 제목과 핵심 도표의 제한적 인용 캡처

규칙:

- 실제 페이지나 영상에서 직접 캡처한다.
- URL, 페이지 제목, 캡처 날짜, PDF 페이지, 영상 시간코드를 기록한다.
- 데이터나 문구를 수정·합성하지 않는다.
- 관련 영역만 잘라 사용할 수 있지만 맥락을 오해하게 만들 정도로 과도하게 자르지 않는다.
- 개인정보, 계정 정보, 알림, 전화번호 등은 제거하거나 가린다.
- 유료 장벽을 우회하거나 기사 전체를 복제하지 않는다.
- 캡처가 너무 작으면 사용하지 않는다.

origin 값:

- `official-screenshot`
- `pdf-capture`
- `video-frame`
- `app-capture`

### Tier 4 — 실제 데이터 기반 그래프·표

원문에 숫자·기록·변화량·순위·기간 데이터가 있으면 사진 대신 그래프나 표를 만든다.

허용 그래프:

- 가로 막대
- 세로 막대
- 선 그래프
- slope chart
- 기록 변화 타임라인
- 순위·기록 ladder
- 구간 페이스 비교
- 전후 비교

강제 규칙:

- 원문·CSV·공식 결과의 실제 값만 사용한다.
- 숫자를 추정하거나 보기 좋게 만들기 위해 바꾸지 않는다.
- 축, 단위, 기간, 기준을 표시한다.
- 3D 그래프와 장식형 원형 차트 남발을 피한다.
- 한 장에 그래프 메시지는 1개가 기본이다.
- 그래프 출처를 페이지 또는 `IMAGE_SOURCES.md`에 기록한다.
- 숫자 근거가 없는 정성적 내용을 가짜 수치 그래프로 만들지 않는다.

origin 값:

- `generated-chart`
- `generated-table`

### Tier 5 — 원문 기반 도식·타임라인·지도·프로세스

숫자보다 구조가 중요한 내용은 다음으로 표현한다.

- 타임라인
- 단계 흐름도
- 훈련 주기
- 레이스 전술 경로
- 선수 간 비교 구조
- 원인→적응→결과 도식
- 트랙/코스 선형 다이어그램
- 간단한 해부·생리 개념도

강제 규칙:

- 원문에 없는 인과관계를 새로 만들지 않는다.
- 아이콘은 의미 전달에 필요한 수만 사용한다.
- 선, 화살표, 수치, 캡션은 코드로 조판한다.
- 실제 지도 정확도가 필요한 경우 공식 지도 또는 좌표 기반 지도를 사용한다.

origin 값:

- `generated-diagram`
- `generated-timeline`
- `generated-map`

### Tier 6 — 낮은 불쾌감의 보조 생성 이미지

실제 사진·캡처·데이터 시각화·도식으로도 적절한 화면을 만들 수 없을 때만 사용한다.

허용 용도:

- 작은 선형 아이콘
- 단순한 스포츠 동작 실루엣
- 친근한 2D 캐릭터
- 건강·회복·훈련 개념을 설명하는 평면 일러스트
- 배경용 추상 패턴
- 사진이 아닌 개념 설명용 보조 그림

시각 쾌적성 프로필:

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

- 실제 선수의 가짜 경기 사진 또는 가짜 수상 장면
- 실제 인물과 혼동될 포토리얼 합성
- 기괴한 얼굴, 손가락, 신체 왜곡
- 부상 부위 클로즈업, 피, 주사, 수술, 체액
- 과도한 근육·통증 표정·공포 연출
- 성적 대상화
- 저작권 캐릭터·브랜드 로고 모방
- 생성 이미지 내부에 긴 한국어 본문·표·페이지 번호를 넣는 것

생성형 보조 자산은 페이지 전체가 아니라 **별도 에셋**으로 만든 뒤 결정론적 렌더러에 삽입한다.

사용자가 `이미지 생성 기능 쓰지 말고`라고 지시하면 Tier 6은 완전히 비활성화한다.

origin 값:

- `generated-icon`
- `generated-character`
- `generated-illustration`
- `generated-pattern`

### Tier 7 — 타이포그래피 중심 해결

시각물이 꼭 필요하지 않으면 사진을 억지로 채우지 않는다.

- source-highlight
- 대형 기록 숫자
- 문장 인용
- 타임 코드
- 핵심 단어 대비
- 번호형 리스트

원문에 근거한 내용만 사용하고 본문과 중복 기록하지 않는다.

---

## 5. 콘텐츠 유형별 자동 선택

```text
실제 인물·경기·제품 → 실제 사진 우선
공식 결과·발표·문서 → 실제 캡처 우선
숫자·순위·변화 → 그래프 또는 표
시간 순서·과정 → 타임라인 또는 흐름도
복잡한 개념 → 도식·아이콘
가벼운 분위기·초보 설명 → 낮은 불쾌감의 2D 캐릭터
적절한 시각물 없음 → 큰 타이포그래피와 source-highlight
```

한 페이지에 여러 대체 수단을 무조건 섞지 않는다. 가장 강한 메시지 하나를 선택한다.

---

## 6. 새 페이지 타입

### `chart-report`

- 제목 + 한 개의 핵심 그래프 + 짧은 해석
- 그래프는 코드로 생성
- 축·단위·기간·출처 필수

### `evidence-capture`

- 실제 캡처 + 캡처 출처 + 설명
- 원본 맥락이 식별될 정도의 주변 정보를 남긴다.

### `diagram-explainer`

- 원문 기반 흐름도·타임라인·트랙·훈련 구조
- 사진 없이도 사용 가능

### `icon-grid`

- 2~4개의 단순 아이콘 + 짧은 설명
- 장식용 6개 이상 아이콘 남발 금지

### `character-explainer`

- 친근한 2D 캐릭터 또는 스포츠 실루엣 + 짧은 설명
- 실제 인물 대체나 사실 증명 용도로 사용하지 않는다.

---

## 7. asset-map 확장 스키마

```json
{
  "id": "asset-12",
  "local_path": "assets/asset-12.png",
  "origin": "official-screenshot",
  "media_type": "screenshot",
  "sha256": "...",
  "perceptual_hash": "...",
  "source_url": "https://...",
  "source_title": "Official results",
  "author": "...",
  "license": "...",
  "capture_date": "2026-08-28",
  "page_number": null,
  "video_timestamp": null,
  "generated_from_data": null,
  "transformations": ["crop-relevant-region", "blur-private-data"],
  "used_on": [8]
}
```

지원 origin:

```text
user-upload
downloaded-original
official-screenshot
pdf-capture
video-frame
app-capture
generated-chart
generated-table
generated-diagram
generated-timeline
generated-map
generated-icon
generated-character
generated-illustration
generated-pattern
```

---

## 8. 필수 로그 파일

기본 산출물에 다음을 추가한다.

### `ASSET_AUDIT.md`

- 업로드 파일 목록
- 형식·크기·비율·품질
- 중복 검사
- 권리 상태
- 사용 가능/제외 사유

### `VISUAL_FALLBACK_LOG.md`

- 어느 페이지에서 이미지가 부족했는지
- 어떤 Tier를 사용했는지
- 왜 그 방식이 적절했는지
- 생성형 보조 자산 사용 여부
- 사용자 금지 조건 적용 여부

---

## 9. 완료 실패 조건

다음은 실패다.

- 지원하지 않는 파일을 변환 확인 없이 사용
- 저해상도 사진을 무리하게 전면 확대
- 이미지가 부족하다는 이유로 같은 사진을 반복
- 출처 없는 웹 캡처 사용
- 캡처의 수치·문구 변조
- 실제 데이터가 없는 가짜 그래프
- 표를 장식 이미지처럼 사용
- 생성형 보조 이미지를 실제 사건의 증거처럼 제시
- 불쾌감·공포·신체 왜곡이 큰 캐릭터나 아이콘 사용
- 생성 이미지 안에 한국어 장문·표를 직접 생성
- 사용자가 생성 기능을 금지했는데 generated-* origin 자산 사용
- ASSET_AUDIT.md 또는 VISUAL_FALLBACK_LOG.md 누락
