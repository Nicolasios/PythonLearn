import cv2 as cv
import numpy as np

def clamp(pv):
    if pv>255:
        return 255
    if pv<0:
        return 0
    else:
        return pv

def guassian(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,50,3)
            b = image[row,col,0]
            g = image[row,col,1]
            r = image[row,col,2]
            image[row,col,0]=clamp(b+s[0])
            image[row,col,1]=clamp(g+s[1])
            image[row,col,2]=clamp(r+s[2])
    cv.imshow("noise image",image)

print("------Hello Python------")
src_1 = cv.imread("C:\\Users\TY\Pictures\Saved Pictures\LinYoga.jpg")
src_2 = cv.imread("C:\\Users\TY\Pictures\photoshop\Lin.jpg")
#cv.imshow("input_image_2",src_2)
dst = cv.GaussianBlur(src_1,(15,15),0)
cv.imshow("gussian",dst)
#guassian(src_1)
cv.waitKey(0)


cv.destroyAllWindows()