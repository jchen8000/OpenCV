import cv2
import numpy as np

def draw_text(image, text, org,
              font_face=cv2.FONT_HERSHEY_COMPLEX,
              font_scale=1,
              color=(255,255,255),
              thickness=1,
              line_type=cv2.LINE_AA):
    cv2.putText(image, text, org, font_face,
                font_scale, color, thickness, line_type	)

canvas = np.zeros((180, 480, 3), np.uint8)
canvas[:] = 235,235,235

#Draw a text
draw_text(canvas, "Hello OPENCV", (50, 100),
          color=(125, 0, 0),
          font_scale=1.5,
          thickness=2)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

