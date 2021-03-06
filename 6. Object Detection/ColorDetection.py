import cv2
import numpy as np
from common.Detector import ShapeDetector
from common.Detector import ColorDetector

def show_hsv_values(image, hsv, canvas):
    global shape_detector, color_detector
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        mask = np.zeros(image.shape[:2], np.uint8)
        cv2.drawContours(mask, [contour], -1, (255), cv2.FILLED)
        color, mean = color_detector.get_color_label(hsv, mask)
        x, y, w, h = shape_detector.get_bounding_rect(contour)
        text = "hsv=({:.0f},{:.0f},{:.0f})".format(mean[0],mean[1],mean[2])
        cv2.putText(canvas, color, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 1)
        cv2.putText(canvas, text, (x-20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 0), 1)

def color_detection():
    global shape_detector, color_detector

    # Create ShapeDetector object from the class
    shape_detector = ShapeDetector()
    color_detector = ColorDetector()

    # Load and show the image
    img = cv2.imread("../res/colors.jpg")
    percent = 70
    width = int(img.shape[1] * percent / 100)
    height = int(img.shape[0] * percent / 100)
    img = cv2.resize(img, (width, height))

    result = img.copy()

    imgPreprocessed = shape_detector.pre_processing(img, False)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    show_hsv_values(imgPreprocessed, hsv, result)

    cv2.imshow("Original", img)
    cv2.imshow("Color Detected", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    color_detection()


