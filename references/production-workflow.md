# Production Workflow — 입력부터 20장 ZIP 전달까지

이 문서는 다장 캐러셀을 실제 파일로 만드는 표준 공정이다. 기획 설명으로 끝내지 않고 산출물을 생성하는 데 목적이 있다.

현재 기본 조판 방식은 **큰 본문 + 텍스트 실측형 레이어 + 2-pass 페이지 재균형**이다.

이미지 입력·자산 부족·캡처·그래프·도식·보조 생성 이미지가 포함되면 다음 문서를 추가로 읽는다.

- `asset-intake-and-visual-fallback.md`
- `asset-production-extension.md`

해당 문서와 이 문서가 충돌하면 v3.2 asset 문서가 우선한다.

## 1. 작업 폴더

```text
work/<slug>/
  source.txt
  style.json
  page-map.json
  asset-map.json
  assets/
  build/
```

최종 결과:

```text
output/<slug>/
  01.png
  02.png
  ...
  20.png
  source.txt
  text-manifest.txt
  page-map.json
  asset-map.json
  ASSET_AUDIT.md
  VISUAL_FALLBACK_LOG.md
  IMAGE_SOURCES.md
  QA_REPORT.md
output/<slug>.zip
output/<slug>_preview.jpg
output/<slug>_preview.png
```

## 2. 원문 잠금

1. 사용자 원문을 그대로 `source.txt`에 저장한다.
2. 유니코드 정규화 방식을 하나로 고정한다.
3. 원문 SHA-256을 기록한다.
4. 조판용 텍스트는 source.txt에서만 가져온다.
5. 채팅 일부를 기억으로 재입력하지 않는다.

## 3. 스타일 프리셋 선택

렌더링 전에 데크 전체 프리셋을 하나 선택한다.

### 기본

`reading-large`

```yaml
body: 23/35
caption: 18/27
table: 15/22
reference: 11/16
```

### 장문 원문 + 고정 장수

`source-dense-large`

```yaml
body: 21/32
caption: 17/25
table: 14/20
reference: 11/16
```

- 장마다 프리셋을 바꾸지 않는다.
- 오버플로를 이유로 특정 장만 축소하지 않는다.
- 일반 본문은 20px 미만으로 내려가지 않는다.

## 4. 페이지 맵

전체 페이지를 처음부터 끝까지 하나의 JSON으로 관리한다.

```json
{
  "total_pages": 20,
  "typography_preset": "source-dense-large",
  "pages": [
    {
      "page": 1,
      "type": "cover-photo",
      "source_start": 0,
      "source_end": 57,
      "asset_id": "photo-01",
      "expected_text_height": 410,
      "panel_bounds": [70, 760, 940, 430]
    }
  ]
}
```

강제 규칙:

- source_start/source_end는 단조 증가한다.
- 이전 페이지와 겹치거나 빈 구간이 생기면 실패다.
- 11~20장을 나중에 제작해도 같은 page-map.json을 사용한다.
- 페이지 순서를 수정하면 1~20장 전체를 다시 검수한다.

## 5. 이미지 자산 맵

각 이미지에 고유 ID를 붙인다.

```json
{
  "id": "photo-01",
  "local_path": "assets/photo-01.jpg",
  "sha256": "...",
  "perceptual_hash": "...",
  "origin": "user-upload",
  "source_url": null,
  "author": null,
  "license": null,
  "used_on": [2]
}
```

### 중복 검사

- SHA-256이 같으면 완전 중복
- perceptual hash가 가까우면 리사이즈·재압축 가능성
- 근접 중복은 콘택트시트에서 수동 확인
- 기본적으로 used_on은 한 페이지

### 온라인 이미지

- 실제 원본 파일을 다운로드한다.
- HTML 캡처나 검색 썸네일을 원본처럼 쓰지 않는다.
- 다운로드 실패 시 사용 목록에서 제거한다.
- URL, 작가, 라이선스, 다운로드 날짜를 IMAGE_SOURCES.md에 기록한다.

### v3.2 자산 감사·보완

페이지 맵 작성 전 다음을 수행한다.

1. 업로드 형식·해상도·비율·색공간·방향을 정규화한다.
2. 완전 중복·근접 중복을 검사한다.
3. 페이지를 photo-required/preferred/optional/forbidden으로 분류한다.
4. 자산 부족 페이지를 탐지한다.
5. 실제 이미지→실제 캡처→실제 데이터 그래프·표→도식→저불쾌감 보조 에셋→타이포그래피 순으로 보완한다.
6. 결과를 ASSET_AUDIT.md와 VISUAL_FALLBACK_LOG.md에 기록한다.

상세 절차는 `asset-production-extension.md`를 따른다.

## 6. 페이지 타입 배정

- 표가 있으면 `table-balanced`
- 긴 원문만 있으면 `body-balanced`
- 사진이 주인공이고 설명이 짧으면 `photo-bottom-panel`
- 가로 사진과 장문이면 `photo-top-report`
- 세로 사진과 짧은 본문이면 `photo-split`
- 두 사진 비교면 `photo-duo`
- 여러 사진의 시간·선수 전개면 `photo-stack`
- 원문 문장·수치 강조면 `source-highlight`
- 실제 데이터 그래프면 `chart-report`
- 실제 웹/PDF/영상/앱 캡처면 `evidence-capture`
- 타임라인·흐름도·훈련 구조면 `diagram-explainer`
- 2~4개 개념 아이콘이면 `icon-grid`
- 친근한 2D 보조 설명이면 `character-explainer`
- 결론과 출처는 `sources`

