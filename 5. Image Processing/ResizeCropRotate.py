import cv2
import common.ImageProcessing as ip

if __name__ == "__main__":
    # Create an ImageProcessing object
    ip = ip.ImageProcessing("Original", "../res/flower009.jpg")

    # Show original image
    ip.show(image=ip.resize(80))

    # Resize the original image and show it
    resized_image = ip.resize(50)
    ip.show("Resized -- 50%", resized_image)

    # Rotate the resized image and show it
    rotated_image = ip.rotate(45, resized_image)
    ip.show("Rotated -- 45 degree", rotated_image)

    # Crop the original image and show it
    cropped_image = ip.crop((100, 100), (530, 400))
    ip.show("Cropped", cropped_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

