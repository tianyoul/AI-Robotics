import cv2
import numpy as np

img1 = cv2.imread("TestImages/Puzzle1.jpg")
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Harris Detector
grayImg = np.float32(grayImg)
dst = cv2.cornerHarris(grayImg, 2, 3, 0.04)
dilDst = cv2.dilate(dst, None)
thresh = 0.01 * dst.max()
ret, threshDst =  cv2.threshold(dilDst, thresh, 255, cv2.THRESH_BINARY)

disp = np.uint8(threshDst)

cv2.imshow("Harris", disp)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Shi-Tomasi Detector
img1 = cv2.imread("TestImages/Puzzle1.jpg")
goodFeats = cv2.goodFeaturesToTrack(grayImg, 100, 0.1, 5)
goodFeats = np.int0(goodFeats)
for feature in goodFeats:
    x, y = feature.ravel()
    cv2.circle(img1, (x, y), 10,(0,255,0),2)
cv2.imshow("Shi-tomosi", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()