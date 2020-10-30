import cv2 as cv
import numpy as np

def blur_demo(image):
    dst = cv.blur(image,(40,1))
    cv.imshow("blur demo",dst)

def median_blur_demo(image):
    dst = cv.medianBlur(image,3)
    cv.imshow("median_blur_demo",dst)

def custom_blur_demo(image):
    kernel = np.array([[0,-1,0],[-3,9,-3],[0,-1,0]],np.float32)
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("custom_blur_demo",image)

print("------Hello Python------")
src_1 = cv.imread("C:\\Users\TY\Pictures\Saved Pictures\LinYoga.jpg")
src_2 = cv.imread("C:\\Users\TY\Pictures\photoshop\Lin.jpg")
cv.imshow("input_image_1",src_1)
#cv.imshow("input_image_2",src_2)
#blur_demo(src_1)
#median_blur_demo(src_2)
custom_blur_demo(src_1)
cv.waitKey(0)

cv.destroyAllWindows()