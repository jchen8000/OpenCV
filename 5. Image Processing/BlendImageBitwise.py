import cv2
import common.ImageProcessing as ip

def blendTwoImagesWithMask(imageFile1, imageFile2):
    title = "Blend Two Images"
    iproc = ip.ImageProcessing(title, imageFile1)
    iproc.show(title="Original Image1", image=iproc.image)
    toBlend = cv2.imread(imageFile2)
    iproc.show(title="Original Image2", image=toBlend)
    _, mask = iproc.remove_background_by_color( hsv_lower=(90, 0, 100),
                                                hsv_upper=(179, 255, 255),
                                                image=toBlend)
    iproc.show(title="Mask from Original Image2", image=mask )
    iproc.show(title="(1-Mask)", image= (255-mask))
    # iproc.show("Mask applied on 1st image", cv2.bitwise_and(toBlend, mask) )
    # iproc.show("Mask applied on 2nd image", cv2.bitwise_and(iproc.image, (255-mask)))
    # blend = cv2.bitwise_or(cv2.bitwise_and(toBlend, mask), cv2.bitwise_and(iproc.image, (255-mask)))
    blend = iproc.blend_with_mask(toBlend, mask)
    iproc.show(title=title, image=blend)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image1 = "../res/sky001.jpg"
    image2 = "../res/bird002.jpg"
    blendTwoImagesWithMask(image1, image2)


