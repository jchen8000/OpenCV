import cv2
import numpy as np
import pytesseract

def resize(percent, image):
    width = int(image.shape[1]*percent/100)
    height = int(image.shape[0]*percent/100)
    resized_image = cv2.resize(image, (width, height) )
    return resized_image

def perspective_warp(points, width, height, image):
    pts_source = np.float32([points[0], points[1], points[3], points[2]])
    pts_target = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts_source, pts_target)
    result = cv2.warpPerspective(image, matrix, (width, height))
    return result

def recognize_to_string(image):
    text = pytesseract.image_to_string(image)
    return text

def recognize_by_char(image):
    height, weight = image.shape[:2]
    chars = pytesseract.image_to_boxes(image)
    for char in chars.splitlines():
        print(char)
        char = char.split(" ")
        c,x,y,w,h = char[0], int(char[1]), int(char[2]), int(char[3]), int(char[4])
        cv2.rectangle(image, (x,height-y), (w,height-h), (0,0,255),1)
        cv2.putText(image, c, (x,height-y-35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 1)

def recognize_by_word(image):
    words = pytesseract.image_to_data(image)
    for i, word in enumerate(words.splitlines()):
        if i != 0:
            word = word.split()
            print(word)
            if len(word) == 12:
                t,x,y,w,h = word[11], int(word[6]), int(word[7]), int(word[8]), int(word[9])
                cv2.rectangle(image, (x,y), (w+x,h+y), (0,0,255),1)
                cv2.putText(image, t, (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 1)

def text_recognition():
    # img = cv2.imread("../res/text_for_ocr.png")
    # width, height = 880, 760
    # # points = [(69, 1), (1089, 83), (1020, 947), (0, 866)]
    # points = [(64,106), (1058,182), (998,940), (4,863)]

    img = cv2.imread("../res/text_for_ocr2.jpg")
    width, height = 1000, 1020
    points = [(103, 14), (1103, 104), (1008, 1130), (10, 1040)]

    warped = perspective_warp(points, width, height, img)
    cv2.imshow("Warped", warped)
    cv2.imshow("Original", img)
    text = recognize_to_string(warped)
    print(text)

    result1 = warped.copy()
    result2 = warped.copy()
    recognize_by_char(result1)
    recognize_by_word(result2)

    cv2.imshow("Text Recognition by Char", result1)
    cv2.imshow("Text Recognition by Word", result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # #For Windows
    # pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    #For Linux/Ubuntu
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
    text_recognition()
