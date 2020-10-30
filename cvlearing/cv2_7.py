import cv2 as cv
import numpy as np
import matplotlib 

def bi_demo(image):
    dst = cv.bilateralFilter(image,0,90,15)
    cv.imshow("bi_demo",dst)

print("------Hello Python------")
src_1 = cv.imread("C:\\Users\TY\Pictures\Saved Pictures\LinYoga.jpg")
src_2 = cv.imread("C:\\Users\TY\Pictures\photoshop\\tear.jpg")
bi_demo(src_2)
cv.waitKey(0)


cv.destroyAllWindows()