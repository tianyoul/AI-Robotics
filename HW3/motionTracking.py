'''This program uses a video feed input and determine regions of movement.
    It then creates contour boxes for such regions, and track them (look for movements in later frames)'''

import cv2
import numpy as np

# A function to decide if two contours are close enough
def find_if_close(cnt1,cnt2):
    row1,row2 = cnt1.shape[0],cnt2.shape[0]
    for i in range(row1):
        for j in range(row2):
            dist = np.linalg.norm(cnt1[i]-cnt2[j])
            if abs(dist) < 50 :
                return True
            elif i==row1-1 and j==row2-1:
                return False


vidCap = cv2.VideoCapture(0)
ret, prevImg = vidCap.read()

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(5)

while True:
    x = cv2.waitKey(10)
    char = chr(x & 0xFF)
    if char == 'q':
        break

    ret, img = vidCap.read()
    # # compute the difference between images
    # difference = cv2.absdiff(grayPrevImg, grayImg)
    # #cv2.imshow("Difference", difference)

    fgmask = fgbg.apply(img, learningRate = 0.05)
    # finding the contours
    ret, thresh = cv2.threshold(fgmask, 77, 255, 0)
    # was cv2.RETR_TREE and cv2.CHAIN_APPROX_SIMPLE
    conImg, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_areas = sorted(contours, key=cv2.contourArea, reverse=True)

    status = np.zeros((10, 1))
    for i,contour in enumerate(largest_areas[:10]):
        if status[i] == 0:
            #when it hasn't have any other contours to merge with before
            status[i] = i
        if i != 9:
            for j, nextContour in enumerate(largest_areas[i+1:10]):
                if status[j] == 0 and find_if_close(contour,nextContour):
                    status[j] = status[i]

    unified = []
    for i in range(1,10):
        pos = np.where(status == i)[0]
        if pos.size != 0:
            cont = np.vstack(largest_areas[i] for i in pos)
            hull = cv2.convexHull(cont)
            unified.append(hull)

    if len(unified)!=0:
        largest = sorted(unified, key=cv2.contourArea, reverse=True)
        x, y, w, h = cv2.boundingRect(largest[0])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Image", img)

vidCap.release()
cv2.destroyAllWindows()