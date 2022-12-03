import numpy as np
import numpy.fft as fp
import cv2

from scipy import ndimage, misc, signal, fftpack

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.sttd(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)


#연습문제 9-6
def m9_6(window):#모폴로지 연산
    
    def inner():
        img = window.original_img
        
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((5,5),np.uint8)
        closing = cv2.morphologyEx(gray_img, cv2.MORPH_CLOSE, kernel)
        
        img2 = cv2.cvtColor(closing,cv2.COLOR_GRAY2BGR)
        window.original_img = img2
        window.edit_img = window.original_img
        window.imageChange(img = window.original_img)
    return inner



#연습문제 5-4
def m5_4(window):#가우시안 블러
    
    def inner():
        img = window.original_img
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 5x5 가우시안 커널 적용하기
        output_img = cv2.GaussianBlur(gray_img,(5,5),1)
        
        
        img2 = cv2.cvtColor(output_img,cv2.COLOR_GRAY2BGR)
        
        window.original_img = img2
        window.edit_img = window.original_img
        window.imageChange(img = window.original_img)
    return inner

#연습문제 5-3
def m5_3(window):#중간값 블러
    
    def inner():
        img = window.original_img
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 5x5 중간값 커널 적용하기
        output_img = cv2.medianBlur(gray_img,5)

        img2 = cv2.cvtColor(output_img,cv2.COLOR_GRAY2BGR)
        window.original_img = img2
        window.edit_img = window.original_img
        window.imageChange(img = window.original_img)
    return inner

#연습문제 5-2
def m5_2(window):#opencv의 블러함수
    
    def inner():
        img = window.original_img
        
        
        # color영상을 gray영상으로 만들기
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 3x3커널 적용하기
        output_img = cv2.blur(gray_img,(3,3))
        
        img2 = cv2.cvtColor(output_img,cv2.COLOR_GRAY2BGR)
        window.original_img = img2
        window.edit_img = window.original_img
        window.imageChange(img = window.original_img)
    return inner

#연습문제 5-1
def m5_1(window):#평균값 블러
    
    def inner():
        img = window.original_img
        
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 계수가 1로 구성된 3x3커널 만들기
        kernel = np.ones((3,3),np.float32)/9
        output_img = cv2.filter2D(gray_img,-1,kernel)
        
        img2 = cv2.cvtColor(output_img,cv2.COLOR_GRAY2BGR)
        
        window.original_img = img2
        window.edit_img = window.original_img
        window.imageChange(img = window.original_img)
    return inner

#연습문제 4-6
def m4_6(window):#히스토그램 평활화
    
    def inner():
        img = window.original_img
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        output_img = cv2.equalizeHist(gray_img)

        hist=cv2.calcHist([gray_img],[0],None,[256],[0,256])
        hist=cv2.calcHist([output_img],[0],None,[256],[0,256])
        
        img2 = cv2.cvtColor(output_img,cv2.COLOR_GRAY2BGR)
        
        window.original_img = img2
        window.edit_img = window.original_img
        window.imageChange(img = window.original_img)
    return inner