
import cv2
import threading
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from Func.Inum import State

#카메라 실행 쓰레드
#pyqt 의 aplication 이 돌아가야하기때문에 따로 쓰레드를 만들어야함
#현재 카메라의 이미지를 계속가져오고 ImageChange 함수로 보여줌
def run(window):
    cap = cv2.VideoCapture(0)
    width = 800
    height = 600
    window.label.resize(width, height)
    while window.state == State.CAMERA_RUN:
        ret, img = cap.read()
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            reimg = cv2.resize(img, dsize=(width,height),interpolation=cv2.INTER_AREA)
            
            window.original_img = reimg
            window.edit_img = reimg
            window.imageChange(reimg)

        else:
            QtWidgets.QMessageBox.about(window, "Error", "Cannot read frame.")
            print("cannot read frame.")
            break

    cap.release()
    print("Thread end.")

#카메라 종료 함수
#이미지를 계속 가져오고 저장하기때문에
#종료했을때 마지막에 가져온 이미지를 가지고있어서 캡쳐한것처럼 기능함
def end(window):

    def inner():
        window.file_path = ""
        window.state = State.DEFAULT
        print("end..")
    return inner

#카메라 시작 함수
def start(window):
    def inner():
        window.file_path = ""
        window.state = State.CAMERA_RUN
        th = threading.Thread(target=run,args=(window,))
        th.start()
        print("start..")
    return inner


