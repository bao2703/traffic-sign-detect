import numpy as np
import cv2
import os

stop_cascade = cv2.CascadeClassifier("cascade/stop_cascade.xml")
left_cascade = cv2.CascadeClassifier("cascade/left_cascade.xml")
right_cascade = cv2.CascadeClassifier("cascade/right_cascade.xml")

KERNEL_SIZE = 3
def gaussian_blur(img):
	return cv2.GaussianBlur(img, (KERNEL_SIZE, KERNEL_SIZE), 0)

def grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def detect(img, i):
    img = cv2.resize(img, (500, 300))
    gray = grayscale(img)
    gaussian = gaussian_blur(gray)
    stop = stop_cascade.detectMultiScale(gaussian)
    #left = left_cascade.detectMultiScale(gray, 1.02, 10)
    #right = right_cascade.detectMultiScale(gray, 1.02, 10)
        
    for (x, y, w, h) in stop:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        print(w)
        print(h)
    #for (x, y, w, h) in left:
    #    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #for (x, y, w, h) in right:
    #    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img

def real_time():
    cap = cv2.VideoCapture('videos/ROBOGAME.mp4')
    i = 0
    while True:
        success, frame = cap.read()        
        if success:
            i += 1
            if i > 1000:
                img = detect(frame, i)
                cv2.imshow('img', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        else:
            print('fail')
            break
    cap.release()
    cv2.destroyAllWindows()

real_time()