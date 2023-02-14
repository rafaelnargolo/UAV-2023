import cv2

webcam = cv2.VideoCapture(0)
if webcam.isOpened():
    b, frame = webcam.read()
    while b:
        b, frame = webcam.read()
        cv2.imshow('imagem', frame)
        key = cv2.waitKey(5)
        if key == 27:
            b = False
            cv2.destroyAllWindows()