import cv2

#
# Load the image
#
img = cv2.imread("../res/flower004.jpg")
# percent = 65
# width = int(img.shape[1] * percent / 100)
# height = int(img.shape[0] * percent / 100)
# img = cv2.resize(img, (width, height))
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#
# Load the image in grayscale mode
#
img = cv2.imread("../res/flower004.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()




#
# Load the image in original color mode
# and then covert it to grayscale
#
img = cv2.imread("../res/flower004.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.imshow("Image Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()