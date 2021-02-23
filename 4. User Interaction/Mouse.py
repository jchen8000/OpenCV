import numpy as np
import cv2

#
# List all events support by cv2
#
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

img = cv2.imread("../res/flower003.jpg")
cv2.imshow("image", img)
cv2.setMouseCallback("image", mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()



#
# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, ", ", y)
#         font = cv2.FONT_HERSHEY_COMPLEX
#         strXY = str(x) + ", " + str(y)
#         cv2.circle(img, (x, y), 3, (255, 255, 0), -1)
#         cv2.putText(img, strXY, (x+5,y+5), font, .5, (255, 255, 0), 1)
#         cv2.imshow("image", img)
#     if event == cv2.EVENT_RBUTTONDOWN:
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]
#         font = cv2.FONT_HERSHEY_COMPLEX
#         strBGR = str(blue) + ", " + str(green) + ", " + str(red)
#         cv2.circle(img, (x, y), 3, (0, 255, 255), -1)
#         cv2.putText(img, strBGR, (x+5,y+5), font, .5, (0, 255, 255), 1)
#         cv2.imshow("image", img)
#
# #img = np.zeros( (512, 512, 3), np.uint8)
# img = cv2.imread("Resources/people-girl-design-happy-35188.jpg")
# cv2.imshow("image", img)
# cv2.setMouseCallback("image", click_event)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
#
#
# def click_event2(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
#         points.append((x, y))
#         if len(points) >= 2:
#             cv2.line(img, points[-1], points[-2], (255, 0, 0), 1)
#         cv2.imshow("image", img)
#
# img = np.zeros( (512, 512, 3), np.uint8)
# #img = cv2.imread("Resources/people-girl-design-happy-35188.jpg")
# cv2.imshow("image", img)
# points = []
# cv2.setMouseCallback("image", click_event2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
#
#
#


