import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

#For webcam feed
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)     # Widht has id 3
cap.set(4, frameHeight)     # Height has id 4
cap.set(10, 150)    # brightness has id 10

myColors = [[105,119,39,179,255,255], # Purple
            [0,136,67,7,255,152], # Red
            [76,106,75,169,255,255]] # Teal

myColorValues = [[255,102,178],
                 [0,0,153],
                 [153,153,0]]

myPoints = []#[x, y, colorId]
def findColor(img, myColors, myColorValues):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHsv, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorValues[count], cv2.FILLED)
        if x!=0 and y!= 0:
            newPoints.append([x, y, count])
        count += 1
        #cv2.imshow(str(color[0]), mask)
    return newPoints


def getContours(img):
    #cv2.RETR_EXTERNAL will retrive extreame outer contours
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        # get minimum area so it does not detect any noise
        if area > 500:
            # every contour from cnt is highlighted as blue border on on imgContour
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            # perimeter so will help to approximate corners of our shapes
            peri = cv2.arcLength(cnt, True)
            # approximate corner points- number of corners
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # True - shapes are closed so true, 0.02 - resulution
            # create bounding box around detecting object
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints)!= 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
