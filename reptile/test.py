import cv2

cv2.namedWindow('photo',0)   #0窗口大小可以任意拖动，1自适应
cv2.resizeWindow('photo',640,480)

url='http://i5.qhimg.com/t019c3e49c9c9319c33.jpg'
cap=cv2.VideoCapture(url)
ret=cap.isOpened()
while (ret):
    ret,img=cap.read()
    if not ret:break
    cv2.imshow('photo', img)
    cv2.waitKey(0)
cap.release()