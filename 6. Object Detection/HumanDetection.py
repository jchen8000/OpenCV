import cv2

def human_detection_from_video():
    cap = cv2.VideoCapture(0)
    success, image = cap.read()
    while success:
        cv2.imshow("Human Detection from Video", human_detection(image))
        # Press ESC key to break the loop
        if cv2.waitKey(5) & 0xFF == 27:
            break
        success, image = cap.read()
    cap.release()
    cv2.destroyAllWindows()

def human_detection(image):
    boxes, weights = hog.detectMultiScale(image, winStride=(8, 8))
    person = 1
    for x,y,w,h in boxes:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(image, f'person-{person}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
        person += 1
    return image

if __name__ == "__main__":
    # initialize HOG for human/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    img1 = cv2.imread("../res/pexels-charlotte-may-5965704.jpg")
    cv2.imshow("Human Detection 1", human_detection(img1))

    img2 = cv2.imread("../res/pexels-catia-matos-1605936.jpg")
    cv2.imshow("Human Detection 2", human_detection(img2))

    img3 = cv2.imread("../res/pexels-daniel-frese-574177.jpg")
    cv2.imshow("Human Detection 3", human_detection(img3))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Loading youtube video...")
    human_detection_from_video()


