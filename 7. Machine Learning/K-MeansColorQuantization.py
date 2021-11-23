import numpy as np
import cv2

def get_distinct_colours(image):
    unique, counts = np.unique(image.reshape(-1, img.shape[-1]),
                               axis=0, return_counts=True)
    return counts.size

def color_quantization(image, clusters):
    X = image.reshape((-1,3))
    X = np.float32(X)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv2.kmeans(X, clusters, None, criteria, 10,
                                cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape((img.shape))
    return result

if __name__ == "__main__":
    img = cv2.imread("../res/color_wheel.png")
    print("Distinct colors in original image:", get_distinct_colours(img))
    cv2.imshow('Original', img)
    result = color_quantization(img, 9)
    print("Distinct colors after color quantization:", get_distinct_colours(result))
    cv2.imshow('Color Quantization (clusters=9)', result)
    print("Press any key...")
    filepath = "C:/temp/color_quan.jpg"
    cv2.imwrite(filepath, img)
    filepath = "C:/temp/color_quan2.jpg"
    cv2.imwrite(filepath, result)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img = cv2.imread("../res/flower004.jpg")
    print("Distinct colors in original:", get_distinct_colours(img))
    cv2.imshow('Original', img)
    result = color_quantization(img, 32)
    print("Distinct colors after color quantization(clusters=32):", get_distinct_colours(result))
    cv2.imshow('Color Quantization (clusters=32)', result)
    print("Press any key...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
