import cv2
import numpy as np

def closest(l1, l2, l3):
    thre = 20
    if l1 > l2:
        if l1 > l3:
            if l1 > thre:
                return 1
        else:
            if l3 > thre:
                return 3
    else:
        if l2 > l3:
            if l2 > thre:
                return 2
        else:
            if l3 > thre:
                return 3

    return 0

dict = {}
dict[0] = 'none'
dict[1] = 'door'
dict[2] = 'exit'
dict[3] = 'hatch'

font = cv2.FONT_HERSHEY_SIMPLEX

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

def match_val(img1, img2):
    mat = cv2.matchTemplate(img1, img2, eval(methods[0]))
    return cv2.minMaxLoc(mat)[1]

orb = cv2.ORB_create()
bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
door = cv2.imread('words/door.jpg')
exit = cv2.imread('words/exit.jpg')
hatch = cv2.imread('words/hatch.jpg')


vidCap = cv2.VideoCapture(0)

kp1, des_door = orb.detectAndCompute(door, None)
kp2, des_exit = orb.detectAndCompute(exit, None)
kp3, des_hatch = orb.detectAndCompute(hatch, None)

while True:
    x = cv2.waitKey(10)
    char = chr(x & 0xFF)
    if char == 'q':
        break

    ret, img = vidCap.read()

    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lower_white = np.array([0, 0, 0])
    upper_white = np.array([50, 50, 50])
    mask = cv2.inRange(img, lower_white, upper_white)
    edges = cv2.Canny(mask, 100, 200)
    dilated_image = cv2.dilate(mask, np.ones((5, 3)), iterations=20)



    #edges = cv2.Canny(img, 100, 200)

    #dilated_image = cv2.dilate(edges, np.ones((5,3)), iterations=10)

    _, contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    borders = []
    area = edges.shape[0] * edges.shape[1]
    for i, c in enumerate(contours):
        x, y, w, h = cv2.boundingRect(c)
        if w * h > 0.05 * area:
            borders.append((i, x, y, x + w - 1, y + h - 1))
            cv2.rectangle(img, (x,y), (x + w - 1, y + h - 1), (100, 180, 50), 1)


    if len(borders) == 1:
        bd = borders[0]
        x1 = bd[1]
        y1 = bd[2]
        x2 = bd[3]
        y2 = bd[4]
        origPts = np.float32([[x1, y1], [x2, y1], [x1, y2]])
        newPts = np.float32([[0, 0], [800, 0], [0, 400]])
        mat = cv2.getAffineTransform(origPts, newPts)
        warpImg = cv2.warpAffine(img, mat, (800, 400))

        kp, des = orb.detectAndCompute(warpImg, None)
        matches_door = bfMatcher.match(des, des_door)
        matches_exit = bfMatcher.match(des, des_exit)
        matches_hatch = bfMatcher.match(des, des_hatch)

        #index = closest(len(matches_door),len(matches_exit),len(matches_hatch))
        #index = closest(np.sum(warpImg*door), np.sum(warpImg*exit), np.sum(warpImg*hatch))
        index = closest(match_val(door, warpImg), match_val(exit, warpImg), match_val(hatch, warpImg))
        cv2.putText(warpImg, dict[index], (5, 30), font, 1, (255, 255, 255), 3)
        cv2.imshow("Warped", warpImg)
        if char == 'c':
            cv2.imwrite('words/'+str(index)+'.jpg', warpImg)




    cv2.imshow("Cam", img)



cv2.destroyAllWindows()
vidCap.release()


