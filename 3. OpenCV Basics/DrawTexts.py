import cv2
import numpy as np

# create an image from numpy array
img = np.zeros((512,512,3), np.uint8)
# color the image
img[:] = 235,235,235

tx_start = (50,400)
tx_font = cv2.FONT_HERSHEY_COMPLEX
tx_color = (0, 0, 0)
tx_fontScale = 1
tx_thickness = 1
cv2.putText(img, "OPENCV Example", tx_start, tx_font, tx_fontScale, tx_color, tx_thickness)

cv2.imshow("Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()