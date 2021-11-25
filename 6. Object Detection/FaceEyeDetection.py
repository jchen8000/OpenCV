import cv2

def detect_face_and_eye(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    print('Faces found: ', len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face_gray = gray[y:y + h, x:x + w]
        face_color = image[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=3)
        print('Eyes found: ', len(eyes))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    return image

if __name__ == "__main__":
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                         "haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                        "haarcascade_eye.xml")

    img = cv2.imread("../res/pexels-bess-hamiti-35188.jpg")
    cv2.imshow("Face and Eye Detection", detect_face_and_eye(img) )

    cv2.waitKey(0)
    cv2.destroyAllWindows()


