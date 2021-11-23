import cv2
import numpy as np
import common.Draw as dw
import common.ImageProcessing as ip

drawing = False
final_color = (0, 0, 255)
drawing_color = (0, 0, 125)
width, height = 320, 480
points = []

def on_mouse(event, x, y, flags, param):
    global points, drawing, img, img_bk, iproc, warped_image
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        add_point(points, (x, y))
        if len(points) == 4:
            draw_polygon(img, points, (x, y), True)
            drawing = False
            img_bk = iproc.copy()
            warped_image = iproc.perspective_warp(points, width, height)
            points.clear()
            iproc.show("Perspective Warping", image=warped_image)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = img_bk.copy()
            draw_polygon(img, points, (x, y))

def add_point(points, curt_pt):
    print("Adding point #%d with position(%d,%d)"
          % (len(points), curt_pt[0], curt_pt[1]))
    points.append(curt_pt)

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
    txtInstruction = "Left click to specify four points to warp image. ESC to exit, 's' to save"
    dw.draw_text(img,txtInstruction, (10, 20), 0.5, (255, 255, 255))
    print(txtInstruction)


if __name__ == "__main__":
    global img, img_bk, iproc, warped_image

    title = "Original Image"
    iproc = ip.ImageProcessing(title, "../res/skewed_image001.jpg")
    img = iproc.image
    print_instruction(img)
    img_bk = iproc.copy()
    cv2.setMouseCallback(title, on_mouse)
    iproc.show()

    while True:
        iproc.show(image=img)
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:
            break
        elif ch == ord('s'):
            # press 's' key to save image
            filepath = "C:/temp/warp_image.png"
            cv2.imwrite(filepath, warped_image)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()



