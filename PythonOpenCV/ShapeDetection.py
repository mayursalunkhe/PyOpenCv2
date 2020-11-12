import cv2
import numpy as np
import stackImages as stack


path = 'Utils/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# Detect edges
imgCanny = cv2.Canny(imgBlur, 50, 50)

stack.getContours(imgCanny, imgContour)
imgBlank = np.zeros_like(img)
imgStack = stack.stackImages(0.6, ([img, imgGray, imgBlur],
                                   [imgCanny, imgContour, imgBlank]))

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)