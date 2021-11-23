import cv2

def chg_ksize(value):
    global ksize
    if value % 2 == 0:
        ksize = value+1
    else:
        ksize = value

def chg_method(value):
    global blur_method
    blur_method = value

def chg_color_gray(value):
    global is_gray
    is_gray = value

def chg_sigma(value):
    global sigma
    sigma = value

def blur_background(image, mask):
    global ksize, blur_method, is_gray, sigma
    ksize = 9
    blur_method = 0
    is_gray = 0
    sigma = 22
    image = cv2.imread(image)
    mask = cv2.imread(mask)
    foreground = cv2.bitwise_and(image, mask)
    cv2.imshow("Original", image)
    # cv2.imshow("Mask", (255-mask))
    # cv2.imshow("Background Removed", foreground)
    title = "Background Blurred"
    cv2.namedWindow("Parameters")
    cv2.createTrackbar("K-Size", "Parameters", ksize, 51, chg_ksize)
    cv2.createTrackbar("Sigma", "Parameters", sigma, 50, chg_sigma)
    cv2.createTrackbar("Gaus/Medn", "Parameters", blur_method, 1, chg_method)
    cv2.createTrackbar("Color/Gray", "Parameters", is_gray, 1, chg_color_gray)
    while True:
        background = cv2.bitwise_and(image, (255 - mask))
        if blur_method == 0:
            background = cv2.GaussianBlur(background, (ksize, ksize),
                                          sigma, sigma, cv2.BORDER_DEFAULT )
        else:
            background = cv2.medianBlur(background, ksize)
        if is_gray == 1:
            background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
            background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)

        result = cv2.bitwise_or(foreground, background)
        cv2.imshow(title, result)
        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:   # Press 'ESC' to exit
            break
        elif ch == ord('s'):    # Press 's' to save
            filepath = "C:/temp/blur_background.png"
            cv2.imwrite(filepath, result)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    blur_background(image="../res/flower011.jpg",
                    mask="../res/flower011_mask.jpg")

    # blur_background(image="../res/flower012.jpg",
    #                 mask="../res/flower012_mask.jpg")

    # blur_background(image="../res/flower014.jpg",
    #                 mask="../res/flower014_mask.jpg")