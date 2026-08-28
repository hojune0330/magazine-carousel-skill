---
name: io-magazine-report-carousel
description: Produce Korean Instagram 4:5 report carousels as deterministic files with large readable body text, text-first adaptive composition, multi-format asset intake, and an evidence-first visual fallback ladder. When the user says 스킬대로, 파일로, 렌더링해서, 20장 전체, PNG/ZIP, or asks to continue a deck, render the full requested page count in one production run. Do not use image generation for Korean text or page layout, do not apply a 10-image limit, preserve source order and exact text when requested, keep tables photo-free, normalize uploaded assets, audit duplicates and quality, and when images are insufficient choose real originals, factual captures, data-backed charts/tables, diagrams, or very-low-discomfort auxiliary icons/characters in that order. Deliver PNGs, ZIP, previews, manifests, maps, asset audit, visual fallback log, image credits, and QA.
version: 3.2
status: active
---

# IO MAGAZINE REPORT CAROUSEL SKILL v3.2

인스타그램 4:5 세로형 카드뉴스를 **파일 렌더링 방식**으로 제작한다. 이 스킬은 생성형 포스터가 아니라 여러 장의 원문·사진·표·그래프·캡처·도식을 정확한 순서로 조판하여 PNG 묶음으로 내보내는 제작 시스템이다.

현재 공식 프로필은 **`report-carousel-v3.2-large-type-adaptive-assets`**다.

- 제작 방식: Python/Pillow, SVG, HTML/CSS canvas 등 결정론적 렌더링
- 타이포그래피: 큰 모바일 가독성 우선 본문
- 레이아웃: 텍스트를 먼저 실측하고 사진·패널·표·그래프를 텍스트에 맞춤
- 이미지 입력: JPG·PNG·WebP·HEIC·SVG·PDF·ZIP·CSV/XLSX 등 다중 형식 지원
- 자산 부족 대응: 실제 이미지 → 실제 캡처 → 실제 데이터 그래프·표 → 도식 → 저불쾌감 보조 생성 이미지 → 타이포그래피
- 표 구성: 사진 없는 웜화이트 리포트형
- 금지 방식: 생성형 이미지 도구가 한국어 장문·표·페이지 번호·전체 레이아웃을 직접 그리는 방식

---

## 0. 요청을 찰떡같이 해석하는 최우선 규칙

다음 표현이 하나라도 있으면 **파일 렌더링 모드**로 즉시 고정한다.

- `스킬대로 만들어`
- `파일로 만들어`
- `렌더링해서 만들어`
- `20장 전체 만들어`
- `PNG와 ZIP으로`
- `캐러셀 전체 제작`
- `앞 장에 이어서 만들어`
- `이미지 생성 기능 쓰지 말고`

이 모드에서는:

1. 최종 페이지 레이아웃과 한국어 텍스트에 image_gen을 사용하지 않는다.
2. 10장 생성 제한을 언급하거나 적용하지 않는다.
3. 요청 장수를 한 번에 제작한다.
4. 한국어 텍스트, 표, 그래프 레이블, 페이지 번호, 크레딧은 코드로 조판한다.
5. 파일이 실제로 생성되고 경로가 확인되기 전에는 완료했다고 말하지 않는다.

사용자가 `이미지 만들어`라고만 말해도 다장 캐러셀·원문·표·ZIP 맥락이면 파일 렌더링이 우선이다. 사용자가 명시적으로 `생성형 이미지로`, `그림을 새로 그려`, `한 장 포스터를 생성`이라고 할 때만 전체 이미지 생성 모드를 고려한다.

보조 아이콘·캐릭터·개념 일러스트는 **별도 에셋**으로만 생성할 수 있다. 사용자가 `이미지 생성 기능 쓰지 말고`라고 하면 보조 생성 에셋도 전부 금지한다.

상세 분기 규칙은 `references/request-routing.md`를 따른다.

---

## 1. 절대 규칙

