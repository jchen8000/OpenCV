import cv2
import numpy as np

# create an image from numpy array
img = np.zeros((512,512,3), np.uint8)
# color the image
img[:] = 235,235,235

ln_start = (10,10)
ln_end = (img.shape[1], img.shape[0])
ln_color = (0, 255, 128)
cv2.line(img, ln_start, ln_end, ln_color, 3)

rt_topleft = (100,100)
rt_rightbottom =(250, 350)
rt_color = (200, 120, 35)
rt_weight = 5
#rt_weight = cv2.FILLED
cv2.rectangle(img, rt_topleft, rt_rightbottom, rt_color, rt_weight)

cl_center = (300,200)
cl_radius = 50
cl_color = (123, 95,232)
cl_weight = 3
cl_weight = cv2.FILLED
cv2.circle(img, cl_center, cl_radius, cl_color, cl_weight)

cv2.imshow("Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()