import numpy as np
import cv2
import common.Draw as dw

drawing = False
final_color = (255, 255, 255)
drawing_color = (125, 125, 125)
pts = []

def on_mouse(event, x, y, flags, param):
    global pts, drawing, img, img_bk
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        add_point(pts, (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = img_bk.copy()
            draw_polygon(img, pts, (x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        add_point(pts, (x, y), True)
        draw_polygon(img, pts, (x, y), True)
        drawing = False
        pts.clear()
        img_bk = img.copy()

def add_point(points, curt_pt, is_final=False):
    print("Adding point #%d with position(%d,%d)"
          % (len(points), curt_pt[0], curt_pt[1]))
    points.append(curt_pt)
    if is_final == True:
        print("Completing polygon with %d points." % len(pts))

def draw_polygon(img, points, curt_pt, is_final=False):
    if (len(points) > 0):
        if is_final == False:
            dw.draw_polylines(img, np.array([points]), False, final_color)
            dw.draw_line(img, points[-1], curt_pt, drawing_color)
        else:
            dw.draw_polylines(img, np.array([points]), True, final_color)
        for point in points:
            dw.draw_circle(img, point, 2, final_color, 2)
            dw.draw_text(img, str(point), point, color=final_color, font_scale=0.5)

def print_instruction(img):
    txtInstruction = "Left key to add a point, right key to finish a polygon. ESC to exit."
    dw.draw_text(img,txtInstruction, (10, 20), 0.5, (255, 255, 255))
    print(txtInstruction)

def main():
    global img, img_bk
    windowName = 'Mouse Drawing Polygon'
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