1. 다장 카드뉴스의 기본은 결정론적 파일 렌더링이다.
2. 같은 역할의 텍스트는 전 장에서 폰트·크기·굵기·줄간격을 고정한다.
3. 일반 본문은 20px 미만으로 내려가지 않는다.
4. 폰트를 레이어에 맞추지 않는다. 사진·패널·표·그래프 레이어를 텍스트 실측값에 맞춘다.
5. 오버플로는 페이지 경계 재조정, 사진 영역 축소, 1열/2열 변경, 표 분할로 해결한다. 특정 장만 글자를 줄이지 않는다.
6. 사용자가 원문 전체 유지 또는 누락 금지를 지시하면 원문 보존 모드를 강제한다.
7. 원문 보존 모드에서는 문자·숫자·괄호·각주·URL·표 셀·문장 순서를 수정, 요약, 교정하지 않는다.
8. 표 페이지에는 사진을 넣지 않는다.
9. 실제 사진 전경은 원본 비율을 유지하고 크롭하지 않는다. 배경 채움만 blur/cover 크롭을 허용한다.
10. 사용자가 전달한 사진은 실제 업로드 파일을 사용한다. 비슷한 이미지를 생성형 도구로 재현하지 않는다.
11. 사진 중복을 피한다. 동일 파일, 다른 파일명의 같은 사진, 근접 중복을 검사한다.
12. 온라인 사진은 실제 원본을 다운로드한 뒤에만 사용한다. 다운로드하지 못했으면 사용했다고 주장하지 않는다.
13. 이미지가 부족하면 의미 없는 장식을 넣지 않고 `asset-intake-and-visual-fallback.md`의 근거 중심 대체 순서를 따른다.
14. 실제 수치가 없는 가짜 그래프를 만들지 않는다.
15. 실제 화면·문서·영상 캡처는 출처, 페이지, 시간코드, 캡처 날짜를 기록한다.
16. 보조 생성 이미지는 매우 낮은 불쾌감의 건강하고 친근한 2D 아이콘·캐릭터·개념 일러스트로 제한한다.
17. 생성형 보조 이미지를 실제 사건·선수·경기 사진의 증거처럼 제시하지 않는다.
18. 모든 자산의 origin, 파일 해시, 출처, 사용 페이지를 `asset-map.json`에 기록한다.
19. 최종 완료 전 개별 PNG, 콘택트시트, 텍스트 매니페스트, 페이지 순서, 이미지 중복, 빈 공간, 자산 출처, 대체 시각물 근거를 검수한다.

---

## 2. 반드시 읽을 문서

- `references/request-routing.md` — 사용자 표현 해석
- `references/production-workflow.md` — 입력부터 ZIP 전달까지 전체 공정
- `references/report-carousel-v3.md` — 캔버스, 타이포그래피, 페이지 타입
- `references/adaptive-density.md` — 큰 본문, 동적 패널, 빈 공간 재균형
- `references/asset-intake-and-visual-fallback.md` — 업로드 형식, 자산 감사, 이미지 부족 대응
- `references/copy-guard.md` — 원문 무삭제와 연속성 검수
- `references/qa-checklist.md` — 완료 판정 기준

충돌 시 우선순위:

1. 사용자의 현재 명시적 지시
2. `SKILL.md` 절대 규칙
3. `asset-intake-and-visual-fallback.md`
4. `adaptive-density.md`
5. `request-routing.md`
6. `production-workflow.md`
7. `report-carousel-v3.md`
8. 나머지 문서

---

## 3. 작업 모드

### A. 원문 보존 모드

- 원문을 `source.txt`로 잠근다.
- 페이지별 텍스트는 원문 앞에서 뒤로 연속해서 나눈다.
- 어떤 장도 이전 장 내용을 다시 시작하지 않는다.
- 10장 이후 11장은 10장 마지막 문자 다음부터 시작한다.
- 표의 열·행·셀 값을 그대로 사용한다.
- 원문 분할로 생긴 줄바꿈만 허용한다.
- `text-manifest.txt`와 source를 비교한다.
- 누락, 중복, 순서 역전, offset gap/overlap이 하나라도 있으면 실패다.

### B. 편집 모드

