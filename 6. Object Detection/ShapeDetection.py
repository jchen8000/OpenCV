import cv2
import numpy as np
from common.Detector import ShapeDetector

def find_contours(image, canvas):
    color = (255, 10, 10)
    thickness = 3
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        cv2.drawContours(canvas, contour, -1, color, thickness)
    return contours

def find_shapes(contours, canvas):
    global shape_detector

    contour_color = (255, 10, 10)
    bounding_color = (10, 10, 10)
    text_color = (10, 10, 10)
    for contour in contours:
        shape, area, perimeter, vertices = shape_detector.detect(contour)
        x, y, w, h = shape_detector.get_bounding_rect(contour)
        cx, cy = shape_detector.get_center(contour)
        cv2.drawContours(canvas, contour, -1, contour_color, 3)
        cv2.rectangle(canvas, (x, y), (x + w, y + h), bounding_color, 1)
        textX = x
        textY = y - 70
        textVert = ": Vertices={:d},".format(vertices)
        textArea = "Area={:.0f},".format(area)
        textPeri = "Perimeter={:.0f}".format(perimeter)
        print(shape, textVert, textArea, textPeri)
        cv2.putText(canvas, shape, (textX, textY+10), cv2.FONT_HERSHEY_COMPLEX, 1, text_color, 2)
        cv2.putText(canvas, textArea, (textX, textY + 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, text_color, 1)
        cv2.putText(canvas, textPeri, (textX, textY + 65), cv2.FONT_HERSHEY_COMPLEX, 0.8, text_color, 1)
        cv2.circle(canvas, (cx,cy), 2, contour_color, 2)

def shape_detection():
    global shape_detector

    # Create ShapeDetector object from the class
    shape_detector = ShapeDetector()

    # Load and show the image
    img = cv2.imread("../res/shapes_002.jpg")
    cv2.imshow("Original", img)

    # pre-process the image for shape detection
    # pass True in second parameter will draw the interim results
    imgPreprocessed = shape_detector.pre_processing(img, True)

    # find contours and draw it on the canvas, which is
    # a copy of the original image
    imgCanvas = img.copy()
    contours = find_contours(imgPreprocessed, imgCanvas)
    cv2.imshow("Contours", imgCanvas)

    # find shapes based on the contours detected,
    # draw it on a blank canvas
    imgDetected = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    imgDetected[:] = 255, 255, 255
    find_shapes(contours, imgDetected)
    cv2.imshow("Detected", imgDetected)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    shape_detection()

