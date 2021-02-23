import cv2
import numpy as np
import common.Draw as dw

def draw_opencv_icon(image):
    axes = (50, 50)
    center_top_circle = (160, 70)
    center_lowerleft_circle = (center_top_circle[0]-80,
                               center_top_circle[1]+120)
    center_lowerright_circle = (center_top_circle[0]+80,
                                center_top_circle[1]+120)
    angle_top_circle = 90
    angle_lowerleft_circle = -45
    angle_lowerright_circle = -90
    start_angle = 40
    end_angle = 320
    dw.draw_ellipse(image, center_top_circle, axes,
                 angle_top_circle, start_angle, end_angle,
                 color=(0, 0, 255),
                 thickness=40)
    dw.draw_ellipse(image, center_lowerleft_circle, axes,
                 angle_lowerleft_circle, start_angle, end_angle,
                 color=(0, 255, 0),
                 thickness=40)
    dw.draw_ellipse(image, center_lowerright_circle, axes,
                 angle_lowerright_circle, start_angle, end_angle,
                 color=(255, 0, 0),
                 thickness=40)
    dw.draw_text(image, "OpenCV", (10,330), color=(0,0,0),
                 font_scale=2.4, thickness=5)


if __name__ == '__main__':
    # create an image from numpy array
    canvas = np.zeros((180,320,3), np.uint8)
    canvas[:] = 235,235,235

    dw.draw_text(canvas, "Hello OPENCV", (50,100), color=(125,0,0))
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    canvas = np.zeros((360,320,3), np.uint8)
    canvas[:] = 235,235,235
    draw_opencv_icon(canvas)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()