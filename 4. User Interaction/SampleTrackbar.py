import cv2
import numpy as np
def on_trackbar(val):
    print("Trackbar value:", val)

cv2.namedWindow("Trackbar Window")
cv2.createTrackbar("Trackbar", "Trackbar Window", 0, 100, on_trackbar)
canvas = np.zeros((100, 800, 3), np.uint8)
canvas[:] = 235,235,235

while True:
    cv2.imshow("Trackbar Window", canvas)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()