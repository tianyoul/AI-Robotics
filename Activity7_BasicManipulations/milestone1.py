import cv2
import numpy
from random import shuffle

def shuffle_channel(img):
    (bc, gc, rc) = cv2.split(img)

    lst = [bc, gc, rc]
    shuffle(lst)
    resultImg = cv2.merge((lst[0], lst[1], lst[2]))

    cv2.imshow("shuffle channel",resultImg)
    cv2.waitKey(0)

image = cv2.imread("TestImages/shops.jpg")
cv2.imshow("original",image)
cv2.waitKey(0)

shuffle_channel(image)