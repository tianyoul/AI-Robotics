import cv2
import numpy as np

coins1Img = cv2.imread("TestImages/Coins1.jpg")
grayImg1 = cv2.cvtColor(coins1Img, cv2.COLOR_BGR2GRAY)
circles1 = cv2.HoughCircles(grayImg1, cv2.HOUGH_GRADIENT, 1, 30,
                              param1 = 80, param2 = 70,
                              minRadius = 10, maxRadius = 50)

for i in circles1[0,:]:
    # draw the outer circle
    cv2.circle(coins1Img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(coins1Img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow("Coins1", coins1Img)
cv2.waitKey(0)
cv2.destroyAllWindows()

coins2Img = cv2.imread("TestImages/Coins2.jpg")
grayImg2 = cv2.cvtColor(coins2Img, cv2.COLOR_BGR2GRAY)
circles2 = cv2.HoughCircles(grayImg2, cv2.HOUGH_GRADIENT, 1, 30,
                              param1 = 85, param2 = 70,
                              minRadius = 40, maxRadius = 100)
for i in circles2[0,:]:
    # draw the outer circle
    cv2.circle(coins2Img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(coins2Img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow("Coins2", coins2Img)
cv2.waitKey(0)
cv2.destroyAllWindows()