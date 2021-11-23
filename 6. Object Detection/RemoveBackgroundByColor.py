import cv2
import common.ImageProcessing as ip

def empty(a):
    pass

if __name__ == "__main__":
    iproc = ip.ImageProcessing("Original", "../res/flower012.jpg")
    iproc.show(image=iproc.image)
    h_min, h_max = 25, 81
    s_min, s_max = 0, 255
    v_min, v_max = 0, 162
    cv2.namedWindow("Parameters")
    cv2.resizeWindow("Parameters", 460, 240)
    cv2.createTrackbar("Hue Min", "Parameters", h_min, 179, empty)
    cv2.createTrackbar("Hue Max", "Parameters", h_max, 179, empty)
    cv2.createTrackbar("Sat Min", "Parameters", s_min, 255, empty)
    cv2.createTrackbar("Sat Max", "Parameters", s_max, 255, empty)
    cv2.createTrackbar("Val Min", "Parameters", v_min, 255, empty)
    cv2.createTrackbar("Val Max", "Parameters", v_max, 255, empty)
    while True:
        h_min = cv2.getTrackbarPos("Hue Min", "Parameters")
        h_max = cv2.getTrackbarPos("Hue Max", "Parameters")
        s_min = cv2.getTrackbarPos("Sat Min", "Parameters")
        s_max = cv2.getTrackbarPos("Sat Max", "Parameters")
        v_min = cv2.getTrackbarPos("Val Min", "Parameters")
        v_max = cv2.getTrackbarPos("Val Max", "Parameters")
        bg_removed, mask = iproc.remove_background_by_color(
                                hsv_lower=(h_min, s_min, v_min),
                                hsv_upper=(h_max, s_max, v_max) )
        iproc.show(title="Mask", image=mask)
        iproc.show(title="Background Removed", image=bg_removed)
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:  # Press 'ESC' to exit
            break
    cv2.destroyAllWindows()