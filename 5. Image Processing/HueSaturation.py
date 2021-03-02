import cv2
import common.ImageProcessing as ip

def change_hue(value):
    global hue
    hue = (value * 2) - 255

def change_saturation(value):
    global sat
    sat = (value * 2) - 255

def change_value(value):
    global val
    val = (value * 2) - 255

if __name__ == "__main__":
    hue, sat, val = 0, 0, 0
    title = "Adjust Hue, Saturation and Value"
    ip = ip.ImageProcessing(title, "../res/flower003.jpg")
    cv2.createTrackbar('Hue', title, 127, 255, change_hue)
    cv2.createTrackbar('Saturation', title, 127, 255, change_saturation)
    cv2.createTrackbar('Value', title, 127, 255, change_value)
    ip.show("Original")
    print("Press s key to save image, ESC to exit.")

    while True:
        adjusted_image = ip.hue_saturation_value(hue, sat, val)
        ip.show(image=adjusted_image)
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:
            break
        elif ch == ord('s'):
            # press 's' key to save image
            filepath = "C:/temp/flower003.png"
            cv2.imwrite(filepath, adjusted_image)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()

