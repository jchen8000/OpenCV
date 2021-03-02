import cv2
import common.ImageProcessing as ip

if __name__ == "__main__":
    # Create an ImageProcessing object
    ip = ip.ImageProcessing("Resize,Crop and Rotate", "../res/flower005.jpg")

    # Show original image
    ip.show()

    # Resize the original image and show it
    resized_image = ip.resize(50)
    ip.show("Resized -- 50%", resized_image)

    # Rotate the resized image and show it
    rotated_image = ip.rotate(45, resized_image)
    ip.show("Rotated -- 45 degree", rotated_image)

    # Crop the original image and show it
    cropped_image = ip.crop((300, 10), (600, 310))
    ip.show("Cropped", cropped_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

