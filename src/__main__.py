from ctypes.wintypes import RGB
from time import time

import cv2

WINDOW_NAME = "Main"


def empty(x):
    pass


def BrightnessContrast(img, brightness=0):
    # getTrackbarPos returns the current
    # position of the specified trackbar.
    brightness = cv2.getTrackbarPos("Brightness", WINDOW_NAME)
    contrast = cv2.getTrackbarPos("Contrast", WINDOW_NAME)
    effect = controller(img, brightness, contrast)
    # The function imshow displays an image
    # in the specified window
    return effect


def controller(img, brightness=255, contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness

        al_pha = (max - shadow) / 255
        ga_mma = shadow

        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma)
    else:
        cal = img

    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)

        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(cal, Alpha, cal, 0, Gamma)

    # putText renders the specified text string in the image.
    cv2.putText(
        cal,
        "B:{},C:{}".format(brightness, contrast),
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
    )

    return cal


# define a video capture object

camera = cv2.VideoCapture(2)
if not camera.isOpened():
    camera = cv2.VideoCapture(0)

ret, frame = camera.read()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
video_out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

cv2.namedWindow(WINDOW_NAME)

# Brightness range -255 to 255
cv2.createTrackbar("Brightness", WINDOW_NAME, 255, 2 * 255, empty)

# Contrast range -127 to 127
cv2.createTrackbar("Contrast", WINDOW_NAME, 127, 2 * 127, empty)

while True:
    # Capture the video frame by frame
    ret, frame = camera.read()

    # Display the resulting frame
    # cv2.imshow(WINDOW_NAME, frame)
    efect = BrightnessContrast(frame, 0)
    cv2.imshow(WINDOW_NAME, efect)

    video_out.write(frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choicee
    key = cv2.waitKey(1)

    if key & 0xFF == ord("q"):
        break

    # press 's' to capture the photo
    if key & 0xFF == ord("s"):
        cv2.imwrite(f"img/img_{int(time())}.png", efect)
        print(f"saved as img_{int(time())}.png")


video_out.release()
camera.release()
cv2.destroyAllWindows()
