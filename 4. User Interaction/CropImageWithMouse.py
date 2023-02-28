import cv2
import common.Draw as dw

drawing = False
final_color = (255, 255, 255)
drawing_color = (238, 238, 238)
pt_first = (0, 0)
pt_second = (0, 0)

def on_mouse(event, x, y, flags, param):
    global pt_first, pt_second, drawing, img, img_bk, img_original
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt_first = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = img_bk.copy()
            draw_rectangle(img, pt_first, (x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        pt_second = (x, y)
        draw_rectangle(img, pt_first, pt_second, True)
        crop_image(img_original, pt_first, pt_second)

def crop_image(img, pt_first, pt_second):
    x_tl, y_tl = pt_first               # top-left point
    x_br, y_br = pt_second              # bottom-right point
    if x_br < x_tl:                     # swap x value if opposite
        x_br, x_tl = x_tl, x_br
    if y_br < y_tl:                     # swap y value if opposite
        y_br, y_tl = y_tl, y_br
    cropped_image = img[y_tl:y_br, x_tl:x_br]
    cv2.imshow("Cropped Image", cropped_image)

def draw_rectangle(img, point1, point2, is_final=False):
    if is_final == False:
        dw.draw_rectangle(img, point1, point2, drawing_color)
        dw.draw_text(img, str(point1), point1, color=drawing_color, font_scale=0.5)
        dw.draw_text(img, str(point2), point2, color=final_color, font_scale=0.5)
    else:
        dw.draw_rectangle(img, point1, point2, final_color, thickness=2)
        dw.draw_text(img, str(point1), point1, color=final_color, font_scale=0.5)
        dw.draw_text(img, str(point2), point2, color=final_color, font_scale=0.5)

def print_instruction(img):
    txtInstruction = "Press left button to drag a rectangle, release it to crop. ESC to exit."
    dw.draw_text(img,txtInstruction, (10, 20), 0.5, (0, 0, 0))
    print(txtInstruction)

def main():
    global img, img_bk, img_original
    windowName = 'Crop an Image'
    img = cv2.imread("../res/flower003.jpg")
    img_original = img.copy()
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