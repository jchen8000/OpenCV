import cv2
import numpy as np

img = np.zeros((320,640,3), np.uint8)
img[:] = 125,125,125

tx_start = (80,160)
tx_font = cv2.FONT_HERSHEY_COMPLEX
tx_color = (255, 255, 0)
tx_fontScale = 2
tx_thickness = 2
cv2.putText(img, "Hello OpenCV", tx_start, tx_font,
            tx_fontScale, tx_color, tx_thickness)

cv2.imshow("Hello", img)
cv2.waitKey(0)
cv2.destroyAllWindows()