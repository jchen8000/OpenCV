import cv2
import common.ImageProcessing as ip

def change_brightness(value):
    global brightness
    brightness = value - 128

def change_contrast(value):
    global contrast
    contrast = float(value)/100

if __name__ == "__main__":
    brightness = 0
    contrast = 1.0
    title = "Adjust Brightness and Contrast"
    ip = ip.ImageProcessing(title, "../res/flower003.jpg")
    cv2.createTrackbar('Brightness', title, 128, 255, change_brightness)
    cv2.createTrackbar('Contrast', title, 100, 300, change_contrast)

    while True:
        adjusted_image = ip.contrast_brightness(contrast, brightness)
        ip.show(image=adjusted_image)
        if cv2.waitKey(10) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
