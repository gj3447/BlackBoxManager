import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
import numpy as np

#이미지로드 함수
def Load(window):
    def inner():
        fname = QFileDialog.getOpenFileName(window)
        LoadImage(window=window,path=fname[0])
        window.file_name = fname[0]
    return inner

#이미지의 경로를 받으면 main 이미지 적용해주는 함수
def LoadImage(window,path):
    
    img = cv2.imread(path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    window.original_img = img
    window.edit_img = img
    window.imageChange(img=img)
    
#현재 이미지 현재경로에 저장해주는 함수
def Save(window):
    def inner():
        if window.file_name == "":
            SaveAs(window)()
        else:
            img = cv2.cvtColor(window.original_img,cv2.COLOR_BGR2RGB)
            cv2.imwrite(window.file_name,img)
    return inner

#현재 이미지 원하는 이름으로 저장해주는 함수
def SaveAs(window):
    def inner():
        fname = QFileDialog.getSaveFileName(window)
        if(fname[0]!=""):
            img = cv2.cvtColor(window.original_img,cv2.COLOR_BGR2RGB)
            cv2.imwrite(fname[0]+".jpg",img)
            window.file_name = fname[0]
    return inner