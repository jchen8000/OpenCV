import cv2

def convert_bgr2gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def convert_gray2bgr(image):
    bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return bgr

def convert_bgr2hsv(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv

def convert_hsv2bgr(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    return hsv

def load_image_gray(file_name):
    gray = cv2.imread("../res/flower003.jpg", cv2.IMREAD_GRAYSCALE)
    gray = cv2.resize(gray, (int(gray.shape[1] * 60.0 / 100), int(gray.shape[0] * 60.0 / 100)))
    return gray

def split_image(image):
    ch1, ch2, ch3 = cv2.split(image)
    return ch1, ch2, ch3

if __name__ == "__main__":
    print("Convert a color image from BGR to GRAY.")
    image = cv2.imread("../res/flower003.jpg")
    image = cv2.resize(image, (int(image.shape[1]*60.0/100), int(image.shape[0]*60.0/100)) )
    gray = convert_bgr2gray(image)
    cv2.imshow("Color", image)
    cv2.imshow("Gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Split BGR image into channels")
    blue, green, red = split_image(image)
    cv2.imshow("Color", image)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Red", red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Load a image in GRAY mode.")
    cv2.imshow("Gray Image", load_image_gray("../res/flower003.jpg"))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Convert a GRAY image to BGR.")
    cv2.imshow("Gray", gray)
    cv2.imshow("BGR", convert_gray2bgr(gray))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Convert a BGR image to HSV and Split it into H, S and V channels.")
    hsv = convert_bgr2hsv(image)
    h, s, v = split_image(hsv)
    cv2.imshow("Original", image)
    cv2.imshow("Hue", h)
    cv2.imshow("Saturation", s)
    cv2.imshow("Value", v)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

