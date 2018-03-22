import cv2
import numpy as np

#Histograms
# im1 = cv2.imread('TestImages/garden.jpg')
# grayIm1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
# newGray = cv2.equalizeHist(grayIm1)
# cv2.imshow('Original', grayIm1)
# cv2.imshow('Equalized', newGray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#contours
# import numpy as np
# import cv2
#
# origIm = cv2.imread('TestImages/Coins1.jpg')
# imgray = cv2.cvtColor(origIm,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# im2, contrs, hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(origIm, contrs, -1, (0,255,0), 3)
# cv2.imshow('Contours', origIm)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#milestone1
origIm = cv2.imread('TestImages/Coins1.jpg')
imgray = cv2.cvtColor(origIm,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,95, 255, 0)
cv2.imshow("Thresholded", thresh)
im2, contrs, hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(origIm, contrs, -1, (0,255,0), 3)
cv2.imshow('Contours', origIm)
cv2.waitKey(0)
cv2.destroyAllWindows()