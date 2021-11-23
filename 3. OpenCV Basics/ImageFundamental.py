import cv2
import numpy as np

#
# Load the image
#
img = cv2.imread("../res/flower003.jpg")
img = cv2.resize(img, (0,0), fx=0.6, fy=0.6)
print("BGR values on pixel at (100,100) are", img[100,100])
#
# Split image into BRG,
# Show Blue, Red, Green in colored space
#
blue = img.copy()
blue[:,:,1] = 0
blue[:,:,2] = 0

red = img.copy()
red[:,:,0] = 0
red[:,:,1] = 0

green = img.copy()
green[:,:,0] = 0
green[:,:,2] = 0

color_split = np.concatenate((blue,green,red),axis=1)

cv2.imshow("Color Image", img)
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)
cv2.imshow("Blue,Green,Red split", color_split)
cv2.waitKey(0)
cv2.destroyAllWindows()


#
# Split image into BRG,
# Show Blue, Red, Green in single channel as grayscale
#
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

bgr_split = np.concatenate((b,g,r),axis=1)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

cv2.imshow("Color Image", img)
cv2.imshow("Blue,Green,Red split", bgr_split)

cv2.waitKey(0)
cv2.destroyAllWindows()



#
# Split image into HSV,
#
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)

cv2.imshow("Hue", h)
cv2.imshow("Saturation", s)
cv2.imshow("Value", v)

cv2.imshow("Color Image", img)
cv2.imshow("Hue, Saturation and Value split",hsv_split)
cv2.waitKey(0)
cv2.destroyAllWindows()