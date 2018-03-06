import cv2
import numpy

canvas = 255 * numpy.ones((500, 500, 3), numpy.uint8)
cv2.rectangle(canvas, (10, 100), (100, 10), (240, 180, 50))
cv2.rectangle(canvas, (110, 100), (200, 10), (100, 180, 50), -1)
cv2.circle(canvas, (260, 60), 50, (10, 10, 70))
cv2.circle(canvas, (380, 60), 50, (10, 80, 150), -1)
cv2.ellipse(canvas, (250, 250), (80, 40), 30, 0, 360, (250, 180, 110), -1)
cv2.ellipse(canvas, (100, 170), (70, 80), 30, 0, 150, (250, 240, 110))
cv2.imwrite("drawings.jpg", canvas)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
