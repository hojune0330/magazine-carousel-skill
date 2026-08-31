# Asset Intake & Visual Fallback v3.3

이 문서는 텍스트 중심 스킬의 입력 형식과 보조 자산 처리를 정의한다. 페이지별 자료 조사는 `image-research-and-placement.md`, 공개층은 `audience-content-boundary.md`를 따른다.

## 1. 입력 형식

- 사진: JPG/JPEG, PNG, WebP.
- 조건부 변환: HEIC/HEIF, TIFF, BMP, GIF. 실제 디코더 지원을 확인하고 원본은 보존한다.
- 로고·도식: SVG, 투명 PNG.
- 문서: PDF, PPTX, DOCX. 실제 문서·PDF 도구로 필요한 내용과 이미지를 확인한다.
- 그래프 데이터: CSV, XLSX, JSON. 스프레드시트는 해당 전용 도구 규칙을 따른다.
- 영상: MP4, MOV, WebM. 허용된 프레임을 시간코드와 함께 추출한다.
- ZIP: 원본 폴더 구조를 보존하며 경로 탈출 항목·실행파일·과도한 압축 해제 용량은 차단한다. 임의 스크립트를 실행하지 않는다.

ZIP의 선택 구조: photos / screenshots / logos / documents / data / asset-notes.csv. 사용자가 이런 폴더명을 쓰지 않아도 실제 파일을 조사해 정리한다.

## 2. 형식·품질

EXIF 방향, sRGB 변환, 알파 채널, 해상도·비율을 확인한다. 원본은 읽기 전용으로 보존하고 변환본을 따로 만든다.

대형 사진 짧은 변 1600px 이상, 권장 2400px 이상은 후보 기준이다. 실제 배치 픽셀 크기와 선명도를 함께 평가한다. 작은 슬롯에 충분한 파일을 치수만으로 배제하지 않는다. 불필요한 업스케일로 정보를 복원했다고 주장하지 않는다.

## 3. 감사

local_path, format, width, height, color_space, has_alpha, sha256, perceptual_hash, subject/source metadata, quality, rights_status, used_on을 기록한다.

해시 동일 파일과 시각적으로 가까운 후보를 확인한다. 근접한 해시는 자동 삭제 근거가 아니라 검토 신호다. 배경 블러용 동일 사진은 같은 장의 한 번 사용으로 본다.

## 4. 사진 필요도

기본은 optional이다. 표 페이지는 forbidden, 나머지는 본문을 다 배치한 뒤 의미와 공간을 판단한다. 20장에 사진 20장이 필요하지 않다. 이미지 부족이 곧 콘텐츠 부족은 아니다.

## 5. 대체 선택

1. 관련 사용자 이미지.
2. 권리 확인 가능한 실제 원본 다운로드.
3. 독자 이해에 필요한 실제 웹/PDF/영상 캡처.
4. 실제 데이터의 코드 그래프·표.
5. 원문 구조의 코드 도식·타임라인.
6. 허용된 낮은 불쾌감 2D 보조 아이콘·캐릭터.
7. 적합한 시각물이 없으면 텍스트만 사용.

이 순서를 채우기 체크리스트처럼 강제하지 않는다. 텍스트만으로 충분하면 바로 7번으로 끝낸다. 모든 보조 시각물은 원문을 삭제·요약하는 근거가 될 수 없다.

## 6. 생성형과 코드 렌더링 구분

`generator_kind`를 deterministic / generative-ai / none으로 별도 기록한다. 기존 generated-chart origin은 코드로 생성한 정확한 차트일 수 있다. `generated-*` 접두사만으로 생성형 AI라고 판단하지 않는다.

사용자 생성 금지 지시가 있으면 generator_kind=generative-ai를 사용하지 않는다. 실제 자료만 요청하면 허구적 보조 캐릭터도 배제한다. 최종 페이지 조판은 항상 deterministic이다.

허용된 생성형 보조 에셋은 친근한 평면 2D, 낮은 불쾌감, 왜곡·공포·부상 클로즈업 없는 개념용으로 제한한다. 실제 선수의 가짜 사진이나 증거 화면을 만들지 않는다. 글자·표·페이지 번호는 렌더러가 그린다.

## 7. 출처와 공개층

origin은 user-upload / downloaded-original / official-screenshot / pdf-capture / video-frame / app-capture / generated-chart / generated-table / generated-diagram / generated-timeline / generated-map / generated-icon / generated-character / generated-illustration 등을 기록할 수 있다. 각 항목에 실제 획득·제작 방법을 적는다.

조사·감사·실패 로그는 production/internal 문서다. 촬영 맥락·필수 출처·권리 표기는 public에 남긴다. 검색 링크만 확인한 자산을 내려받았다고 기록하지 않는다.
