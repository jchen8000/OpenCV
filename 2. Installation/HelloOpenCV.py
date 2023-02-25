import cv2
import numpy as np
print(cv2.__version__)

img = np.zeros((480,1000,3), np.uint8)
img[:] = 235,235,235

tx_start = (180,260)
tx_font = cv2.FONT_HERSHEY_COMPLEX
tx_color = (125, 0, 0)
tx_fontScale = 3
tx_thickness = 8
cv2.putText(img, "Hello OpenCV", tx_start, tx_font,
            tx_fontScale, tx_color, tx_thickness)
cv2.imshow("Hello OpenCV", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
