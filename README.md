필요 라이브러리

pyqt5
opencv
pillow
scipy
numpy

pytesseract--------------

pip 으로 pytesseract 깔고
구글에 tessercat설치 검색해서 설치한다음에
돌려보고
pytesseract 경로오류시
VV
https://ddolcat.tistory.com/953
이웹페이지에 맨밑에 나오는 경로수정한거를
FuncOCR 의 경로설정 주석 밑에 변수에다가 고쳐서 넣어야함



PPT 발표할때 핵심 주제

프로그램 기능 = 블랙박스 차량 번호판 인식을 OCR 으로 구현

OCR 할때 전처리작업이 들어가는데
자동으로 사진별로 동일한 전처리작업를 하는게 아닌
각각 사진에따라 노이즈 제거, 선명하게 하는 작업을
수작업으로 직접 보고 맞춰가면서 OCR의 텍스트 인식률을 더욱 높일수 있다.