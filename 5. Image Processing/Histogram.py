import cv2
import numpy as np
from matplotlib import pyplot as plt


img = np.zeros((200, 200), np.uint8)
cv2.rectangle(img, (0,100), (200, 200), (255), -1)
cv2.rectangle(img, (0,50), (100, 100), (100), -1)
cv2.imshow("Image", img)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


# read a picture in gray mode
imgGray = cv2.imread("../res/flower003.jpg", 0 )
cv2.imshow("Image", imgGray)
plt.hist(imgGray.ravel(), 256, [0, 256])
print("Showing histogram using plt.hist")
plt.show()

hist = cv2.calcHist([imgGray], [0], None, [256], [0, 256])
print("Showing histogram using cv2.calcHist")
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()



# read a picture in color mode
# then split it into b, g, r
# and show histgram for each
img = cv2.imread("../res/flower003.jpg" )
b, g, r = cv2.split(img)
cv2.imshow("Image", img)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
print("Showing histogram of color picture in B, G, R channel")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()