- 한 장에 하나의 명확한 메시지를 둔다.
- 제목은 결론형, 판단형, 질문형을 우선한다.
- 본문은 짧고 구체적으로 쓴다.
- 숫자, 기록, 비교, 행동 기준을 앞쪽에 둔다.
- 편집 문구와 출처 원문을 별도로 관리한다.

### C. 고정 장수 모드

- 장수를 계약 조건으로 취급한다.
- 먼저 고정 폰트로 텍스트 용량을 계산한다.
- 사진 면적, 문단 열, 표 분할, 페이지 경계를 조정한다.
- 장수를 맞추기 위해 원문을 삭제하거나 글자를 축소하지 않는다.
- 물리적으로 수용할 수 없을 때만 렌더링 전에 충돌을 알린다.

### D. 큰 본문·빈 공간 개선 모드

다음 표현에서 자동 적용한다.

- `본문이 작아`
- `글자를 더 크게`
- `빈 공간이 눈에 띄어`
- `레이어를 텍스트에 맞춰`
- `사진을 더 크게 채워`

적용:

- `reading-large` 또는 `source-dense-large`를 데크 전체에 설정
- 텍스트 bounding box 선측정
- 패널 높이 = 텍스트 높이 + 패딩
- 남은 영역을 사진·그래프·도식에 배분
- 인접 페이지 underfill/overfill 재균형

### E. 자산 부족 자동 보완 모드

다음 표현에서 자동 적용한다.

- `이미지가 부족하면 알아서 채워`
- `사진 없으면 그래프나 표로`
- `실제 화면을 캡처해서 써`
- `아이콘이나 캐릭터로 표현해`
- `중복 없이 구성해`

실행:

1. 업로드 파일 형식·해상도·비율·중복·권리를 감사한다.
2. 사진 필수/선호/선택/금지 페이지를 구분한다.
3. 부족 페이지에 가장 적합한 시각물 Tier를 선택한다.
4. 실제 사진·실제 캡처·실제 데이터 시각화를 생성형 자산보다 우선한다.
5. 사용자가 생성 기능을 금지하지 않았을 때만 마지막 수단으로 저불쾌감 보조 생성 에셋을 사용한다.
6. 선택 근거를 `VISUAL_FALLBACK_LOG.md`에 기록한다.

---

## 4. 큰 본문 타이포그래피

1080×1350 기준:

### `reading-large`

```yaml
main_title: 56/66
section_title: 36/47
subtitle: 30/41
body: 23/35
caption: 18/27
table: 15/22
reference: 11/16
```

### `source-dense-large`

```yaml
main_title: 56/66
section_title: 36/47
subtitle: 30/41
body: 21/32
caption: 17/25
table: 14/20
reference: 11/16
```

- 한 데크는 하나의 프리셋을 사용한다.
- 장마다 프리셋을 바꾸지 않는다.
- 17px 본문을 기본값으로 쓰지 않는다.

---

## 5. 이미지 업로드 형식

권장:

- 사진: JPG/JPEG, PNG, WebP
- 투명 로고·도식: SVG, PNG
- 문서·공식 표: PDF
- 그래프 원본: CSV, XLSX, JSON
- 일괄 업로드: ZIP
- 조건부 변환: HEIC/HEIF, TIFF, BMP, GIF
- 프레임 캡처: MP4, MOV, WebM

권장 해상도:

- 대형 사진 짧은 변 1600px 이상, 이상적 2400px 이상
- 절반 폭 사진 짧은 변 1000px 이상
- 스크린샷 가로 1440px 이상 또는 2× 캡처
- 로고 SVG 또는 1200px 이상 투명 PNG

모든 입력은 sRGB, 실제 방향, 알파 채널, 파일 해시 기준으로 정규화한다.

상세 규칙은 `references/asset-intake-and-visual-fallback.md`를 따른다.

---

## 6. 시각 자산 부족 대응 순서

페이지 성격에 따라 가장 근거가 강한 수단을 선택한다.

### Tier 1 — 사용자 제공 실제 이미지

실제 업로드 파일을 무크롭 전경으로 사용한다.

### Tier 2 — 실제 원본 이미지 추가 다운로드

