# Production Workflow — 입력부터 20장 ZIP 전달까지

이 문서는 다장 캐러셀을 실제 파일로 만드는 표준 공정이다. 기획 설명으로 끝내지 않고 산출물을 생성하는 데 목적이 있다.

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
  IMAGE_SOURCES.md
  QA_REPORT.md
output/<slug>.zip
output/<slug>_preview.jpg
output/<slug>_preview.png
```

## 2. 원문 잠금

1. 사용자가 준 원문을 그대로 `source.txt`에 저장한다.
2. 유니코드 정규화 방식을 하나로 고정한다.
3. 원문의 SHA-256 해시를 기록한다.
4. 이후 조판용 텍스트는 source.txt에서만 가져온다.
5. 채팅의 일부 문장을 기억으로 재입력하지 않는다.

## 3. 페이지 맵

전체 페이지를 처음부터 끝까지 하나의 JSON으로 관리한다.

예시:

```json
{
  "total_pages": 20,
  "pages": [
    {
      "page": 1,
      "type": "cover-photo",
      "source_start": 0,
      "source_end": 57,
      "asset_id": "photo-01"
    }
  ]
}
```

강제 규칙:

- source_start/source_end는 앞에서 뒤로 단조 증가한다.
- 이전 페이지와 겹치거나 빈 구간이 생기면 실패다.
- 11~20장을 나중에 제작해도 같은 page-map.json을 사용한다.
- 페이지 순서를 수정하면 1~20장 전체를 다시 검수한다.

## 4. 이미지 자산 맵

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

- SHA-256이 같으면 완전 중복이다.
- perceptual hash가 가까우면 같은 사진의 리사이즈·재압축 가능성이 있다.
- 장면과 구도가 사실상 같은 근접 중복도 사람이 콘택트시트에서 확인한다.
- 기본적으로 `used_on`은 한 페이지다.

### 온라인 이미지

- 실제 원본 파일을 다운로드한다.
- HTML 페이지 캡처나 검색 썸네일을 원본처럼 쓰지 않는다.
- 다운로드 실패 시 사용 목록에서 제거한다.
- URL, 작가, 라이선스, 다운로드 날짜를 IMAGE_SOURCES.md에 기록한다.

## 5. 페이지 타입 배정

- 표가 있으면 `table`
- 긴 원문만 있으면 `body`
- 사진이 주인공이고 설명이 짧으면 `photo-bottom-panel`
- 가로 사진과 장문이면 `photo-top-report`
- 세로 사진과 짧은 본문이면 `photo-split`
- 두 사진 비교면 `photo-duo`
- 여러 사진을 위아래로 쓰면 `photo-stack`
- 결론과 출처는 `sources`

표 페이지는 사진 타입과 결합하지 않는다.

## 6. 텍스트 수용량 사전 계산

렌더링 전에 각 페이지의 가용 폭·높이와 폰트 메트릭으로 예상 줄 수를 계산한다.

오버플로 해결 순서:

1. 문단을 다음 페이지로 넘긴다.
2. 사진 패널을 승인된 작은 프리셋으로 바꾼다.
3. 1열 본문을 2열 본문으로 바꾼다.
4. 표를 두 장으로 나눈다.
5. 장수 고정과 원문 보존이 충돌하면 렌더링 전에 사용자에게 알린다.

하지 않는 것:

- 본문 폰트 축소
- 자간 과도 축소
- 원문 삭제
- 문장 순서 변경

## 7. 결정론적 렌더링

권장 방식:

- Python + Pillow
- SVG + headless browser
- HTML/CSS + Playwright screenshot

공통 규칙:

- 1080×1350 RGB 또는 sRGB PNG
- 동일 입력이면 동일한 결과가 나오게 한다.
- 폰트 파일은 사용자에게 배포하지 않는다.
- 폰트가 없으면 정해진 fallback 순서를 사용한다.
- 페이지 번호는 2자리 파일명으로 저장한다.

## 8. 사진 렌더링

전경:

- contain 방식
- 원본 비율 유지
- 핵심 피사체 전체 보존

배경:

- 같은 사진을 cover로 확대
- blur + tone down 적용 가능
- 배경은 장식이며 전경을 대체하지 않는다.

텍스트:

- 긴 본문은 사진 위에 직접 올리지 않는다.
- 웜화이트 불투명 패널 또는 충분한 불투명도의 어두운 패널을 사용한다.
- 패널 높이는 small/medium/large 프리셋 중 선택한다.

## 9. 표 렌더링

- 사진 없음
- 웜화이트 단색 배경
- 검정 외곽선과 회색 내부선
- 헤더 굵기 고정
- 셀별 줄바꿈 허용
- 행 높이는 콘텐츠에 맞춰 늘릴 수 있음
- 표 폰트 크기는 전 표 페이지에서 동일

## 10. 텍스트 검수

원문 보존 모드에서 다음을 수행한다.

1. page-map 순서로 페이지 텍스트를 연결한다.
2. 조판용 줄바꿈, 페이지 번호, 푸터를 제거한다.
3. source.txt와 비교한다.
4. 다음 수치를 QA_REPORT.md에 기록한다.

```text
source_chars: N
manifest_chars: N
missing_chars: 0
duplicated_chars: 0
order_mismatch: 0
```

## 11. 시각 검수

- 개별 PNG 100% 확대
- 25% 모바일 축소
- 전체 콘택트시트

확인 항목:

- 폰트 크기와 제목 위치
- 페이지 번호 연속성
- 표 페이지 사진 없음
- 사진 중복 없음
- 얼굴·머리·손·발·핵심 동작 보존
- 텍스트가 패널 밖으로 넘치지 않음
- 빈 공간이 의도적으로 보임

## 12. 패키징

- 01.png~마지막.png를 숫자 순서로 ZIP에 넣는다.
- 검수 파일도 ZIP에 포함한다.
- 콘택트시트를 JPG와 PNG로 만든다.
- ZIP과 미리보기 파일이 실제로 열리는지 확인한다.
- 최종 답변에는 검증된 sandbox 경로만 링크한다.

## 13. 완료 보고 형식

완료 보고는 다음을 포함한다.

- 총 페이지 수
- 렌더링 방식: deterministic file rendering
- 이미지 사용 방식: user-upload 또는 downloaded-original
- 표 페이지 번호
- 중복 이미지 검사 결과
- 원문 누락 검사 결과
- ZIP, preview, manifest, sources, QA 링크

`완료`라고 쓴 뒤 파일이 없거나, 이미지 생성 도구 결과만 나열하는 것은 실패다.
