# IO MAGAZINE Report Carousel Skill

인스타그램 4:5 세로형 카드뉴스를 **생성형 이미지가 아니라 파일 렌더링 방식**으로 제작하는 전용 스킬입니다.

## Active profile

- `report-carousel-v3-render-first`
- 상태: `ACTIVE / v3.0`
- 캔버스: `1080×1350`
- 핵심: 20장 전체를 한 번에 PNG 파일로 렌더링

## 이 스킬이 자동으로 알아듣는 말

아래 표현은 모두 같은 요청으로 처리합니다.

- `스킬대로 파일로 만들어`
- `20장 전체 렌더링해`
- `이미지 생성 기능 쓰지 말고`
- `PNG 20장과 ZIP으로 만들어`
- `앞 10장에 이어서 뒤 10장 만들어`
- `원문 빠짐없이 캐러셀 제작`

이때는:

- image_gen을 사용하지 않습니다.
- 10장 제한을 적용하지 않습니다.
- Python/Pillow, SVG, HTML canvas 등으로 요청한 전체 장수를 렌더링합니다.

## 승인된 제작 규칙

- 보고서형 제목·본문·표·푸터 규격 고정
- 사진 중심 페이지는 실제 사진을 주인공으로 사용
- 전경 사진은 원본 비율 유지, 무크롭 contain
- 빈 공간은 같은 사진의 블러·톤다운 배경으로 채움
- 표 페이지에는 사진 사용 금지
- 같은 사진은 기본적으로 한 번만 사용
- 사용자 제공 사진은 실제 업로드 파일 사용
- 온라인 사진은 실제 원본 다운로드 후 출처·작가·라이선스 기록
- 원문 보존 요청 시 문자·수치·각주·URL·표 셀·순서까지 그대로 유지
- 1~10장과 11~20장의 경계를 하나의 page-map으로 관리

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
- `references/request-routing.md` — 사용자의 짧은 말을 제작 모드로 해석하는 법
- `references/production-workflow.md` — 입력 잠금부터 ZIP 전달까지 전체 공정
- `references/report-carousel-v3.md` — 1080×1350 시각 시스템과 사진·표 슬롯
- `references/copy-guard.md` — 원문 무삭제, 페이지 오프셋, 연속성 검수
- `references/qa-checklist.md` — 최종 완료 판정 기준
- `examples/report-carousel-v3.sample.json` — 페이지 맵 예시

## 핵심 실패 조건

- 파일 렌더링 요청에 image_gen 사용
- 20장 요청에 10장 제한 적용
- 생성형 이미지 안에 한국어 장문·표 생성
- 1~10장과 11~20장 원문 순서 어긋남
- 표 페이지에 사진 배치
- 사진 핵심 피사체 크롭
- 같은 사진의 승인 없는 반복
- 다운로드하지 않은 온라인 사진을 사용했다고 주장
- 실제 파일 없이 완료 보고

## Legacy

- `report-carousel-v2`는 과거 좌표 참고용입니다.
- 현재 실행 기준은 오직 `report-carousel-v3-render-first`입니다.
