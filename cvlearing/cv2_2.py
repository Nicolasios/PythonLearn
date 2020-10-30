import cv2 as cv
import numpy as np

def video_cap():
    capture = cv.VideoCapture("https://vdept.bdstatic.com/376e4c535274503356326e3341344b68/46794b7851574c35/8c74184d66c8ae1ec70402512dc33d29bcf74d442da726bec9709d9d0a912de6ceb91e0242403c5f9ea65f36656d853b.mp4?auth_key=1581514205-0-0-3a1bdbab88c1132a3a1e9fc24b26e646")
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
src_1 = cv.imread("C:\\Users\\TY\\Pictures\\Saved Pictures\\01.jpg")
src_2 = cv.imread("C:\\Users\\TY\\Pictures\\Saved Pictures\\02.jpg")
cv.imshow("Linux",src_1)
cv.imshow("Windows",src_2)
#calcul(src_1,src_2)
#logic(src_1,src_2)
video_cap()
cv.waitKey(0)

cv.destroyAllWindows()