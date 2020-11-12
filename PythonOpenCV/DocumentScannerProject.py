import cv2
import numpy as np

widthImg = 640
heightImg = 480

#For webcam feed
cap = cv2.VideoCapture(0)
cap.set(3, widthImg)     # Widht has id 3
cap.set(4, heightImg)     # Height has id 4
cap.set(10, 150)    # brightness has id 10


def preProcessing(img):
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrey, (5,5),1)
    imgCanny = cv2.Canny(imgBlur, 100,100)
    # for thin edges we first make dilation and erosion
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)

    return imgThres



while True:
    success, img = cap.read()
    img = cv2.resize(img, (widthImg, heightImg))
    imgThres = preProcessing(img)
    cv2.imshow("Result", imgThres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
