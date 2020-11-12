import cv2
frameWidth = 640
frameHeight = 480

#For webcam feed
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)     # Widht has id 3
cap.set(4, frameHeight)     # Height has id 4
cap.set(10, 150)    # brightness has id 10


faceCascade = cv2.CascadeClassifier("Utils/haarcascade_frontalface_default.xml")
# img = cv2.imread('Utils/ww3.jpg')
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGrey, 1.1, 4)
#
# #Create bounding box around detected faces
# for x, y, w, h in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

while True:
    success, img = cap.read()
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGrey, 1.1, 4)

    # Create bounding box around detected faces
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
