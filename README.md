# IO MAGAZINE Report Carousel Skill

인스타그램 4:5 세로형 카드뉴스를 **결정론적 파일 렌더링**으로 제작하는 전용 스킬입니다.

## Active profile

- `report-carousel-v3.1-large-type-adaptive-fill`
- 상태: `ACTIVE / v3.1`
- 캔버스: `1080×1350`
- 핵심: 본문을 크게 조판한 뒤 사진·패널·표 레이어를 텍스트 실측값에 맞춤

## 이 스킬이 자동으로 알아듣는 말

아래 표현은 모두 파일 렌더링 요청입니다.

- `스킬대로 파일로 만들어`
- `20장 전체 렌더링해`
- `이미지 생성 기능 쓰지 말고`
- `PNG 20장과 ZIP으로 만들어`
- `앞 10장에 이어서 뒤 10장 만들어`
- `원문 빠짐없이 캐러셀 제작`

이때는:

- image_gen을 사용하지 않습니다.
- 10장 제한을 적용하지 않습니다.
- Python/Pillow, SVG, HTML/CSS canvas 등으로 요청한 전체 장수를 렌더링합니다.

## 큰 본문·빈 공간 개선 요청

아래 표현은 자동으로 `large-type adaptive-fill` 모드를 켭니다.

- `본문이 작아`
- `원문 글자를 더 크게`
- `빈 공간이 눈에 띄어`
- `공백을 줄여`
- `사진이나 레이어를 텍스트에 맞춰`
- `사진을 더 크게 채워`

적용 방식:

- 텍스트 bounding box를 먼저 측정
- 패널 높이 = 텍스트 높이 + 패딩
- 남은 영역을 사진에 배분
- underfill/overfill 페이지를 인접 페이지와 재균형
- 140px 이상 의도하지 않은 빈 띠는 재조판
- 장별 폰트 축소 금지

## 읽기 프리셋

### `reading-large` — 기본

- body 23 / line-height 35
- caption 18 / 27
- table 15 / 22

### `source-dense-large`

원문 전체 보존 + 고정 장수 + 장문에 사용합니다.

- body 21 / 32
- caption 17 / 25
- table 14 / 20

한 데크 안에서는 한 프리셋만 사용하며, 일반 본문은 20px 미만으로 내리지 않습니다.

## 승인된 제작 규칙

- 보고서형 제목·본문·표·푸터 규격 고정
- 본문을 먼저 크게 조판하고 레이어를 텍스트에 맞춤
- 사진 중심 페이지는 실제 사진을 주인공으로 사용
- 전경 사진은 원본 비율 유지, 무크롭 contain
- 빈 공간은 패널 축소, 사진 확대, 인접 문단 재균형으로 해결
- 표 페이지에는 사진 사용 금지
- 표의 남는 높이는 행 높이와 표 위치로 균형 조정
- 같은 사진은 기본적으로 한 번만 사용
- 사용자 제공 사진은 실제 업로드 파일 사용
- 온라인 사진은 실제 원본 다운로드 후 출처·작가·라이선스 기록
- 원문 보존 요청 시 문자·수치·각주·URL·표 셀·순서 유지
- 1~10장과 11~20장 경계를 하나의 page-map으로 관리

## 기본 산출물

```text
01.png ~ 20.png
<slug>.zip
<slug>_preview.jpg
<slug>_preview.png
source.txt
text-manifest.txt
page-map.json
asset-map.json
IMAGE_SOURCES.md
QA_REPORT.md
```

## 파일 구조

- `SKILL.md` — 최상위 실행 규칙
- `references/request-routing.md` — 짧은 사용자 지시 해석
- `references/production-workflow.md` — 입력 잠금부터 ZIP 전달까지 전체 공정
- `references/report-carousel-v3.md` — 1080×1350 시각 시스템
- `references/adaptive-density.md` — 큰 본문·동적 패널·빈 공간 재균형
- `references/copy-guard.md` — 원문 무삭제와 연속성
- `references/qa-checklist.md` — 최종 완료 판정
- `examples/report-carousel-v3.sample.json` — 페이지 맵 예시

## 핵심 실패 조건

- 파일 렌더링 요청에 image_gen 사용
- 20장 요청에 10장 제한 적용
- 생성형 이미지 안에 한국어 장문·표 생성
- 일반 본문 20px 미만
- 장별 본문 폰트 크기 변경
- 140px 이상 의도하지 않은 빈 띠
- 패널 활용률 0.65 미만 또는 0.96 초과
- 1~10장과 11~20장 원문 순서 어긋남
- 표 페이지에 사진 배치
- 사진 핵심 피사체 크롭
- 같은 사진의 승인 없는 반복
- 실제 파일 없이 완료 보고

## Legacy

- `report-carousel-v2`와 `report-carousel-v3-render-first`는 과거 좌표 참고용입니다.
- 현재 실행 기준은 `report-carousel-v3.1-large-type-adaptive-fill`입니다.
