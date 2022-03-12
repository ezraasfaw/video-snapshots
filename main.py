import cv2

# region Read image from default webcam using OpenCV. Pressing ‘s’ takes a snapshot, ‘q’ quits.
video_capture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
file_number = 0
while True:
    return_code, frame = video_capture.read()
    cv2.imshow(‘Output’, frame)
    kp = cv2.waitKey(1) & 0xFF
    if kp == ord(‘s’):
        cv2.imwrite(‘Frame%d.png’ % file_number, frame)
        file_number += 1
    elif kp == ord(‘q’):
        break
# endregion

# region Release the camera resources.
video_capture.release()
cv2.destroyAllWindows()
# endregion
