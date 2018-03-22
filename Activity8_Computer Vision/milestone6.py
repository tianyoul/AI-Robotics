import cv2
# Some versions of OpenCV need this to fix a bug
cv2.ocl.setUseOpenCL(False)

img1 = cv2.imread("TestImages/fistq.jpg")

orb = cv2.ORB_create()
bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

kp1, des1 = orb.detectAndCompute(img1, None)

vidCap = cv2.VideoCapture(0)
while True:
    x = cv2.waitKey(10)
    char = chr(x & 0xFF)
    if char == 'q':
        break

    ret, img2 = vidCap.read()

    kp2, des2 = orb.detectAndCompute(img2, None)

    matches = bfMatcher.match(des1, des2)
    matches.sort(key=lambda x: x.distance)  # sort by distance

    # draw matches with distance less than threshold
    for i in range(len(matches)):
        if matches[i].distance > 50.0:
            break
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:i], None)
    cv2.imshow("Matches", img3)

cv2.destroyAllWindows()
vidCap.release()


