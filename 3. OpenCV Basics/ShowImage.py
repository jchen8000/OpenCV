import cv2

img = cv2.imread("../res/flower004.jpg")
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
