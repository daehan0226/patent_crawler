### 키프리스에서 특허 엑셀 파일로 다운로드
---
### 크롤링 과정
1. 키프리스 웹페이지 로드
2. 로그인 팝업창을 통해 로그인 정보 입력 후 로그인
3. 검색 정보 입력 - (등록특허만 연도별 등록날짜 정렬 후 다운로드)
4. 다운로드 팝업창을 통해 다운로드 정보 입력 후 파일 생성
5. 파일 다운로드

### 로그 확인
* info : 로딩 페이지 확인, 종료 메세지
* debug : 텍스트 추출 시, 버튼 클릭 시, 텍스트 입력시 확인
* error : 엘리먼트 찾지 못한 경우, Alert time out, 탭 변경 에러, 잘못된 페이지 로딩한 경우, 엘리먼트 선택자 타입 에러, 엘리먼트 잘못된 형태([css, 선택자])