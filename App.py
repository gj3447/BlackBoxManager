import sys
from PyQt5.QtWidgets import *
from MainWindow import main_window


#메인 실행파일
app = QApplication([])
window = main_window(app=app)
window.show()
app.exec_()