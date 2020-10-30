import cv2 as cv
import numpy as np


def inverse(image):
    inverse = cv.bitwise_not(image)
    cv.imshow("inverse",inverse)

def bitnot(image):
    drt = 255-image
    cv.imshow("drt",drt)

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    #Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    #cv.imshow("ycrcb",Ycrcb)

def video_cap():
    capture = cv.VideoCapture("C:\\Users\\TY\\Pictures\\Saved Pictures\\ikun.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([0,43,46])
        upper_hsv = np.array([10,255,255])
        mask = cv.inRange(hsv,lowerb = lower_hsv,upperb = upper_hsv)
        cv.imshow("frame",frame)
        cv.imshow("mask",mask)
        cv.imshow("hsv",hsv)
        c = cv.waitKey(40)
        if c == 27:
            break



print("---opencv---")
src = cv.imread("C:\\Users\\TY\\Pictures\\Saved Pictures\\blue.jpg")
cv.namedWindow("yoga",cv.WINDOW_FULLSCREEN)
cv.imshow("yoga",src)
'''
t1 = cv.getTickCount()
color_space_demo(src)
t2 = cv.getTickCount()
t = (t2-t1)/cv.getTickFrequency()
print("time : %s ms" % (t + 1000))
'''
#video_cap()
b ,g ,r = cv.split(src)
src[:,1,:]
print(src[:,1,:])
'''
cv.imshow("change",src)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
'''
cv.waitKey(0)

cv.destroyAllWindows()