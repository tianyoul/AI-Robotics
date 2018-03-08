import cv2

vidCap = cv2.VideoCapture(0)
for i in range(300):
    ret, img = vidCap.read()
    cv2.imshow("Webcam", img)
    cv2.waitKey(10)   # Waiting may be needed for window updating

cv2.destroyAllWindows()
vidCap.release()
