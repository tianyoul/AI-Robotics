'''This program uses a video feed input and determine regions of movement.
    It then creates contour boxes for such regions, and track them (look for movements in later frames)'''

import cv2
import numpy as np

vidCap = cv2.VideoCapture(0)
ret, prevImg = vidCap.read()

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(5)

while True:
    x = cv2.waitKey(10)
    char = chr(x & 0xFF)
    if char == 'q':
        break

    ret, img = vidCap.read()
    grayPrevImg = cv2.cvtColor(prevImg, cv2.COLOR_BGR2GRAY)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(img, learningRate = 0.05)
    blurred = cv2.blur(fgmask,(5,5))
    # finding the contours
    ret, thresh = cv2.threshold(blurred, 77, 255, 0)
    # was cv2.RETR_TREE and cv2.CHAIN_APPROX_SIMPLE
    conImg, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if (len(contours)!=0):
        largest = sorted(contours, key=cv2.contourArea, reverse=True)
        x, y, w, h = cv2.boundingRect(largest[0])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Img", img)

vidCap.release()
cv2.destroyAllWindows()