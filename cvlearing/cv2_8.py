import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.show("直方图")

def image_hist(image):
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color = color)
        plt.xlim([0,256])
    plt.show()

print("------Hello Python------")
src_1 = cv.imread("C:\\Users\TY\Pictures\Saved Pictures\LinYoga.jpg")
src_2 = cv.imread("C:\\Users\TY\Pictures\photoshop\Lin.jpg")
cv.imshow("orgion",src_2)
image_hist(src_2)

cv.waitKey(0)


cv.destroyAllWindows()