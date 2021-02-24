import cv2

class ResizeCropRotate(object):
    def __init__(self, window_name, image_name):
        self.window_name = window_name
        self.image_name = image_name
        self.image = cv2.imread(self.image_name)

    def resize(self, percent):
        width = int(self.image.shape[1]*percent/100)
        height = int(self.image.shape[0]*percent/100)
        resized_image = cv2.resize(self.image, (width, height) )
        return resized_image

    def crop(self, pt_first, pt_second):
        x_tl, y_tl = pt_first           # top-left point
        x_br, y_br = pt_second          # bottom-right point
        if x_br < x_tl:                 # swap x value if opposite
            x_br, x_tl = x_tl, x_br
        if y_br < y_tl:                 # swap y value if opposite
            y_br, y_tl = y_tl, y_br
        cropped_image = self.image[y_tl:y_br, x_tl:x_br]
        return cropped_image

    def run(self):
        cv2.imshow("Original", self.image)
        cv2.imshow("Resized", self.resize(60) )
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    rcr = ResizeCropRotate("Resize,Crop and Rotate", "../res/flower005.jpg")
    rcr.run()

