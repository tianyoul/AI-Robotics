import cv2
import numpy

#Sobel Gradient-Finding
# img = cv2.imread("TestImages/shops.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Compute gradient in horizontal direction (detects vertical edges)
# sobelValsHorz = cv2.Sobel(gray, -1, 1, 0)
# horzImg = cv2.convertScaleAbs(sobelValsHorz)
# cv2.imshow("horizontal gradient", horzImg)
# cv2.waitKey(0)
#
# # Compute gradient in vertical direction (Detects horizontal edges)
# sobelValsVerts = cv2.Sobel(gray, -1, 0, 1) #cv2.CV_32F
# vertImg = cv2.convertScaleAbs(sobelValsVerts)
# cv2.imshow("vertical gradient", vertImg)
# cv2.waitKey(0)
#
# # Compute gradient in horizontal direction (detects vertical edges)
# sobelValsHorz32f = cv2.Sobel(gray, cv2.CV_32F, 1, 0)
# horzImg1 = cv2.convertScaleAbs(sobelValsHorz32f)
# cv2.imshow("horizontal gradient 32f", horzImg1)
# cv2.waitKey(0)
#
# # Compute gradient in vertical direction (Detects horizontal edges)
# sobelValsVerts32f = cv2.Sobel(gray, cv2.CV_32F, 0, 1) #cv2.CV_32F
# vertImg1 = cv2.convertScaleAbs(sobelValsVerts32f)
# cv2.imshow("vertical gradient 32f", vertImg1)
# cv2.waitKey(0)
#
# # Combine the two gradients
# sobelComb = cv2.addWeighted(sobelValsHorz, 0.5,
#                             sobelValsVerts, 0.5, 0)
# # Convert back to uint8
# sobelImg = cv2.convertScaleAbs(sobelComb)
# cv2.imshow("Sobel", sobelImg)
# cv2.waitKey(0)


#Canny Edge Detection
# img = cv2.imread("TestImages/shops.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# cannyImg = cv2.Canny(gray, 100, 200)
# cv2.imshow("Canny", cannyImg)
# cv2.waitKey(0)

#Hough Lines
# img1 = cv2.imread("TestImages/Puzzle1.jpg")
# grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# cannyImg = cv2.Canny(grayImg, 100, 200)
# lines = cv2.HoughLinesP(cannyImg, 1, numpy.pi/180,
#                         threshold = 5,
#                         minLineLength = 20, maxLineGap = 10)
# for lineSet in lines:
#     for line in lineSet:
#         cv2.line(img1, (line[0], line[1]), (line[2], line[3]),
#                  (255, 255, 0))
# cv2.imshow("HoughLines", img1)
# cv2.waitKey(0)

#Milestone 2: Experimenting with Canny and Hough Functions
"""Program that operates on the built-in camera images.
It should display two images: the result of canny edge detection and the result of the probabilistic Hough Lines algorithm.
Try changing the parameters to see how that affects the resulting line-finding.
"""
vidCap = cv2.VideoCapture(0)
while True:
    x = cv2.waitKey(10)
    char = chr(x & 0xFF)
    if char == 'q':
        break

    ret, img = vidCap.read()

    #canny edge detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cannyImg = cv2.Canny(gray, 200, 200)
    cv2.imshow("canny", cannyImg)

    #Hough Lines
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cannyImg = cv2.Canny(grayImg, 200, 200)
    lines = cv2.HoughLinesP(cannyImg, 1, numpy.pi/180,
                            threshold = 5,
                            minLineLength = 20, maxLineGap = 10)
    for lineSet in lines:
        for line in lineSet:
            cv2.line(img, (line[0], line[1]), (line[2], line[3]),
                     (255, 255, 0))
    cv2.imshow("HoughLines", img)

cv2.destroyAllWindows()
vidCap.release()