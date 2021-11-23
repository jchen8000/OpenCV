import numpy as np
import cv2

#
# List all events support by cv2
#
def list_event():
    for event in dir(cv2):
        if "EVENT" in event:
            print(event)

#
# Display coordinates and color RGB value on a separate window
# when mouse clicked on the image
#
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        mycolorImage = np.zeros((100, 280, 3), np.uint8)
        mycolorImage[:] = [blue, green, red]
        strBGR = "(B,G,R) = (" + str(blue) + ", " + str(green) + ", " + str(red) + ")"
        strXY = "(X,Y) = (" + str(x) + ", " + str(y) + ")"
        txtFont = cv2.FONT_HERSHEY_COMPLEX
        txtColor = (255, 255, 255)
        cv2.putText(mycolorImage, strXY, (10, 30), txtFont, .6, txtColor, 1)
        cv2.putText(mycolorImage, strBGR, (10, 50), txtFont, .6, txtColor, 1)
        cv2.imshow("color", mycolorImage)

if __name__ == '__main__':
    list_event()

    img = cv2.imread("../res/flower003.jpg")
    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouse_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


