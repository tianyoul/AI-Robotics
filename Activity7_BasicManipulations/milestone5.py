import cv2
import numpy as np

vidCap = cv2.VideoCapture(0)
while True:
    x = cv2.waitKey(10)
    char = chr(x & 0xFF)
    if char == 'q':
        break

    ret, img = vidCap.read()
    #mirror image
    flipimg = cv2.flip(img, 1)

    #blending of the original and mirrored version
    newImage = cv2.addWeighted(img, 0.5, flipimg, 0.5, 0)

    #top hat effect
    kernel = np.ones((50, 50), np.uint8)
    gradient = cv2.morphologyEx(newImage, cv2.MORPH_TOPHAT, kernel)

    cv2.imshow("Webcam", gradient)


cv2.destroyAllWindows()
vidCap.release()