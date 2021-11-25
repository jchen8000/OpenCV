import cv2
import pixellib
from pixellib.tune_bg import alter_bg
from pathlib import Path

if __name__ == "__main__":
    model_file = "../res/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5"
    file_exist = Path(model_file)
    if file_exist.is_file():
        change_bg = alter_bg()
        change_bg.load_pascalvoc_model(model_file)
        #
        # Original image
        #
        print("Loading original image ...")
        image_file = "../res/bird004.jpg"
        image = cv2.imread(image_file)
        cv2.imshow("Original", image)

        #
        # Remove Background
        #
        print("Removing background ...")
        bg_removed = change_bg.color_bg(image_file, colors = (0,0,0))
        cv2.imshow("Remove Background", bg_removed)

        #
        # Gray Background
        #
        print("Gray Background ...")
        bg_gray = change_bg.gray_bg(image_file)
        cv2.imshow("Gray Background", bg_gray)

        #
        # Blur Background
        #
        print("Blur Background ...")
        bg_blur = change_bg.blur_bg(image_file, low = True)
        cv2.imshow("Blur Background", bg_blur)

        #
        # Change Background
        #
        background_file = "../res/background_002.jpg"
        print("Change Background ...")
        bg_change = change_bg.change_bg_img(f_image_path = image_file,
                                            b_image_path = background_file)
        cv2.imshow("Change Background", bg_change)
        print("Press any key to close ...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print( "Can not find the model file:", model_file)
        print( "Please download it at https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
        print("and put it in /res directory")