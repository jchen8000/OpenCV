#
# Show the Webcam as video
#
import cv2

cap = cv2.VideoCapture(0)                   # read from default webcam

# Set video properties
# https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704dab26d2ba37086662261148e9fe93eecad
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)      # set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)     # set height
cap.set(cv2.CAP_PROP_BRIGHTNESS, 180)       # set brightness
cap.set(cv2.CAP_PROP_CONTRAST, 50)          # set contrast

success, img = cap.read()
while success:
    cv2.imshow("Webcam", img)

    # Press ESC key to break the loop
    if cv2.waitKey(10) & 0xFF == 27:
        break
    success, img = cap.read()

cap.release()
cv2.destroyWindow("Webcam")