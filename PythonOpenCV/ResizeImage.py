import cv2
import numpy as np

img = cv2.imread("Utils/ww3.jpg")
print(img.shape)

imgResize = cv2.resize(img, (480, 720)) # first is width then height

imgCrop = img[0:200, 200:500] # height is first then width
cv2.imshow("image", img)
cv2.imshow("ResizeImage", imgResize)
cv2.imshow("CropImage", imgCrop)


img1 = np.zeros((500, 500, 3), np.uint8)
#print(img1)
#img1[:] = 255, 0, 0 # : to apply to whole image, blue color

cv2.line(img1, (0, 0), (300, 300), (0, 255, 0), 3) # line whth dimensions
cv2.line(img1, (0, 0), (img1.shape[1], img1.shape[0]), (0, 255, 0), 3) # diagonal line
cv2.rectangle(img1, (0, 0), (200, 300), (0, 0, 255), 2)
cv2.circle(img1, (400, 50), 30, (255, 255, 0), 4)
cv2.putText(img1, "Dark Knight", (300, 200), cv2.FONT_ITALIC, 0.5, (0, 150, 100), 2)
cv2.imshow("blank", img1)

cv2.waitKey(0)