import cv2
import numpy as np

img = cv2.imread("Utils/ww3.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (5, 5), 0)
imgCanny = cv2.Canny(img, 100, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("GreyScaleImage", imgGrey)
cv2.imshow("BlurImage", imgBlur)
cv2.imshow("CannyImage", imgCanny)
cv2.imshow("DialationImage", imgDialation)
cv2.imshow("ErodeImage", imgErode)
cv2.waitKey(0)
