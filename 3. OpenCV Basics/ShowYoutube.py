#
# Show a video from youtube link.
# need to install package: pafy, youtube_dl
#
import cv2
import pafy

# Specify an Youtube video URL
url = "https://www.youtube.com/watch?v=a3ICNMQW7Ok"
video = pafy.new(url)
best = video.getbest(preftype="mp4")
cap = cv2.VideoCapture()
cap.open(best.url)

success, img = cap.read()
while success:
    cv2.imshow("Youtube", img)

    # Press ESC key to break the loop
    if cv2.waitKey(10) & 0xFF == 27:
        break
    success, img = cap.read()

cap.release()
cv2.destroyWindow("Youtube")


