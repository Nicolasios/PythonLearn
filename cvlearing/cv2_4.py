import cv2 as cv
import numpy as np

print("------Hello Python------")
src = cv.imread("C:\\Users\TY\Pictures\Saved Pictures\LinYoga.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

face = src[200:250,100:300]
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[200:250,100:300] = backface
cv.imshow("face",src)
cv.waitKey(0)

cv.destroyAllWindows() 