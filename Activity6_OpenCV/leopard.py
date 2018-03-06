import cv2
import numpy

img = cv2.imread("TestImages/SnowLeo2.jpg")
print(img.shape)
cv2.circle(img, (120, 140), 80, (180, 60, 150), 5)
cv2.rectangle(img, (250, 100), (550, 300), (100, 180, 50), -1)
cv2.ellipse(img, (130, 350), (100, 60), 0, 30, 120, (250, 240, 110), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "SnowLeo2.jpg", (5, 30), font, 1, (255,255,255), 3)

cv2.imshow("Leopard", img)

cv2.imwrite("leopard.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
