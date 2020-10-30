import  cv2 as cv
import numpy as np


path = "C:\\Users\\TY\\Pictures\\Saved Pictures\\LinYoga.jpg"
src = cv.imread(path)
cv.namedWindow("initial image",cv.WND_PROP_AUTOSIZE)
cv.imshow("initial",src)
 