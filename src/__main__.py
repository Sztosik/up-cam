import cv2

# define a video capture object
camera = cv2.VideoCapture(0)

while True:
    # Capture the video frame by frame
    ret, frame = camera.read()

    # Display the resulting frame
    cv2.imshow("frame", frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choicee
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) == ord("s"):
        cv2.imwrite('image.png', frame)

camera.release()
cv2.destroyAllWindows()
