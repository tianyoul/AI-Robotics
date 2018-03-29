import numpy as np
import cv2

def getNextFrame(vidObj):
    """Takes in the VideoCapture object and reads the next frame, returning one that is half the size 
    (Comment out that line if you want fullsize)."""
    ret, frame = vidObj.read()
    # print(type(vidObj), type(frame))
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    return frame

def show_hist(hist):
    """Takes in the histogram, and displays it in the hist window."""
    bin_count = hist.shape[0]
    bin_w = 24
    img = np.zeros((256, bin_count * bin_w, 3), np.uint8)
    for i in range(bin_count):
        h = int(hist[i])
        cv2.rectangle(img, (i * bin_w + 2, 255), ((i + 1) * bin_w - 2, 255 - h), (int(180.0 * i / bin_count), 255, 255),
                      -1)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow('hist', img)

cam = cv2.VideoCapture(0)
ret, frame = cam.read()
frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)
cv2.namedWindow('camshift')
cv2.namedWindow('hist')
cv2.moveWindow('hist', 700, 100)

while True:
    frame = getNextFrame(cam)
    vis = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array((0., 60., 32.)),
                       np.array((180., 255., 255.)))

    green_roi = cv2.imread("/Users/jin/PycharmProjects/AI-Robotics/HW3/predeterminedGreen.png")
    hsv_roi = cv2.cvtColor(green_roi, cv2.COLOR_BGR2HSV)
    mask_roi = cv2.inRange(hsv_roi, np.array((0., 60., 32.)),
                       np.array((180., 255., 255.)))

    hist=cv2.calcHist([hsv_roi], [0], mask_roi, [16], [0, 180])
    cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
    hist = hist.reshape(-1)
    show_hist(hist)

    prob = cv2.calcBackProject([hsv], [0], hist, [0, 180], 1)
    prob &= mask
    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    track_window = (0, 0, 800, 800)
    track_box, track_window = cv2.CamShift(prob, track_window, term_crit)

    if track_box[0][0]-5 > 0:
        upperLeft_x = track_box[0][0]-5
    else:
        upperLeft_x = 0
    if track_box[0][1]-5 > 0:
        upperLeft_y = track_box[0][1]-5
    else:
        upperLeft_y = 0

    try:
        cv2.ellipse(vis, track_box, (0, 0, 255), 1)
        cv2.rectangle(vis, (upperLeft_x, upperLeft_y),
                      (track_box[0][0] + 5, track_box[0][1] + 5), (0, 255, 0))
        # cv2.rectangle(img, pt1, pt2, col)
        # cv2.rectangle(draw1, (10, 100), (100, 10), (0, 180, 0), -1)
        # cv2.ellipse(img, pt, axes, angle, startAng, endAng, col)
        # cv2.ellipse(draw1, (250, 150), (100, 60), 30, 0, 220, (250, 180, 110), -1)
    except:
        print(track_box)

    cv2.imshow('camshift', vis)

    ch = 0xFF & cv2.waitKey(5)
    if ch == 27:
        break

cv2.destroyAllWindows()