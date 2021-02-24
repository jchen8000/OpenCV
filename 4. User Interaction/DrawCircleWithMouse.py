import cv2
import numpy as np
import math
import common.Draw as dw

drawing = False
final_color = (255, 255, 255)
drawing_color = (125, 125, 125)

def on_mouse(event, x, y, flags, param):
    global drawing, ctr, radius, img, img_bk
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ctr = x, y
        radius = 0
        draw_circle(img, ctr, radius, drawing_color)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = img_bk.copy()
            radius = calc_radius(ctr, (x,y))
            draw_circle(img, ctr, radius, drawing_color)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        radius = calc_radius(ctr, (x,y))
        draw_circle(img, ctr, radius, final_color, 2, True)
        img_bk = img.copy()

def calc_radius(center, current_point):
    cx, cy = current_point
    tx, ty = center
    return int(math.hypot(cx - tx, cy - ty))

def draw_circle(img, center, r, color, line_scale=1, is_final=False ):
    txtCenter = "ctr=(%d,%d)" % center
    txtRadius = "r=%d" % radius
    if is_final == True:
        print("Completing circle with %s and %s" % (txtCenter, txtRadius))
    dw.draw_circle(img, center, 1, color, line_scale)   # draw center point
    dw.draw_circle(img, center, r, color, line_scale)   # draw circle
    dw.draw_text(img, txtCenter, (center[0]-60, center[1]+20), 0.5, color)
    dw.draw_text(img, txtRadius, (center[0]-15, center[1]+35), 0.5, color)

def print_instruction(img):
    txtInstruction = "Press and hold left key to draw a circle. ESC to exit."
    dw.draw_text(img,txtInstruction, (10, 20), 0.5, (255, 255, 255))
    print(txtInstruction)

def main():
    global img, img_bk
    windowName = 'Mouse Drawing Circles'
    img = np.zeros((500, 640, 3), np.uint8)
    print_instruction(img)
    img_bk = img.copy()
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, on_mouse)
    while (True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()