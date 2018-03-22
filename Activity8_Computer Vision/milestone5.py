import cv2
import numpy as np


img = cv2.imread("TestImages/twopeople.jpeg")
#cv2.imshow("Original 1", img)

# create an ORB object, that can run the ORB algorithm.
orb = cv2.ORB_create()  # some versions use cv2.ORB() instead

keypts, des = orb.detectAndCompute(img, None)

img2 = cv2.drawKeypoints(img, keypts, None, (255, 0, 0), 4)
cv2.imshow("Keypoints 1", img2)

# create a FAST object, that can run the FAST algorithm.
fast = cv2.FastFeatureDetector_create()
# detect features
keypts = fast.detect(img, None)
img3 = cv2.drawKeypoints(img, keypts, None, (255, 0, 0), 4)
cv2.imshow("Keypoints 2", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


img_two = cv2.imread("TestImages/Coins1.jpg")

keypts, des = orb.detectAndCompute(img_two, None)

img4 = cv2.drawKeypoints(img_two, keypts, None, (255, 0, 0), 4)
cv2.imshow("Coins1 orb", img4)

keypts = fast.detect(img_two, None)
img5 = cv2.drawKeypoints(img_two, keypts, None, (255, 0, 0), 4)
cv2.imshow("Coins1 fast", img5)

img_three = cv2.imread("TestImages/Coins2.jpg")

keypts, des = orb.detectAndCompute(img_three, None)

img6 = cv2.drawKeypoints(img_three, keypts, None, (255, 0, 0), 4)
cv2.imshow("Coins2 orb", img6)

keypts = fast.detect(img_three, None)
img7 = cv2.drawKeypoints(img_three, keypts, None, (255, 0, 0), 4)
cv2.imshow("Coins2 fast", img7)

cv2.waitKey(0)
cv2.destroyAllWindows()


vidCap = cv2.VideoCapture(0)
while True:
    x = cv2.waitKey(10)
    char = chr(x & 0xFF)
    if char == 'q':
        break

    ret, img = vidCap.read()

    keypts, des = orb.detectAndCompute(img, None)

    # img_orb = cv2.drawKeypoints(img, keypts, None, (255, 0, 0), 2)
    # cv2.imshow("cam orb", img_orb)

    keypts = fast.detect(img, None)
    img_fast = cv2.drawKeypoints(img, keypts, None, (255, 0, 0), 4)
    cv2.imshow("can fast", img_fast)


cv2.destroyAllWindows()
vidCap.release()
