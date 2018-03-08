import cv2
import numpy

image = cv2.imread("TestImages/DollarCoin.jpg")
cv2.imshow("Original Image", image)
cv2.waitKey(0)

#Returns a new image that is 100 x 100 pixels, a stretched version of the original
resized = cv2.resize(image, (100, 100))
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)

#Returns a new image that is twice the size of the original, same aspect ratio
resized = cv2.resize(image, (0, 0), fx = 2, fy = 2)
cv2.imshow("same ratio Image", resized)
cv2.waitKey(0)

#Returns a new image whose columns have been squashed to half the original
resized = cv2.resize(image, (0, 0), fx = 0.5, fy = 1.0)
cv2.imshow("squashed to half Image", resized)
cv2.waitKey(0)