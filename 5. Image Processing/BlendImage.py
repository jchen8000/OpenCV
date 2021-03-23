import cv2
import common.ImageProcessing as ip

def change_alpha(value):
    global alpha
    alpha = float(value)/100

def create_mask(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.bitwise_not(image)
    image[image>128] = 255
    image[image<127] = 0
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return image

if __name__ == "__main__":
    alpha = 0.5
    title = "Blend Two Images"
    iproc = ip.ImageProcessing(title, "../res/pexels-valdemaras-d-2230346.jpg")
    toBlend = cv2.imread("../res/pexels-wendy-wei-3000260.jpg")
    mask = create_mask(toBlend)

    cv2.createTrackbar("Alpha", title, 50, 100, change_alpha)
    iproc.show("Original Image 1", )
    iproc.show("Original Image 2", toBlend)
    iproc.show("Mask", mask)
    toBlendMask = iproc.blend_with_mask(toBlend, mask)
    iproc.show("Blend Two Images With Mask", toBlendMask)
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

