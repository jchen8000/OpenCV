import cv2
import common.ImageProcessing as ip

def change_alpha(value):
    global alpha
    alpha = float(value)/100

def blendTwoImages(imageFile1, imageFile2):
    global alpha
    alpha = 0.5
    title = "Blend Two Images"
    iproc = ip.ImageProcessing(title, imageFile1)
    toBlend = cv2.imread(imageFile2)
    cv2.createTrackbar("Alpha", title, 50, 100, change_alpha)

    iproc.show("Original Image 1", )
    iproc.show("Original Image 2", toBlend)
    print("Press s key to save image, ESC to exit.")
    while True:
        blended_image = iproc.blend(toBlend, alpha)
        iproc.show(image=blended_image)
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:
            break
        elif ch == ord('s'):
            # press 's' key to save image
            filepath = "C:/temp/blend_image.png"
            cv2.imwrite(filepath, blended_image)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image1 = "../res/sky001.jpg"
    image2 = "../res/bird002.jpg"
    blendTwoImages(image1, image2)


