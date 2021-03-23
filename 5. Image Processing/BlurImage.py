import cv2
import common.ImageProcessing as ip

def change_ksize(value):
    global ksize
    if value % 2 == 0:
        ksize = (value+1, value+1)
    else:
        ksize = (value, value)

def gaussian_blur():
    global ksize
    ksize = (5,5)
    iproc = ip.ImageProcessing("Original", "../res/flower003.jpg")
    iproc.show(image=iproc.resize(65))

    cv2.namedWindow("Gaussian Blur")
    cv2.createTrackbar("K-Size", "Gaussian Blur", 5, 21, change_ksize)

    while True:
        blur = iproc.gaussian_blur(ksize)
        iproc.show("Gaussian Blur", iproc.resize(65,blur))

        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:   # Press 'ESC' to exit
            break
        elif ch == ord('s'):    # Press 's' to save
            filepath = "C:/temp/blur_image.png"
            cv2.imwrite(filepath, blur)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()


def median_blur():
    global ksize
    ksize = (5, 5)
    iproc = ip.ImageProcessing("Original", "../res/pexels-edward-jenner-4250573.jpg")
    iproc.show(image=iproc.resize(65))

    cv2.namedWindow("Median Blur")
    cv2.createTrackbar("K-Size", "Median Blur", 5, 21, change_ksize)

    while True:
        median_blur = iproc.median_blur(ksize[0])
        iproc.show("Median Blur", iproc.resize(65,median_blur))

        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:   # Press 'ESC' to exit
            break
        elif ch == ord('s'):    # Press 's' to save
            filepath = "C:/temp/blur_image.png"
            cv2.imwrite(filepath, median_blur)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    gaussian_blur()
    median_blur()