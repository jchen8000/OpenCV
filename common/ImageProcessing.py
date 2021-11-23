import cv2
import numpy as np

class ImageProcessing(object):
    def __init__(self, window_name, image_name):
        self.window_name = window_name
        self.image_name = image_name
        cv2.namedWindow(window_name)
        self.image = cv2.imread(self.image_name)

    def show(self, title=None, image=None):
        if image is None:
            image = self.image
        if title is None:
            title = self.window_name
        cv2.imshow(title, image)

    def resize(self, percent, image=None):
        if image is None:
            image = self.image
        width = int(image.shape[1]*percent/100)
        height = int(image.shape[0]*percent/100)
        resized_image = cv2.resize(image, (width, height) )
        return resized_image

    def to_gray(self, image=None):
        if image is None:
            image = self.image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    def crop(self, pt_first, pt_second, image=None):
        if image is None:
            image = self.image
        x_tl, y_tl = pt_first           # top-left point
        x_br, y_br = pt_second          # bottom-right point
        if x_br < x_tl:                 # swap x value if opposite
            x_br, x_tl = x_tl, x_br
        if y_br < y_tl:                 # swap y value if opposite
            y_br, y_tl = y_tl, y_br
        cropped_image = image[y_tl:y_br, x_tl:x_br]
        return cropped_image

    def rotate(self, angle, image=None, scale=1.0):
        if image is None:
            image = self.image
        (h, w) = image.shape[:2]
        center = (w / 2, h / 2)
        rot_mat = cv2.getRotationMatrix2D(center, angle, scale)
        rotated_image = cv2.warpAffine(image, rot_mat, (w, h))
        return rotated_image

    def copy(self):
        return self.image.copy()

    def contrast_brightness(self, contrast, brightness, image=None):
        # contrast: between 0.0 and 1.0: less contrast;
        #           > 1.0: more contrast;
        #           1: unchange
        # brightness: -127 to 127;
        #           0 unchange
        if image is None:
            image = self.image
        zeros = np.zeros(image.shape, image.dtype)
        result = cv2.addWeighted(image, contrast, zeros, 0, brightness)
        return result

    def hue_saturation_value(self, hue, saturation, value, image=None):
        if image is None:
            image = self.image
        hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsvImage)
        zeros = np.zeros(h.shape, h.dtype)
        h = cv2.addWeighted(h, 1.0, zeros, 0, hue)
        s = cv2.addWeighted(s, 1.0, zeros, 0, saturation)
        v = cv2.addWeighted(v, 1.0, zeros, 0, value)
        result = cv2.merge([h, s, v])
        result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
        return result

    def blend(self, blend, alpha, image=None):
        if image is None:
            image = self.image
        #blend = cv2.resize(blend, (image.shape[1], image.shape[0]))
        blend = cv2.resize(blend, image.shape[1::-1])
        result = cv2.addWeighted(image, alpha, blend, (1.0 - alpha), 0)
        return result

    def blend_with_mask(self, blend, mask, image=None):
        if image is None:
            image = self.image
        blend = cv2.resize(blend, image.shape[1::-1])
        mask = cv2.resize(mask, image.shape[1::-1])
        result = cv2.bitwise_and(blend, mask) + cv2.bitwise_and(image, (255 - mask))
        return result

    def perspective_warp(self, points, width, height, image=None):
        if image is None:
            image = self.image
        pts_source = np.float32([points[0], points[1], points[3], points[2]])
        pts_target = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts_source, pts_target)
        result = cv2.warpPerspective(image, matrix, (width, height))
        return result

    def gaussian_blur(self, ksize=(1,1), image=None):
        if image is None:
            image = self.image
        if ksize[0] % 2 == 0:
            ksize = (ksize[0] + 1, ksize[1])
        if ksize[1] % 2 == 0:
            ksize = (ksize[0], ksize[1] + 1)
        result = cv2.GaussianBlur(image, ksize, cv2.BORDER_DEFAULT)
        return result

    def median_blur(self, ksize=1, image=None):
        if image is None:
            image = self.image
        result = cv2.medianBlur(image, ksize)
        return result

    def remove_background_by_contour(self,
                                     gs_blur=3,
                                     canny_lower=10,
                                     canny_upper=200,
                                     dilate_iter=1,
                                     erode_iter=1,
                                     image = None):
        if image is None:
            image = self.image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, canny_lower, canny_upper)
        edges = cv2.dilate(edges, None)
        edges = cv2.erode(edges, None)
        mask = np.zeros_like(edges)
        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            cv2.fillConvexPoly(mask, contour, (255))
        mask = cv2.dilate(mask, None, iterations=dilate_iter)
        mask = cv2.erode(mask, None, iterations=erode_iter)
        if gs_blur % 2 == 0:
            gs_blur = gs_blur + 1
        elif gs_blur <= 0:
            gs_blur = 1
        mask = cv2.GaussianBlur(mask, (gs_blur, gs_blur), 0)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        bg_removed = cv2.bitwise_and(image, mask)
        return bg_removed, mask

    def remove_background_by_color(self,
                                   hsv_lower=(10,10,10),
                                   hsv_upper=(179,255,255),
                                   image=None ):
        if image is None:
            image = self.image
        imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHSV, hsv_lower, hsv_upper)
        mask = 255 - mask
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        bg_removed = cv2.bitwise_and(image, mask)
        return bg_removed, mask

    def remove_background_by_mask(self, mask, image = None):
        if image is None:
            image = self.image
        bg_removed = cv2.bitwise_and(image, mask)
        return bg_removed, mask

