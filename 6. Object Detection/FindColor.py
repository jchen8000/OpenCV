import cv2
import numpy as np

def empty(a):
    pass

def find_color():
    cv2.namedWindow("Hue Sat Val")
    cv2.resizeWindow("TrackBars", 640, 240)
    cv2.createTrackbar("Hue Min", "Hue Sat Val", 165, 179, empty)
    cv2.createTrackbar("Hue Max", "Hue Sat Val", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "Hue Sat Val", 100, 255, empty)
    cv2.createTrackbar("Sat Max", "Hue Sat Val", 255, 255, empty)
    cv2.createTrackbar("Val Min", "Hue Sat Val", 100, 255, empty)
    cv2.createTrackbar("Val Max", "Hue Sat Val", 255, 255, empty)

    img = cv2.imread("../res/RGB_color_wheel.png")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("Original", img)

    while True:
        h_min = cv2.getTrackbarPos("Hue Min", "Hue Sat Val")
        h_max = cv2.getTrackbarPos("Hue Max", "Hue Sat Val")
        s_min = cv2.getTrackbarPos("Sat Min", "Hue Sat Val")
        s_max = cv2.getTrackbarPos("Sat Max", "Hue Sat Val")
        v_min = cv2.getTrackbarPos("Val Min", "Hue Sat Val")
        v_max = cv2.getTrackbarPos("Val Max", "Hue Sat Val")
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        imgResult = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Mask", mask)
        cv2.imshow("Color Found", imgResult)
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:  # Press 'ESC' to exit
            break
    cv2.destroyAllWindows()


def find_color2():
    img = cv2.imread("../res/flower002.jpg")
    cv2.imshow("Original", img)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(imgHSV, (161,100,100), (179,255,255))
    result1 = cv2.bitwise_and(img, img, mask=mask1 )
    cv2.imshow("Mask1", mask1)
    cv2.imshow("Result1", result1)

    mask2 = cv2.inRange(imgHSV, (0, 100, 100), (6, 255, 255))
    result2 = cv2.bitwise_and(img, img, mask=mask2 )
    cv2.imshow("Mask2", mask2)
    cv2.imshow("Result2", result2)

    mask = mask1 | mask2
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    find_color()
    find_color2()