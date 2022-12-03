import sys
import cv2

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Func.Inum import State
import Func.FuncEdit as Fedit


#그림 라벨
class ImageLabel(QLabel):
    def __init__(self,window):
        super().__init__()
        self.window = window
        
        
#마우스 움직였을때
#잘라내기 상태일경우 사각형그리기 그리고 statusbar 에 현재좌표 찍기
    def mouseMoveEvent(self,e):
        if(self.window.state == State.EDIT_CUT_DRAG):
            point = Fedit.Sort(window=self.window,x=e.x(),y=e.y())
            txt = "CUT: ({0},{1})~({2},{3})".format(self.window.edit['cut'][0],self.window.edit['cut'][1],point[0],point[1])
            self.window.edit_image = self.window.original_img.copy()
            cv2.rectangle(self.window.edit_image,(self.window.edit['cut'][0],self.window.edit['cut'][1]),(point[0],point[1]),1)
            self.window.imageChange(img=self.window.edit_image)
            self.window.statusbar.showMessage(txt)
#마우스 눌렀을때
#잘라내기 상태일경우 눌렀을때의 위치를 자르는 시작점 으로 window.edit 에 저장
#크기조절 상태일경우 현재 크기를 window_original_img 에 저장
    def mousePressEvent(self, e):
        if(self.window.state == State.EDIT_CUT):
            self.window.state = State.EDIT_CUT_DRAG
            self.window.edit['cut'] = Fedit.Sort(self.window,e.x(),e.y())
        if(self.window.state == State.EDIT_SIZE):
            self.window.state = State.DEFAULT
            self.window.original_img = self.window.edit_img.copy()
            self.window.imageChange(self.window.original_img)
            self.window.statusbar.showMessage("")

#마우스 뗏을때
#잘라내기 상태일경우 눌렀을때 위치와 지금 위치를 잘라서 이미지 생성
    def mouseReleaseEvent(self,e):
        if(self.window.state == State.EDIT_CUT_DRAG):
            self.window.state = State.DEFAULT
            point = Fedit.Sort(window=self.window,x=e.x(),y=e.y())
            txt = "CUT: ({0},{1})~({2},{3})".format(self.window.edit['cut'][0],self.window.edit['cut'][1],point[0],point[1])
            self.window.statusbar.showMessage(txt)
            output = self.window.original_img[self.window.edit['cut'][1]:point[1],self.window.edit['cut'][0]:point[0]].copy()
            
            self.window.original_img = output
            self.window.edit_img = output
            self.window.imageChange(img=self.window.original_img)
            
            self.window.statusbar.showMessage("")
            
#휠 움직였을때
#크기조절 상태일경우 휠업 = 크기 증가, 휠다운 = 크기감소
    def wheelEvent(self, e) -> None:
        if(self.window.state == State.EDIT_SIZE):
            self.window.edit['size'] -= e.angleDelta().y() * 0.01
            txt = "SIZE: {0}".format(self.window.edit['size'])
            
            h,w,c = self.window.original_img.shape
            fixh = int( h*self.window.edit['size'])
            fixw = int( w*self.window.edit['size'])
            resize_img = cv2.resize(self.window.original_img, (fixw, fixh))
            self.window.edit_img = resize_img
            self.window.imageChange(resize_img)
            self.window.statusbar.showMessage(txt)
    