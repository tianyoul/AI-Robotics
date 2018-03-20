import cv2
import numpy as np

vidCap = cv2.VideoCapture(0)
ret, prevImg = vidCap.read()

while True:
    x = cv2.waitKey(0)
    char = chr(x & 0xFF)
    if char == 'q':
        break

    ret, img = vidCap.read()
    grayPrevImg = cv2.cvtColor(prevImg, cv2.COLOR_BGR2GRAY)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    prevImg = img