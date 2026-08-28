# IO MAGAZINE Report Carousel Skill

인스타그램 4:5 세로형 카드뉴스를 **결정론적 파일 렌더링**으로 제작하는 전용 스킬입니다.

## Active profile

- `report-carousel-v3.2-large-type-adaptive-assets`
- 상태: `ACTIVE / v3.2`
- 캔버스: `1080×1350`
- 핵심: 큰 본문을 먼저 조판하고 사진·패널·표·그래프·캡처를 텍스트와 정보 성격에 맞춤

## 자동 해석

아래 표현은 모두 파일 렌더링 요청입니다.

- `스킬대로 파일로 만들어`
- `20장 전체 렌더링해`
- `이미지 생성 기능 쓰지 말고`
- `PNG와 ZIP으로 만들어`
- `앞 장에 이어서 만들어`
- `원문 빠짐없이 제작`

이때는 전체 장수를 한 실행에서 PNG로 렌더링하며 10장 생성 제한을 적용하지 않습니다.

## 지원 업로드 형식

- 사진: JPG/JPEG, PNG, WebP
- 변환 후 사용: HEIC/HEIF, TIFF, BMP, GIF
- 벡터·문서: SVG, PDF, PPTX, DOCX
- 데이터: CSV, XLSX, JSON
- 영상 프레임: MP4, MOV, WebM
- 일괄 업로드: ZIP

이미지는 sRGB, 실제 방향, 알파 채널, 파일 해시 기준으로 정규화하고 `ASSET_AUDIT.md`에 기록합니다.

## 이미지가 부족할 때

페이지 내용에 따라 다음 순서로 채웁니다.

1. 사용자 제공 실제 이미지
2. 실제 원본 이미지 추가 다운로드
3. 공식 웹·PDF·영상·앱의 실제 캡처
4. 실제 데이터 기반 그래프·표
5. 원문 기반 도식·타임라인·프로세스
6. 매우 낮은 불쾌감의 2D 아이콘·캐릭터·개념 일러스트
7. 대형 기록·source-highlight 등 타이포그래피

숫자 근거가 없는 가짜 그래프, 출처 없는 캡처, 실제 선수의 가짜 경기 사진은 사용하지 않습니다.

사용자가 `이미지 생성 기능 쓰지 말고`라고 하면 6번 보조 생성 자산도 비활성화합니다.

## 보조 생성 이미지의 시각 기준

- clean flat 2D
- healthy, calm, friendly
- uncanny/discomfort very low
- 폭력, 피, 주사, 수술, 체액, 공포, 신체 왜곡, 성적 대상화 없음
- 실제 선수·경기·수상 장면의 포토리얼 재현 금지
- 생성 이미지 내부의 긴 한국어 본문·표·페이지 번호 금지

보조 에셋만 생성할 수 있으며 최종 페이지는 항상 코드로 렌더링합니다.

## 큰 본문·빈 공간 개선

- `reading-large`: body 23/35, table 15/22
- `source-dense-large`: body 21/32, table 14/20
- 본문 20px 미만 금지
- 텍스트 bounding box 선측정
- 패널 높이 = 텍스트 높이 + 패딩
- 남은 영역을 사진·그래프·도식에 배분
- underfill/overfill 인접 페이지 재균형

## 승인된 제작 규칙

- 표 페이지에는 사진 사용 금지
- 실제 사진 전경은 무크롭 contain
- 같은 사진은 기본 1회 사용
- 사용자 제공 이미지는 실제 업로드 파일 사용
- 온라인 이미지는 실제 원본 다운로드 후 출처·작가·라이선스 기록
- 실제 캡처는 URL·페이지·시간코드·캡처 날짜 기록
- 그래프는 실제 원문·CSV·공식 결과의 값만 사용
- 원문 보존 요청 시 문자·수치·각주·URL·표 셀·순서 유지
- 전체 페이지 경계를 하나의 page-map으로 관리

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
ASSET_AUDIT.md
VISUAL_FALLBACK_LOG.md
IMAGE_SOURCES.md
QA_REPORT.md
```

## 파일 구조

- `SKILL.md` — 최상위 실행 규칙
- `references/request-routing.md` — 짧은 사용자 지시 해석
- `references/production-workflow.md` — 입력부터 ZIP 전달까지 공정
- `references/report-carousel-v3.md` — 시각 시스템과 페이지 타입
- `references/adaptive-density.md` — 큰 본문·동적 패널·빈 공간 재균형
- `references/asset-intake-and-visual-fallback.md` — 업로드 형식·자산 감사·시각 대체 순서
- `references/copy-guard.md` — 원문 무삭제와 연속성
- `references/qa-checklist.md` — 완료 판정

## 핵심 실패 조건

- 다장 요청에 생성형 이미지로 전체 페이지 제작
- 파일 렌더링 요청에 10장 제한 적용
- 일반 본문 20px 미만
- 표 페이지에 사진 배치
- 사진 핵심 피사체 크롭
- 같은 사진의 승인 없는 반복
- 저해상도 사진의 무리한 전면 확대
- 출처 없는 캡처
- 실제 데이터가 없는 가짜 그래프
- 불쾌감·왜곡이 큰 캐릭터 사용
- 사용자가 생성을 금지했는데 generated-* 자산 사용
- 실제 파일 없이 완료 보고

## Legacy

- v2와 v3.0~v3.1은 과거 기준 참고용입니다.
- 현재 실행 기준은 `report-carousel-v3.2-large-type-adaptive-assets`입니다.
