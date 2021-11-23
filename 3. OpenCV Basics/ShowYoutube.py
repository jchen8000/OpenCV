#
# Show a youtube video
# need to install package: pafy, youtube_dl
#
import cv2
import pafy

def list_streams(streams):
    for i, stream in enumerate(streams):
        print(i, stream)

def show_video(stream, title, waitTime=10):
    cap = cv2.VideoCapture()
    cap.open(stream.url)
    success, img = cap.read()
    while success:
        cv2.imshow(title, img)
        # Press ESC key to break the loop
        if cv2.waitKey(waitTime) & 0xFF == 27:
            break
        success, img = cap.read()
    cap.release()
    cv2.destroyWindow(title)

if __name__ == "__main__":
    # Specify an Youtube video URL
    url = "https://www.youtube.com/watch?v=a3ICNMQW7Ok"
    video = pafy.new(url)

    # List the video streams
    list_streams(video.videostreams)

    # Show the best stream
    best_stream = video.getbest(preftype="mp4")
    show_video(best_stream, "Youtube Best Stream", 1)

    # Show a selected stream
    stream_426_240 = video.videostreams[5]
    show_video(stream_426_240, "Youtube Stream with 426x240", 50)