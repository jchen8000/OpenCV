import cv2
import numpy as np

class ShapeDetector:
    def __init__(self):
        self.epsilon = 0.02
        self.shapes = {
            "Triangle": 3,
            "Square": 4,
            "Pentagon": 5,
            "Hexagon": 6,
            "Circle": 8
        }

    def get_shape(self, vertices, ratio=1.0):
        shape = "Other"
        for (i, (lbl, vrt)) in enumerate(self.shapes.items()):
            if vertices == vrt:
                if vrt == 4:
                    if ratio > 0.95 and ratio < 1.05:
                        shape = "Square"
                    else:
                        shape = "Rectangle"
                else:
                    shape = lbl
        return shape

    def detect(self, contour):
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        approximation = cv2.approxPolyDP(contour, self.epsilon * perimeter, True)
        x, y, w, h = cv2.boundingRect(approximation)
        vertices = len(approximation)
        shape = self.get_shape(vertices, (float(w) / float(h)))
        return shape, area, perimeter, vertices

    def get_bounding_rect(self, contour):
        perimeter = cv2.arcLength(contour, True)
        approximation = cv2.approxPolyDP(contour, self.epsilon * perimeter, True)
        x, y, w, h = cv2.boundingRect(approximation)
        return x, y, w, h

    def get_center(self, contour):
        M = cv2.moments(contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        return cx, cy

    def pre_processing(self, image, show_interim=False, canny_lower=150, canny_upper=200, ksize=4 ):
        kernel = np.ones((ksize, ksize), np.uint8)
        imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        imgCanny = cv2.Canny(imgGray, canny_lower, canny_upper)
        imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
        imgErosion = cv2.erode(imgDilation, kernel, iterations=1)
        if show_interim:
            cv2.imshow("1.Gray", imgGray)
            cv2.imshow("2.Canny", imgCanny)
            cv2.imshow("3.Dilation", imgDilation)
            cv2.imshow("4.Erosion", imgErosion)
        return imgErosion

class ColorDetector:
    def __init__(self):
        self.colors = {
            "Red_":     ([[0, 90, 100],   [10, 255, 255]]),
            "Yellow":   ([[11, 90, 100],  [35, 255, 255]]),
            "Green":    ([[36, 90, 100],  [70, 255, 255]]),
            "Cyan":     ([[71, 90, 100],  [100, 255, 255]]),
            "Blue":     ([[101, 90, 100], [130, 255, 255]]),
            "Magenta":  ([[131, 90, 100], [159, 255, 255]]),
            "Red":      ([[160, 90, 100], [190, 255, 255]]),
        }

    def get_color_label(self, hsv, mask):
        color_label = "Unknown"
        masked_hsv = cv2.bitwise_and(hsv, hsv, mask=mask)
        mean = cv2.mean(masked_hsv, mask=mask)[:3]
        for (i, (label, (lower, upper))) in enumerate(self.colors.items()):
            if np.all(np.greater_equal(mean, lower)) and np.all(np.less_equal(mean, upper)):
                color_label = label
        return color_label, mean

if __name__ == "__main__":
    cd = ColorDetector()
    sd = ShapeDetector()

    print("Colors")
    for (i, (label, (lower, upper))) in enumerate(cd.colors.items()):
        print(i, label, ": lower=", lower, "; upper=", upper)

    print("Shapes")
    for (i, (label, vertices)) in enumerate(sd.shapes.items()):
        print(i, label, ": vertices =", vertices)

