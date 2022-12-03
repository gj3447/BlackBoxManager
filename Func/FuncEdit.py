import cv2

from Func.Inum import State

#90도 회전함수 opencv 기능 활용
def Rotate(window):
    def inner():
        img90 = cv2.rotate(window.original_img,cv2.ROTATE_90_CLOCKWISE).copy()
        window.original_img = img90
        window.edit_img = img90
        window.imageChange(img90)
    return inner
#잘라내기 기능 함수 window 의 상태를 CUT으로 바꾸면 ImageLabel 파일의 이벤트핸들러가 잘라내기 기능을 수행함
def Cut(window):
    def inner():
        window.state = State.EDIT_CUT
        window.statusbar.showMessage("CUT")
    return inner
#사이즈변환 기능 함수 window 의 상태를 EDIT_SIZE으로 바꾸면 ImageLabel 파일의 이벤트핸들러가 잘라내기 기능을 수행함
def Size(window):
    def inner():
        window.state = State.EDIT_SIZE
        window.edit['size'] = float(1)
        window.statusbar.showMessage("SIZE")
    return inner
#위치정렬함수 이미지를 잘라낼때 잘라내는 위치가 이미지 바깥으로 안가도록 해줌
def Sort(window,x,y):
    result_x = x
    result_y = y
    h,w,c = window.original_img.shape
    if(x<0) :
        result_x = 0
    if(y<0) :
        result_y = 0
    if (x>w):
        result_x = w-1
    if (y>h):
        result_y = h-1
    return [result_x,result_y]