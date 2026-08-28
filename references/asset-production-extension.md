# Asset Production Extension v3.2

이 문서는 `production-workflow.md`를 확장한다. 이미지 입력·자산 부족·캡처·그래프·도식·보조 생성 이미지가 포함된 작업에서는 이 문서를 추가로 적용한다. 두 문서가 충돌하면 이 확장 문서가 우선한다.

## 1. 삽입되는 제작 단계

기존 원문 잠금 이후, 페이지 맵 작성 전에 다음 단계를 수행한다.

```text
source lock
→ upload normalization
→ asset audit
→ page visual requirement classification
→ shortage detection
→ visual fallback planning
→ page map
→ deterministic rendering
→ QA and packaging
```

## 2. 입력 정규화

- JPG/JPEG, PNG, WebP는 그대로 검사한다.
- HEIC/HEIF, TIFF, BMP는 sRGB PNG/JPG로 변환한다.
- GIF는 필요한 프레임을 추출한다.
- SVG는 벡터 상태를 유지하거나 렌더링 해상도에 맞춰 래스터화한다.
- PDF는 필요한 페이지와 도표만 캡처·추출한다.
- CSV/XLSX/JSON은 그래프·표 원본으로 보존한다.
- MP4/MOV/WebM은 허용된 프레임만 시간코드와 함께 추출한다.
- ZIP은 폴더 구조를 유지해 해제하고 파일별 메타데이터를 만든다.

## 3. ASSET_AUDIT.md 생성

각 자산에 대해 기록한다.

```text
id
filename
format
width x height
orientation
color space
alpha
sha256
perceptual hash
subject tags
quality
rights status
recommended use
exclude reason
```

완전 중복, 근접 중복, 해상도 부족, 권리 불명확 자산을 표시한다.

## 4. 페이지 시각 요구도 분류

각 페이지를 아래 중 하나로 표시한다.

```text
photo-required
photo-preferred
photo-optional
photo-forbidden
data-visual
capture-evidence
diagram-preferred
typography-sufficient
```

표 페이지는 항상 photo-forbidden이다.

## 5. 부족 감지

다음 중 하나면 자산 부족으로 기록한다.

- photo-required 페이지에 관련 사진 없음
- 같은 사진 반복이 필요함
- 피사체가 슬롯에서 지나치게 작아짐
- 해상도 미달
- 원문과 의미 연결 약함
- 출처·권리 확인 불가

## 6. VISUAL_FALLBACK_LOG.md 생성

페이지별로 다음을 기록한다.

```yaml
page: 8
shortage_reason: no-relevant-photo
selected_tier: 4
selected_type: chart-report
source_basis: source.txt lines or data file
asset_origin: generated-chart
why: record progression is numerical and clearer as a chart
```

## 7. 대체 시각물 제작

### 실제 캡처

- 공식 웹/PDF/영상/앱에서 직접 캡처
- URL·제목·날짜·페이지·시간코드 기록
- 개인정보 마스킹
- 데이터 변조 금지

### 그래프·표

- 실제 원문·CSV·공식 결과만 사용
- 축·단위·기간·출처 필수
- 수치 추정 금지

### 도식

- 원문 구조만 표현
- 인과관계 추가 금지
- 선·화살표·레이블은 코드 조판

### 보조 생성 이미지

- 실제 자료와 데이터 시각화로 해결되지 않을 때만 사용
- clean-flat-2d, healthy-calm-friendly
- uncanny/discomfort very low
- 실제 선수·경기 증거처럼 보이는 포토리얼 생성 금지
- 생성 자산 내부 긴 한국어 텍스트 금지
- 사용자가 생성 기능을 금지하면 비활성화

## 8. asset-map origin

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

## 9. 최종 산출물 확장

기존 산출물에 다음을 반드시 추가한다.

```text
ASSET_AUDIT.md
VISUAL_FALLBACK_LOG.md
```

`IMAGE_SOURCES.md`에는 사진뿐 아니라 캡처·그래프·도식·생성 보조 자산의 출처와 생성 근거도 기록한다.

## 10. 완료 금지 조건

- 자산 부족 페이지가 있는데 대체 근거가 없음
- 중복 사진으로 억지 채움
- 출처 없는 캡처
- 가짜 수치 그래프
- 실제 사건으로 오인될 생성 이미지
- 불쾌감·신체 왜곡이 큰 아이콘·캐릭터
- ASSET_AUDIT.md 또는 VISUAL_FALLBACK_LOG.md 누락
