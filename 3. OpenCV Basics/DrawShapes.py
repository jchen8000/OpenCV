import cv2
import numpy as np
import common.Draw as dw


if __name__ == '__main__':
    # create a canvas from numpy array
    canvas = np.zeros((380, 480, 3), np.uint8)
    cv2.imshow("Canvas", canvas)
    print("Press any key to continue...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # paint the canvas with a color
    canvas[:] = 235, 235, 235
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Draw a line
    dw.draw_line(canvas, start=(100,100), end=(canvas.shape[1]-100, canvas.shape[0]-100), color=(10,10,10), thickness=10 )
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Draw rectangles
    dw.draw_rectangle(canvas, (200,50), (400, 20), color=(255, 255, 0), thickness=2)
    dw.draw_rectangle(canvas, (20,220), (200, 320), color=(255, 135, 135), thickness=cv2.FILLED)

    #Draw circles
    dw.draw_circle(canvas, center=(280, 120), radius=50, color=(85, 130, 255), thickness=cv2.FILLED)
    dw.draw_circle(canvas, center=(380, 160), radius=80, color=(180, 30, 175), thickness=5)

    #Draw ellipses
    dw.draw_ellipse(canvas, center=(230,280), axes=(60,80), angle=0, start_angle=0, end_angle=360, color=(123,223,210), thickness=cv2.FILLED)

    pts = np.array([[25, 70], [25, 160],
                    [110, 200], [220, 140],
                    [200, 70], [110, 20]], np.int32)
    pts = pts.reshape((-1,1,2))
    dw.draw_polylines(canvas, [pts], color=(23,23,10))

    cv2.imshow("Canvas", canvas)

    cv2.waitKey(0)
    cv2.destroyAllWindows()





