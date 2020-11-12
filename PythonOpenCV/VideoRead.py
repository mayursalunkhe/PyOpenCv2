import cv2


#For video file
cap = cv2.VideoCapture("Utils/testvideo.mp4")

#For webcam feed
cap = cv2.VideoCapture(0)
cap.set(3, 640)     # Widht has id 3
cap.set(4, 480)     # Height has id 4
cap.set(10, 100)    # brightness has id 10

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
