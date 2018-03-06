import cv2
import os
from os import listdir

#Phase 1
# img1 = cv2.imread("TestImages/SnowLeo1.jpg")
# cv2.imshow("slide", img1)
# cv2.waitKey(0)
# img2 = cv2.imread("TestImages/frankenstein.jpg")
# cv2.imshow("slide", img2)
# cv2.waitKey(0)
# img3 = cv2.imread("TestImages/fallWoods.jpg")
# cv2.imshow("slide", img3)
# cv2.waitKey(0)
# img4 = cv2.imread("TestImages/garden.jpg")
# cv2.imshow("slide", img4)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


#Phase 2

files = []
for file in os.listdir("TestImages"):
    if file.endswith(".jpg"):
        files.append(file)


for file in files:
    img = cv2.imread("TestImages/" + file)
    cv2.imshow(file, img)
    cv2.waitKey(0)



