import cv2
import numpy as np
from matplotlib import pyplot as plt
import common.ImageProcessing as ip

def show_histogram():
    img = np.zeros((400, 400), np.uint8)
    cv2.rectangle(img, (200, 0), (400, 100), (100), -1)
    cv2.rectangle(img, (0, 100), (200, 200), (50), -1)
    cv2.rectangle(img, (200, 100), (400, 200), (150), -1)
    cv2.rectangle(img, (0, 200), (200, 300), (175), -1)
    cv2.rectangle(img, (0, 300), (200, 400), (200), -1)
    cv2.rectangle(img, (200, 200), (400, 400), (255), -1)
    cv2.imshow("Histogram", img)
    fig = plt.figure(figsize=(6, 4))
    fig.suptitle('Histogram', fontsize=20)
    plt.xlabel('Color Value', fontsize=12)
    plt.ylabel('# of Pixels', fontsize=12)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()
    cv2.destroyAllWindows()

# Get histogram using OpenCV
def show_histogram_gray(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    fig = plt.figure(figsize=(6, 4))
    fig.suptitle('Histogram -- using OpenCV', fontsize=18)
    plt.plot(hist)
    plt.show()

# An alternative way to get histogram using matplotlib
def show_histogram_gray_alt(image):
    fig = plt.figure(figsize=(6, 4))
    fig.suptitle('Histogram -- using matplotlib', fontsize=18)
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

def show_histogram_color(image):
    blue, green, red = cv2.split(image)
    # cv2.imshow("blue", blue)
    # cv2.imshow("green", green)
    # cv2.imshow("red", red)
    fig = plt.figure(figsize=(6, 4))
    fig.suptitle('Histogram', fontsize=18)
    plt.hist(blue.ravel(), 256, [0, 256])
    plt.hist(green.ravel(), 256, [0, 256])
    plt.hist(red.ravel(), 256, [0, 256])
    plt.show()

if __name__ == "__main__":
    # Introduction to histograms
    show_histogram()

    iproc = ip.ImageProcessing("Histogram", "../res/flower004.jpg")

    # Histograms for gray image
    grayImage = iproc.to_gray()
    iproc.show(image=grayImage)
    show_histogram_gray(grayImage)
    show_histogram_gray_alt(grayImage)

    # Histograms for color image
    iproc.show(image=iproc.image)
    show_histogram_color(iproc.image)
    cv2.destroyAllWindows()