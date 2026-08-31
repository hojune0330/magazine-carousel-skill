# Production Workflow v3.3 — 텍스트 중심 제작과 공개층 검사

## 1. 작업 폴더

```text
work/<slug>/
  source.txt
  style.json
  page-map.json
  asset-map.json
  public-surface.json
  production-notes.json
  assets/
  build/
```

공개 산출물은 PNG와 미리보기다. 제작 설명은 최종 ZIP의 production/에 둔다. 제작 문서에 있는 설명을 헤더·푸터로 다시 복사하지 않는다.

## 2. 입력 잠금

현재 지시가 가리키는 원문과 실제 승인 스타일을 확인한다. 원문 전체를 source.txt로 바이트 보존하고 해시·선택 이유를 production 문서에 기록한다. 처음 보고서가 요구되면 예전 요약 매니페스트를 사용하지 않는다.

## 3. 노출층 분리

모든 텍스트는 public / production / internal로 분류한다. public은 허용 role과 provenance를 가진다. 원문에 있는 연구 설명은 그대로 유지하고 렌더러가 추가한 제작 상태·파일 안내만 공개층에서 뺀다.

## 4. 전체 본문 우선 조판

26/39 기본 또는 실제 승인 스타일로 전 장을 잠근다. 원문 제목·본문·표·각주부터 1~마지막 장까지 배치한다. source_ranges와 실제 렌더 텍스트를 연결한다. 보조 시각물이 없더라도 먼저 원문 완전성을 확보한다.

## 5. 이미지 조사·감사·배치

references/image-research-and-placement.md의 절차를 따른다. 실제 파일 확보, 출처·권리, 촬영 맥락, 중복·해상도를 확인한다. 사진은 전경 무크롭, 기본 1회, 표 페이지 0개다.

관련 사진을 넣을 공간이 없으면 사진을 빼고 본문을 유지한다. 새 그래프·도식은 본문을 대체하지 않는다. 선택/제외 이유와 검색 기록은 production/internal 문서에 둔다.

## 6. 재균형

Pass 1 전체 원문 분할 → Pass 2 인접 문단 재균형 → 보조 이미지 배정 → 원문·노출층 재검사.

장별 글자 크기 축소, 말줄임표, max-lines, 숨김 오버플로를 사용하지 않는다. 의도적인 여백은 기록하고 허용할 수 있다. 빈 공간을 없애기 위해 원문을 반복하거나 무관한 이미지를 넣지 않는다.

## 7. 렌더링 전 공개 문구 검사

public-surface.json은 `{pages: [{page, text_nodes: [...]}]}` 형식이다. 모든 text node는 id, audience, role, provenance, text를 가진다.

```bash
python scripts/lint_public_surface.py work/<slug>/public-surface.json --report work/<slug>/build/PUBLIC_PREFLIGHT.json
```

실패하면 제작자가 추가한 메타정보를 production 층으로 옮긴다. 원문에 있는 실제 연구 표현은 삭제하지 말고 맥락 검토와 승인 예외를 기록한다.

## 8. 결정론적 렌더링

Python/Pillow, HTML/CSS, SVG 등으로 요청 전체 장수를 생성한다. 렌더링 함수에 public만 전달한다. 헤더·푸터·표 셀·그래프 레이블·캡션 등 실제 draw call마다 text node를 render-surface.json에 기록한다.

렌더러가 임의로 `FULL TEXT`, `원문 파일 수록`, 버전·QA 라벨을 붙이지 않는다. HTML 가상 요소와 이미지 자체에 들어 있는 제작 문구도 검사 대상이다.

## 9. 렌더링 후 검사

```bash
python scripts/lint_public_surface.py work/<slug>/build/render-surface.json --report work/<slug>/build/PUBLIC_SURFACE_QA.json
```

다음은 별도 검사다.

- 원문 범위·문자·표 셀·순서 대조.
- 지도에는 있으나 실제 그리지 않은 문구 검사.
- 실제 텍스트 경계, 우측·하단 잘림, clipping mask, 사진·도형 가림 검사.
- 각 PNG 100%와 모바일 표시 크기, 전체 콘택트시트 검토.

텍스트 노출 검사 통과만으로 전체 디자인 QA 통과라고 하지 않는다. 실행하지 않은 검사는 미실행으로 기록한다.

## 10. 패키징

```text
<slug>/
  01.png ... <last>.png
  preview.jpg
  preview.png
  production/
    source.txt
    style.json
    text-manifest.txt
    page-map.json
    asset-map.json
    render-surface.json
    PUBLIC_SURFACE_QA.json
    ASSET_AUDIT.md
    VISUAL_FALLBACK_LOG.md
    IMAGE_SOURCES.md
    CONTENT_REVIEW_NOTES.md
    QA_REPORT.md
<slug>.zip
```

PNG·ZIP·미리보기의 실제 존재와 열림을 확인한다. 인계 문서에는 상세 제작 설명을 남겨도 된다. 그 설명은 관객용 PNG에 인쇄하지 않는다.

## 11. 기존 산출물 수정

스킬 업데이트는 기존 픽셀을 바꾸지 않는다. 실제 출력 수정 요청은 원문·이미지·스타일을 다시 불러와 별도 버전으로 재렌더링하고 공개 문구·원문·잘림을 다시 검수한다.
