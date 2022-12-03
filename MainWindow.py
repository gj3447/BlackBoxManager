import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2

import Func.FuncFile as Ffile
import Func.FuncEdit as Fedit
import Func.FuncCamera as Fcamera
import Func.FuncFilter as Ffilter
import Func.FuncOCR as Focr
from Func.Inum import State
from ImageLabel import ImageLabel


#main_window
class main_window(QMainWindow):
    
    #main생성자
    #main_window 에 변수 선언하고 init 함수 실핸
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.file_name = ""
        self.original_img = ""
        self.edit_img = ""
        self.state = State.DEFAULT
        self.edit={
            'cut':[0,0],
            'size':0,
        }
        
        self.initMenu()
        self.initUI()
    
    #ui 생성 함수
    def initUI(self):
        self.setWindowTitle("블랙박스 매니저")
        self.setMouseTracking(True)
        label = ImageLabel(self)
        self.label = label
        label.setScaledContents(True)
        self.setCentralWidget(label)
        self.statusbar = self.statusBar()
        Ffile.LoadImage(window=self,path="./images/BlackBox.webp")
    
    #menu 생성 함수
    def initMenu(self):

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&파일')
        cameramenu = menubar.addMenu('&카메라')
        editmenu = menubar.addMenu('&편집')
        filtermenu = menubar.addMenu('&필터')
        tfmenu = menubar.addMenu('&TF')
        
        self.initMenu_File(menu=filemenu)
        self.initMenu_Camera(menu=cameramenu)
        self.initMenu_Edit(menu=editmenu)
        self.initMenu_Filter(menu=filtermenu)
        self.initMenu_TF(menu=tfmenu)
        
    #File 관련 menu 생성 기능은 FuncFile 파일에 있음
    def initMenu_File(self,menu):
        
        LoadAction = QAction('불러오기', self)
        LoadAction.setShortcut('Ctrl+L')
        LoadAction.setStatusTip('이미지를 불러옵니다.')
        LoadAction.triggered.connect(Ffile.Load(window=self))
        
        SaveAction = QAction('저장', self)
        SaveAction.setShortcut('Ctrl+S')
        SaveAction.setStatusTip('이미지를 저장합니다.')
        SaveAction.triggered.connect(Ffile.Save(window=self))
        
        SaveAsAction = QAction('다른이름으로 저장', self)
        SaveAsAction.setShortcut('Ctrl+D')
        SaveAsAction.setStatusTip('이미지를 다른이름으로 저장합니다.')
        SaveAsAction.triggered.connect(Ffile.SaveAs(window=self))
        
        ExitAction = QAction('종료', self)
        ExitAction.setShortcut('Ctrl+Q')
        ExitAction.setStatusTip('프로그램을 종료합니다.')
        ExitAction.triggered.connect(self.app.quit)
        
        
        menu.addAction(LoadAction)
        menu.addAction(SaveAction)
        menu.addAction(SaveAsAction)
        menu.addAction(ExitAction)
    
    
    #Camera 관련 menu 생성 기능은 FuncCamera 파일에 있음
    def initMenu_Camera(self,menu):
        
        StartAction = QAction('켜기',self)
        StartAction.setShortcut('Ctrl+O')
        StartAction.setStatusTip('카메라를 켭니다.')
        StartAction.triggered.connect(Fcamera.start(window=self))
        
        EndAction = QAction('캡처',self)
        EndAction.setShortcut('Ctrl+P')
        EndAction.setStatusTip('현재 카메라 화면을 캡쳐합니다.')
        EndAction.triggered.connect(Fcamera.end(window=self))
        
        menu.addAction(StartAction)
        menu.addAction(EndAction)
    
    
    #Edit 관련 menu 생성 기능은 FuncEdit 파일에 있음
    def initMenu_Edit(self,menu):
        
        SizeAction = QAction('크기', self)
        SizeAction.setShortcut('Ctrl+Y')
        SizeAction.setStatusTip('이미지의 크기를 조절합니다..')
        SizeAction.triggered.connect(Fedit.Size(window=self))
        
        CutAction = QAction('잘라내기', self)
        CutAction.setShortcut('Ctrl+T')
        CutAction.setStatusTip('이미지를 일부분 잘라냅니다.')
        CutAction.triggered.connect(Fedit.Cut(window=self))
        
        RotateAction = QAction('회전',self)
        RotateAction.setShortcut('Ctrl+R')
        RotateAction.setStatusTip('오른쪽으로 90도 회전 시킵니다.')
        RotateAction.triggered.connect(Fedit.Rotate(window=self))
        
        
        menu.addAction(SizeAction)
        menu.addAction(CutAction)
        menu.addAction(RotateAction)
        
        return
    
    #Filter 관련 menu 생성 기능은 FuncFilter 파일에 있음
    def initMenu_Filter(self,menu):
        
        m11_5 = QAction('퓨리에 변환', self)
        m10_3 = QAction('모멘트', self)        
        m9_6 = QAction('모폴로지', self)
        m8_4 = QAction('외곽선', self)
        m5_5 = QAction('중앙값', self)
        m5_4 = QAction('가우시안', self)
        m5_3 = QAction('중간값', self)
        m5_2 = QAction('블러', self)
        m5_1 = QAction('평균값', self)
        m4_6 = QAction('히스토그램', self)
        
        m9_6.triggered.connect(Ffilter.m9_6(window=self))
        m5_4.triggered.connect(Ffilter.m5_4(window=self))
        m5_3.triggered.connect(Ffilter.m5_3(window=self))
        m5_2.triggered.connect(Ffilter.m5_2(window=self))
        m5_1.triggered.connect(Ffilter.m5_1(window=self))
        m4_6.triggered.connect(Ffilter.m4_6(window=self))
        
        
        menu.addAction(m9_6)
        menu.addAction(m5_4)
        menu.addAction(m5_3)
        menu.addAction(m5_2)
        menu.addAction(m5_1)
        menu.addAction(m4_6)
        return
    
    #ORC 관련 menu 생성 기능은 FuncFilter 파일에 있음
    def initMenu_TF(self,menu):
        outputText = QAction('텍스트 추출',self)
        outputText.setShortcut('Ctrl+M')
        outputText.setStatusTip('사진의 텍스트를 감지합니다.')
        outputText.triggered.connect(Focr.Textoutput(window=self))
        
        
        menu.addAction(outputText)
        return
    
    #label 이미지 변환함수
    def imageChange(self,img):
        h,w,c= img.shape
        qimg = QImage(img.data,w,h,w*c,QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        self.label.setPixmap(pixmap)
        self.setFixedSize(w,h+50)
        