표 페이지는 사진 타입과 결합하지 않는다.

## 7. 텍스트 실측

페이지 타입을 최종 확정하기 전에 실제 폰트 메트릭으로 텍스트를 조판한다.

측정 순서:

1. 제목 줄바꿈과 높이
2. 본문 줄바꿈과 높이
3. 도입·참고·각주 높이
4. 표 셀·그래프 레이블 줄바꿈과 높이
5. 푸터 안전 영역

패널 계산:

```text
required_panel_height
= top_padding
+ title_height
+ gap
+ body_height
+ bottom_padding
```

- 8px 그리드로 반올림한다.
- panel min 330px, max 930px
- 패널에 맞추려고 폰트를 줄이지 않는다.

## 8. 2-pass 페이지 재균형

### Pass 1 — 용량 분할

고정 폰트와 페이지 타입으로 원문을 순서대로 배치한다.

### Pass 2 — 인접 페이지 균형

각 페이지의 vertical fill과 panel utilization을 계산한다.

목표:

```yaml
vertical_fill: 0.86~0.97
panel_utilization: 0.72~0.92
table_vertical_fill: 0.72~0.92
```

underfill 해결:

1. 패널 축소
2. 사진·그래프·도식 확대
3. 다음 페이지의 완전한 문장·문단을 앞당김
4. photo-duo/photo-stack 전환
5. source-highlight 사용
6. 1열/2열 전환
7. body-balanced 전환

overfill 해결:

1. 시각물 면적 축소
2. 마지막 완전한 문장·문단을 다음 장으로 이동
3. 1열→2열 전환
4. 표·그래프 분할
5. body-balanced 전환

규칙:

- 문장·문단 순서 유지
- 제목 뒤 최소 2줄 본문 유지
- 문단 첫 줄/마지막 한 줄 고립 금지
- 표 행 분리 금지

## 9. 빈 공간 검사

다음은 재조판 대상이다.

- 140px 이상 연속된 빈 세로 띠
- usable height의 10% 이상 무의미한 빈 영역
- 본문 종료 후 푸터까지 180px 이상 공백
- panel utilization 0.65 미만 또는 0.96 초과

표지·챕터 오프닝의 의도적 여백만 예외다.

## 10. 결정론적 렌더링

권장 방식:

- Python + Pillow
- SVG + headless browser
- HTML/CSS + Playwright screenshot

공통 규칙:

- 1080×1350 sRGB PNG
- 동일 입력이면 동일 결과
- 폰트 파일은 사용자에게 배포하지 않는다.
- 정해진 fallback 순서 사용
- 페이지 번호는 2자리 파일명
- 보조 생성 자산이 있더라도 최종 페이지 조판은 코드로 수행

## 11. 사진 렌더링

전경:

- contain
- 원본 비율 유지
- 핵심 피사체 전체 보존

배경:

- 같은 사진 cover 확대
- blur + tone down 가능
- 배경은 전경을 대체하지 않는다.

텍스트:

- 긴 본문은 사진 위에 직접 올리지 않는다.
- 웜화이트 또는 충분한 불투명도의 어두운 패널
- 패널 높이는 텍스트 실측값으로 계산

## 12. 표·그래프·캡처 렌더링

표:

- 사진 없음
- 웜화이트 단색 배경
- 검정 외곽선과 회색 내부선
- 헤더 굵기 고정
- 행 높이 64~118px
- 표 폰트 전 장 동일

그래프:

- 실제 값만 사용
- 축·단위·기간·기준·출처 표시
- 레이블은 코드로 조판
- 3D 그래프 금지

캡처:

- 실제 페이지·PDF·영상·앱에서 직접 획득
- URL·날짜·페이지·시간코드 기록
- 개인정보 마스킹
- 데이터 변조 금지

## 13. 텍스트 검수

원문 보존 모드에서:

```text
source_chars: N
manifest_chars: N
missing_chars: 0
duplicated_chars: 0
order_mismatch: 0
offset_gaps: 0
offset_overlaps: 0
```

## 14. 시각 검수

- 개별 PNG 100%
- 모바일 25%
- 전체 콘택트시트

확인:

- 본문 크기와 줄간격
- 페이지 번호·제목·푸터
- 표 페이지 사진 없음
- 사진 중복 없음
- 핵심 피사체 보존
- 캡처 출처·개인정보
- 그래프 수치·축·단위·출처
- 생성 보조 자산의 낮은 불쾌감
- 빈 공간·패널 활용률

## 15. 패키징

- PNG를 숫자 순서로 ZIP에 넣는다.
- 검수 파일 포함
- 콘택트시트 JPG/PNG 생성
- ZIP과 미리보기 실제 열림 확인
- 검증된 sandbox 경로만 링크

## 16. 완료 보고

포함 항목:

- 총 페이지 수
- deterministic file rendering 사용
- typography preset
- 이미지·캡처·그래프·도식 origin
- 표 페이지 번호
- 자산 부족 페이지와 fallback tier
- 이미지 중복 검사
- 원문 누락 검사
- 빈 공간·패널 활용률 검사
- ZIP, preview, manifest, asset audit, visual fallback log, sources, QA 링크

`완료`라고 쓴 뒤 파일이 없거나 생성형 이미지 결과만 나열하는 것은 실패다.
