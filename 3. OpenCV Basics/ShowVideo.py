#
# Show a video from local file
#
import cv2

cap = cv2.VideoCapture("../res/Sample Videos from Windows.mp4")

success, img = cap.read()
while success:
    cv2.imshow("Video", img)

    # Press ESC key to break the loop
    if cv2.waitKey(15) & 0xFF == 27:
        break
    success, img = cap.read()

cap.release()
cv2.destroyWindow("Video")