import cv2
import numpy as np

def pre_processing(image, show_interim=False):
    canny_lower_thold = 150
    canny_upper_thold = 200
    kernel = np.ones((4, 4), np.uint8)
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, canny_lower_thold, canny_upper_thold)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
    imgErosion = cv2.erode(imgDilation, kernel, iterations=1)
    if show_interim:
        cv2.imshow("1.Gray", imgGray)
        cv2.imshow("2.Canny", imgCanny)
        cv2.imshow("3.Dilation", imgDilation)
        cv2.imshow("4.Erosion", imgErosion)
    return imgErosion

def find_contours(image, canvas):
    color = (255, 10, 10)
    thickness = 3
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        cv2.drawContours(canvas, contour, -1, color, thickness)
    return contours

def find_shapes(contours, canvas):
    contour_color = (255, 10, 10)
    bounding_color = (10, 255, 10)
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        approximation = cv2.approxPolyDP(contour, 0.02*perimeter, True)
        x, y, w, h = cv2.boundingRect(approximation)
        cv2.drawContours(canvas, contour, -1, contour_color, 3)
        cv2.rectangle(canvas, (x, y), (x + w, y + h), bounding_color, 1)
        vertices = len(approximation)
        show_shape_info(canvas, x, y, w, h, type, vertices, area, perimeter)

def show_shape_info(canvas, x, y, w, h, type, vertices, area, perimeter):
    text_color = (10, 10, 10)
    if vertices == 3:
        type = "Tri"
    elif vertices == 4:
        aspRatio = float(w) / float(h)
        if aspRatio > 0.95 and aspRatio < 1.05:
            type = "Sqr"
        else:
            type = "Rect"
    elif vertices == 8:
        type = "Cir"
    else:
        type = "Oth"
    textX = x - 25
    textY = y - 15
    textPoint = "Vertices={:d}".format(vertices)
    textArea = "Area={:.0f}".format(area)
    textPeri = "Perimeter={:.0f}".format(perimeter)
    print(type, textPoint, textArea, textPeri)
    cv2.putText(canvas, type, (textX, textY), cv2.FONT_HERSHEY_COMPLEX, 0.65, text_color, 1)
    cv2.putText(canvas, textArea, (textX, textY + 15), cv2.FONT_HERSHEY_COMPLEX, 0.4, text_color, 1)
    cv2.putText(canvas, textPeri, (textX, textY + 30), cv2.FONT_HERSHEY_COMPLEX, 0.4, text_color, 1)

def shape_detection():
    # Load and show the image
    img = cv2.imread("../res/shapes.jpg")
    cv2.imshow("Original", img)

    # pre-process the image for shape detection
    # pass True in second parameter will draw the interim results
    imgPreprocessed = pre_processing(img, False)

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

