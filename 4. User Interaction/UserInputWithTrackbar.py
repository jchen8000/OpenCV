import cv2

def change_brightness(value):
    global cap
    print("Brightness: " + str(value))
    cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

def change_contrast(value):
    print("Contrast: " + str(value))
    cap.set(cv2.CAP_PROP_CONTRAST, value)

def change_saturation(value):
    print("Saturation: " + str(value))
    cap.set(cv2.CAP_PROP_SATURATION, value)

def change_hue(value):
    print("Hue: " + str(value))
    cap.set(cv2.CAP_PROP_HUE, value)

def resize(image, percent):
    width = int(image.shape[1] * percent / 100)
    height = int(image.shape[0] * percent / 100)
    resized_image = cv2.resize(image, (width, height))
    return resized_image


def main():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)      # set width
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)     # set height
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)       # set initial brightness
    cap.set(cv2.CAP_PROP_CONTRAST, 50)          # set initial contrast
    cap.set(cv2.CAP_PROP_SATURATION, 90)        # set initial saturation
    cap.set(cv2.CAP_PROP_HUE, 15)               # set initial hue

    cv2.namedWindow('Webcam')
    cv2.createTrackbar('Brightness', 'Webcam', 100,300, change_brightness)
    cv2.createTrackbar('Contrast', 'Webcam', 50, 300, change_contrast)
    cv2.createTrackbar('Saturation', 'Webcam', 90, 100, change_saturation)
    cv2.createTrackbar('Hue', 'Webcam', 15, 360, change_hue)

    success, img = cap.read()
    while success:
        cv2.imshow("Webcam", resize(img, 90))

        # Press ESC key to break the loop
        if cv2.waitKey(10) & 0xFF == 27:
            break
        success, img = cap.read()

    cap.release()
    cv2.destroyWindow("Webcam")

if __name__ == '__main__':
    main()