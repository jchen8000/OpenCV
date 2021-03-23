import cv2
import numpy as np

def dilation(image, ksize=(1,1)):
    kernel = np.ones(ksize, np.uint8)
    dilation = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow("Original", image)
    cv2.imshow("Dilation", dilation)
    while True:
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:   # Press 'ESC' to exit
            break
        elif ch == ord('s'):    # Press 's' to save
            filepath = "C:/temp/dilation.png"
            cv2.imwrite(filepath, canny)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()
    return dilation

def erosion(image, ksize=(1,1)):
    kernel = np.ones(ksize, np.uint8)
    erosion = cv2.erode(image, kernel, iterations=1)
    cv2.imshow("Original", image)
    cv2.imshow("Erosion", erosion)
    while True:
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:   # Press 'ESC' to exit
            break
        elif ch == ord('s'):    # Press 's' to save
            filepath = "C:/temp/erosion.png"
            cv2.imwrite(filepath, canny)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()
    return erosion

if __name__ == "__main__":
    image = cv2.imread("../res/flower001.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lower, upper = 290, 475
    canny = cv2.Canny(image, lower, upper)
    dilation = dilation(canny, (3,3))
    erosion(dilation, (3,3))