# Audience Content Boundary — 슬라이드에 무엇을 보여줄 것인가

## 1. 고칠 대상

사용자 피드백은 **실제 PNG 안의 위쪽 `풀 텍스트`, 아래쪽 `원문은 파일에 수록` 문구**다. 결과 안내문을 짧게 하라는 요청으로 오해하지 않는다.

보고서·첨부 문서에는 이런 제작 설명이 있어도 된다. 콘텐츠를 보는 독자의 화면에는 보여주지 않는다.

## 2. 3층 모델

| audience | 들어갈 내용 | 실제 슬라이드 렌더링 |
|---|---|---|
| public | 독자용 제목, 부제, 본문, 표, 그래프 라벨, 내용 캡션, 필요한 출처·권리, 승인 브랜드·페이지 번호 | 허용 |
| production | 원문 포함 여부, 파일 위치, 제작 방식, 수정 내역, 검수 결과, 인계 설명 | 금지 |
| internal | 해시, 원문 오프셋, 렌더 로그, 후보 탈락 사유, 폰트 측정, 오류 | 금지 |

데이터의 보관 여부와 픽셀 노출 여부를 별개로 결정한다. 보고서를 지우거나 작업 기록을 숨길 필요는 없다.

## 3. 렌더링 계약

최종 텍스트 노드는 최소 `id`, `audience`, `role`, `provenance`, `text`를 가진다.

- `audience=public`이고 승인된 role인 노드만 그린다.
- audience 누락·오류는 렌더링 오류다. public으로 추정하지 않는다.
- provenance는 source / approved-editorial / citation / brand 중 하나다. renderer-metadata는 공개층에 넣지 않는다.
- 내부 딕셔너리 전체를 문자열로 바꾸어 그리지 않는다.
- 본문뿐 아니라 헤더·푸터·사진 캡션·표 셀·범례·CSS 가상 요소까지 동일 규칙을 적용한다.
- 고정 템플릿에 `FULL TEXT`, 파일 안내 꼬리표, `v3.3`, 검수 상태가 하드코딩돼 있지 않은지 확인한다.
- 읽는 사람에게 무관한 생성·렌더 버전은 파일명과 제작 문서에만 둔다.

## 4. 공개 금지 예시

제작자가 추가한 다음 문구는 public이 아니다.

- 풀 텍스트 / FULL TEXT
- 원문 보존본 / 원문 그대로 수록 / 검수본 / 검수용
- 원문은 파일에 수록되어 있습니다
- 전체 텍스트는 첨부파일 참조
- text-manifest.txt / QA_REPORT.md / ASSET_AUDIT.md
- rendered version / source file included / text preserved
- 누락 0자 / 렌더링 완료 / 내부 작업용

`ELITE REPORT`, 승인 계정 크레딧, 페이지 번호는 출판물의 브랜드 요소이므로 허용한다.

## 5. 무차별 단어 삭제 금지

`원문`, `보고서`, `파일`, `출처`, `분석`이라는 단어 자체를 금지하지 않는다.

유지해야 하는 예:

- 본 보고서는 2020~2025년 기록을 분석한다.
- 선수별 시즌 최고 기록 기준이며 같은 선수의 중복 출전은 제외했다.
- 조사 기간과 표본 수.
- 원문 자료와 데이터 파일을 비교한 연구 방법.
- 실제 논문 제목, 인용문, 사진 작가·라이선스, 출처 링크.
- 독자가 자료의 한계를 이해하는 데 필요한 주의사항.

연구 설명과 제작 과정 설명을 구분한다. 출처 표기를 없애거나 자료 한계를 감추는 데 이 규칙을 사용하지 않는다.

## 6. 원문 보존과 충돌할 때

- 렌더러가 추가한 메타정보: public에서 제거하고 production에 기록한다. 원문은 손대지 않는다.
- 원문 자체에 메타처럼 보이는 표현이 있음: 자동 삭제하지 않는다. 원문 맥락과 공개 필요도를 확인한다.
- 실제 논문 제목·방법론 등으로 필요한 경우: 노드에 `public_exception`의 approved, reason, approval_ref를 기록한다.
- 사용자가 특정 문구를 공개하라고 지시한 경우: 해당 문구에 한정한 예외로 기록한다.
- 애매한 원문을 조용히 삭제하는 대신 검토를 완료한 뒤 렌더링한다.

## 7. 전후 검사

렌더링 전 승인 public 텍스트와 렌더링 후 실제 draw-call 텍스트를 각각 검사한다.

```bash
python scripts/lint_public_surface.py production/public-surface.json --report production/PUBLIC_SURFACE_PREFLIGHT.json
python scripts/lint_public_surface.py production/render-surface.json --report production/PUBLIC_SURFACE_QA.json
```

실제 이미지에 표시하는 모든 문자열을 draw log로 내보낸다. 표·그래프 글자를 로그에 빠뜨린 채 본문만 검사하지 않는다. HTML 사용 시 textContent만 믿지 말고 가상 요소·canvas 텍스트·이미지에 원래 포함된 문구도 시각 검수한다.

검사기는 후보 표현과 잘못된 노출층을 찾아 실패 처리하지만 문자열을 수정하지 않는다. 미등록 메타 문구는 사람이 전체 PNG·콘택트시트에서 확인한다. 통과 결과는 production 문서에 기록하고 슬라이드에 쓰지 않는다.
