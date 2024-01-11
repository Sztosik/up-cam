from ctypes.wintypes import RGB
from time import time

import cv2

# define a video capture object
camera = cv2.VideoCapture(0)

ret, frame = camera.read()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

while True:
    # Capture the video frame by frame
    ret, frame = camera.read()

    # Display the resulting frame
    cv2.imshow("frame", frame)

    video_out.write(frame)


    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choicee
    key = cv2.waitKey(1)

    if key & 0xFF == ord("q"):
        break

    # press 's' to capture the photo
    if key & 0xFF == ord("s"):
        cv2.imwrite(f"img/img_{int(time())}.png", frame)
        print(f"saved as img_{int(time())}.png")

        

video_out.release()
camera.release()
cv2.destroyAllWindows()