import cv2
import numpy as np
import stackImages as stack

def empty(a):
    pass


path = "Utils/pinkcar.jpg"

#create trackbar
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty) # in cv2 we have 180 values
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 84, 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 246, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 106, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


while True:
    img = cv2.imread(path)

    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, sat_min, sat_max, val_min, val_max)
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("Image", img)
    # cv2.imshow("HSV", imgHsv)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("ResultImage", imgResult)

    imgStack = stack.stackImages(0.6, ([img, imgHsv], [mask, imgResult]))
    cv2.imshow("Stacked images", imgStack)

    cv2.waitKey(1)