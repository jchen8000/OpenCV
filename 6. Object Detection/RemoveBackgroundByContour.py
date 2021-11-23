import cv2
import common.ImageProcessing as ip

def empty(a):
    pass

if __name__ == "__main__":
    iproc = ip.ImageProcessing("Original", "../res/bird001.jpg")
    iproc.show(image=iproc.image)
    gs_blur = 3
    lower, upper = 103, 153
    dilate, erode = 1, 1
    cv2.namedWindow("Parameters")
    cv2.createTrackbar("GS_Blur", "Parameters", gs_blur, 51, empty)
    cv2.createTrackbar("Lower", "Parameters", lower, 300, empty)
    cv2.createTrackbar("Upper", "Parameters", upper, 300, empty)
    cv2.createTrackbar("Dilate", "Parameters", dilate, 25, empty)
    cv2.createTrackbar("Erode", "Parameters", erode, 25, empty)

    while True:
        gs_blur = cv2.getTrackbarPos("GS_Blur", "Parameters")
        lower = cv2.getTrackbarPos("Lower", "Parameters")
        upper = cv2.getTrackbarPos("Upper", "Parameters")
        dilate = cv2.getTrackbarPos("Dilate", "Parameters")
        erode = cv2.getTrackbarPos("Erode", "Parameters")
        bg_removed, mask = iproc.remove_background_by_contour(gs_blur, lower, upper, dilate, erode)
        cv2.imshow("Mask", mask)
        cv2.imshow("Background Removed", bg_removed)
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:  # Press 'ESC' to exit
            break
    cv2.destroyAllWindows()