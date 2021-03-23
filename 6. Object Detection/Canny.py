import cv2

def nothing(x):
    pass

def canny_edge_detection():
    lower, upper = 100, 200
    image = cv2.imread("../res/flower001.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow("Canny")
    cv2.createTrackbar("Lower", "Canny", lower, 500, nothing)
    cv2.createTrackbar("Upper", "Canny", upper, 500, nothing)

    cv2.imshow("Original", image)
    cv2.imshow("Gray", gray)

    while True:
        lower = cv2.getTrackbarPos("Lower", "Canny")
        upper = cv2.getTrackbarPos("Upper", "Canny")
        canny = cv2.Canny(gray, lower, upper)
        cv2.imshow("Canny", canny)

        ch = cv2.waitKey(10)
        if (ch & 0xFF) == 27:   # Press 'ESC' to exit
            break
        elif ch == ord('s'):    # Press 's' to save
            filepath = "C:/temp/canny.png"
            cv2.imwrite(filepath, canny)
            print("File saved to " + filepath)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    canny_edge_detection()