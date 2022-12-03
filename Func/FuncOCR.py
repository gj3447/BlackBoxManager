import numpy as np
from pytesseract import Output
import pytesseract as pt
import cv2
from PIL import Image

#OCR = 이미지의 텍스트를 텍스트 데이터로 바꾸는거
#대표적인 OCR 오픈소스인 tesseract 를 사용하여 자동차 번호판의 이미지를 String 자료형으로 변환함
def Textoutput(window):
    def inner():
        if(window.file_name!=""):
            file_name = window.file_name
            
            #경로설정
            pt.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
            
            str = pt.image_to_string(Image.open(file_name))
            print(file_name)
            window.statusbar.showMessage("TEXT: " +str)
            print(str)
            
    return inner