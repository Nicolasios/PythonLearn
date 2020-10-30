import cv2 as cv
import numpy as np

def video_cap():
    capture = cv.VideoCapture("https://haokan.baidu.com/v?vid=10514426888720153099&pd=bjh&fr=bjhauthor&type=video")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        cv.imshow("ikun_1",frame)
        frame = cv.bitwise_not(frame)
        cv.imshow("ikun_2",frame)
        c = cv.waitKey(40)
        if  c == 27:
            break


def calcul(img_1,img_2):
    src_3 = cv.add(img_1,img_2)
    cv.imshow("add_1",src_3)
    src_3 = cv.subtract(img_1,img_2)
    cv.imshow("sub_1",src_3)
    src_3 = cv.subtract(img_2,img_1)
    cv.imshow("sub_2",src_3)
    src_3 = cv.divide(img_2,img_1)
    cv.imshow("div",src_3)
    src_3 = cv.multiply(img_1,img_2)
    cv.imshow("mul",src_3)

def others(img_1,img_2):
    M1, dev1 = cv.meanStdDev(img_1)
    M2, dev2 = cv.meanStdDev(img_2)
    print(M1)
    print(M2)
    print("---")
    print(dev1)
    print(dev2)

def logic(img_1,img_2):
    src_3 = cv.bitwise_and(img_1,img_2)
    cv.imshow("and",src_3)
    src_3 = cv.bitwise_or(img_1,img_2)
    cv.imshow("or",src_3)
    src_3 = cv.bitwise_xor(img_1,img_2)
    cv.imshow("xor",src_3)
    src_3 = cv.bitwise_not(img_1)
    cv.imshow("not_1",src_3)
    src_3 = cv.bitwise_not(img_2)
    cv.imshow("not_2",src_3)


print("---opencv---")
src_1 = cv.imread("https://dss0.baidu.com/73F1bjeh1BF3odCf/it/u=2710340220,146640331&fm=85&s=8820F1130EF1329007A48C440300E060")
src_2 = cv.imread("C:\\Users\\TY\\Pictures\\Saved Pictures\\02.jpg")
cv.imshow("Linux",src_1)
cv.imshow("Windows",src_2)
#calcul(src_1,src_2)
#logic(src_1,src_2)
video_cap()
cv.waitKey(0)

cv.destroyAllWindows()