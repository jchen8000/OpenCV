import cv2

#
# Load the image
#
img = cv2.imread("../res/flower003.jpg")
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

blue = img.copy()
blue[:,:,1] = 0
blue[:,:,2] = 0

red = img.copy()
red[:,:,0] = 0
red[:,:,1] = 0

green = img.copy()
green[:,:,0] = 0
green[:,:,2] = 0

cv2.imshow("Image", img)


b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

cv2.imshow("Image", img)
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imshow("Image", img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