공식 기관, 사용자 지정 링크, 라이선스가 명확한 원본을 실제로 다운로드한다.

### Tier 3 — 실제 캡처

공식 웹 결과, PDF 차트, 공식 영상 프레임, 앱 화면을 직접 캡처한다. URL·페이지·시간코드·캡처 날짜를 기록한다.

### Tier 4 — 실제 데이터 기반 그래프·표

원문·CSV·공식 결과의 실제 값으로 막대, 선, slope, 기록 타임라인, 순위 ladder 등을 코드 생성한다. 축·단위·기간·출처를 표시한다.

### Tier 5 — 원문 기반 도식·타임라인·프로세스

훈련 구조, 레이스 흐름, 원인→적응→결과, 트랙·코스 구조를 코드로 조판한다.

### Tier 6 — 저불쾌감 보조 생성 에셋

실제 자료와 데이터 시각화로 해결되지 않을 때만 사용한다.

허용:

- 선형 아이콘
- 스포츠 실루엣
- 친근한 2D 캐릭터
- 건강·회복·훈련 개념 일러스트
- 추상 배경 패턴

조건:

- clean flat 2D
- healthy, calm, friendly
- uncanny/discomfort very low
- 폭력, 피, 주사, 수술, 체액, 공포, 신체 왜곡, 성적 대상화 없음
- 실제 선수의 가짜 사진·가짜 경기 장면 금지
- 생성 이미지 내부에 한국어 장문·표·페이지 번호 금지

사용자가 이미지 생성을 금지하면 Tier 6을 사용하지 않는다.

### Tier 7 — 타이포그래피

적절한 시각 근거가 없으면 대형 기록, source-highlight, 번호형 구조로 해결한다. 사진을 억지로 넣지 않는다.

---

## 7. 페이지 타입

- `cover-photo`: 전면 사진 + 제목 패널
- `photo-bottom-panel`: 사진 + 텍스트 실측형 하단 패널
- `photo-top-report`: 상단 사진 + 하단 보고서
- `photo-split`: 세로 사진 + 본문
- `photo-duo`: 두 사진 비교
- `photo-stack`: 2~3장 사진 전개
- `source-highlight`: 원문 구절·수치 대형 강조
- `body-balanced`: 사진 없는 큰 본문
- `table-balanced`: 사진 없는 표
- `chart-report`: 실제 데이터 그래프 + 해석
- `evidence-capture`: 실제 웹/PDF/영상 캡처 + 출처
- `diagram-explainer`: 타임라인·흐름도·트랙·프로세스
- `icon-grid`: 2~4개 의미형 아이콘
- `character-explainer`: 친근한 2D 캐릭터·스포츠 실루엣
- `sources`: 결론과 출처

페이지마다 자유롭게 임의 조판하지 않는다. 승인된 타입 중 하나를 선택한다.

---

## 8. 자산 origin과 기록

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

각 자산에는 다음을 기록한다.

- local path
- SHA-256
- perceptual hash
- origin
- source URL/title
- author/license
- capture date/page/timestamp
- transformations
- used_on

---

## 9. 전체 제작 파이프라인

### 9.1 입력 잠금

```text
source.txt
style.json
page-map.json
asset-map.json
assets/
```

### 9.2 자산 감사

- 형식 지원 여부
- 크기와 비율
- 색공간과 방향
- 중복
- 권리 상태
- 페이지 적합성

결과를 `ASSET_AUDIT.md`에 기록한다.

### 9.3 페이지 맵과 자산 보완

각 페이지에 source offset, page type, asset ID, typography preset, expected text height, fallback tier를 기록한다.

이미지가 부족하면 `VISUAL_FALLBACK_LOG.md`에 페이지별 선택과 근거를 기록한다.

### 9.4 2-pass 페이지 균형

- Pass 1: 고정 폰트 기준 용량 분할
- Pass 2: 인접 페이지 underfill/overfill 재균형

### 9.5 렌더링

