# This script blend two images and the user can change the weighting values by pressing different keys
import cv2
import numpy

image1 = cv2.imread("TestImages/beachBahamas.jpg")
image2 = cv2.imread("TestImages/fallWoods.jpg")
height, width = image1.shape[:2]
img2 = cv2.resize(image2, (width, height))
x = cv2.waitKey(10)
char = chr(x & 0xFF)
scale1 = 0.5
scale2 = 0.5
newImage = cv2.addWeighted(image1, scale1, img2, scale2, 0)
cv2.imshow("new", newImage)

while char != 'q':
    x = cv2.waitKey(10)
    char = chr(x & 0xFF)
    if char == 'w':
        scale1 += 0.1
        scale2 -= 0.1
    if char == 's':
        scale1 -= 0.1
        scale2 += 0.1
    if scale1 <= 1.0 and scale2 <= 1.0:
        newImage = cv2.addWeighted(image1, scale1, img2, scale2, 0)

    cv2.imshow("new", newImage)

cv2.destroyAllWindows()