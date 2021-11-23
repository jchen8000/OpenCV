import cv2
import numpy as np
import common.Draw as dw

def draw_opencv_icon(image):
    axes = (100, 100)
    center_top_circle = (320, 140)
    center_lowerleft_circle = (center_top_circle[0]-160,
                               center_top_circle[1]+240)
    center_lowerright_circle = (center_top_circle[0]+160,
                                center_top_circle[1]+240)
    angle_top_circle = 90
    angle_lowerleft_circle = -45
    angle_lowerright_circle = -90
    start_angle = 40
    end_angle = 320
    dw.draw_ellipse(image, center_top_circle, axes,
                 angle_top_circle, start_angle, end_angle,
                 color=(0, 0, 255),
                 thickness=80)
    dw.draw_ellipse(image, center_lowerleft_circle, axes,
                 angle_lowerleft_circle, start_angle, end_angle,
                 color=(0, 255, 0),
                 thickness=80)
    dw.draw_ellipse(image, center_lowerright_circle, axes,
                 angle_lowerright_circle, start_angle, end_angle,
                 color=(255, 0, 0),
                 thickness=80)
    dw.draw_text(image, "OpenCV", (20,660), color=(0,0,0),
                 font_scale=4.8, thickness=15)


if __name__ == '__main__':
    # create an image from numpy array
    canvas = np.zeros((480, 980, 3), np.uint8)
    canvas[:] = 235, 235, 235

    dw.draw_text(canvas, "Hello OpenCV", (150,260),
                 color=(125,0,0),
                 thickness=8, font_scale=3)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    canvas = np.zeros((720,640,3), np.uint8)
    canvas[:] = 235,235,235
    draw_opencv_icon(canvas)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()