- 1080×1350, 4:5
- Python/Pillow, SVG, HTML/CSS canvas 등
- 요청 전체 장수를 한 실행에서 렌더링
- 생성형 보조 에셋이 있어도 최종 페이지 조판은 결정론적 렌더링
- 오버플로, 큰 빈 공간, 자산 근거 부족 시 중단 후 page map 수정

### 9.6 검수와 패키징

검수:

- 원문 누락·중복·순서
- 본문 크기와 패널 활용률
- 표 페이지 사진 0개
- 사진 중복과 피사체 보존
- 캡처 출처와 개인정보
- 그래프 수치·축·단위·출처
- 생성 보조 에셋의 낮은 불쾌감과 사실 오인 가능성

산출물:

```text
<slug>/
  01.png ... 20.png
  source.txt
  text-manifest.txt
  page-map.json
  asset-map.json
  ASSET_AUDIT.md
  VISUAL_FALLBACK_LOG.md
  IMAGE_SOURCES.md
  QA_REPORT.md
<slug>.zip
<slug>_preview.jpg
<slug>_preview.png
```

---

## 10. 온라인 이미지·캡처 정직성

- 검색 링크만 확인하고 파일을 받지 않았다면 사용했다고 말하지 않는다.
- 대화 업로드는 `user-upload`로 기록한다.
- 실제 원본 다운로드만 `downloaded-original`로 기록한다.
- 실제 캡처만 screenshot/capture origin으로 기록한다.
- URL, 제목, 작가, 라이선스, 페이지, 시간코드, 다운로드·캡처 날짜를 남긴다.

---

## 11. 실패 조건

다음 중 하나라도 있으면 완료 처리하지 않는다.

- 다장 파일 제작 요청에 image_gen으로 전체 페이지를 생성했다.
- 파일 렌더링 요청에 10장 제한을 적용했다.
- 생성형 이미지에 한국어 장문·표·페이지 번호를 맡겼다.
- 원문 누락, 중복, 순서 역전이 있다.
- 일반 본문이 20px 미만이다.
- 같은 역할의 폰트가 장마다 다르다.
- 의도하지 않은 큰 빈 공간이 남았다.
- 표 페이지에 사진이 들어갔다.
- 전경 사진 핵심 피사체가 잘렸다.
- 같은 사진이 승인 없이 반복됐다.
- 저해상도 사진을 무리하게 전면 확대했다.
- 출처 없는 웹 캡처를 사용했다.
- 실제 데이터 없는 가짜 그래프를 만들었다.
- 생성형 보조 이미지를 실제 사건의 증거처럼 제시했다.
- 불쾌감·공포·신체 왜곡이 큰 아이콘·캐릭터를 사용했다.
- 사용자가 생성 기능을 금지했는데 generated-* 자산을 사용했다.
- ASSET_AUDIT.md, VISUAL_FALLBACK_LOG.md, IMAGE_SOURCES.md, QA_REPORT.md 중 하나가 빠졌다.
- 실제 파일 경로를 확인하지 않고 완료 보고했다.

---

## 12. 사용자 피드백의 영구 반영

사용자가 `스킬에 넣어`, `다음에도 기억`, `규칙으로 고정`, `스킬 업데이트`라고 말하면:

1. 현재 작업에 즉시 적용한다.
2. `SKILL.md` 또는 reference 문서에 실제 반영한다.
3. GitHub 커밋을 완료한다.
4. 변경 파일과 핵심 변경점을 보고한다.

---

## 공식 선언

**현재 기본 제작 방식은 `report-carousel-v3.2-large-type-adaptive-assets`다.**

**다장 카드뉴스는 이미지 생성이 아니라 파일 렌더링으로 한 번에 제작한다.**

**본문을 먼저 크게 조판하고 사진·패널·표·그래프·캡처 레이어를 텍스트와 정보 근거에 맞춘다.**

**이미지가 부족하면 실제 이미지, 실제 캡처, 실제 데이터 그래프·표, 원문 기반 도식, 저불쾌감 보조 생성 에셋, 타이포그래피 순으로 해결한다.**

**표에는 사진을 사용하지 않고, 실제 사진 전경은 무크롭이며, 원문은 지시된 경우 한 글자도 빠짐없이 유지한다.**
