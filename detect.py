import numpy as np
import cv2
import os

s = ''
stop_cascade = cv2.CascadeClassifier("cascade/stop_cascade.xml")
left_cascade = cv2.CascadeClassifier("cascade/left_cascade.xml")
right_cascade = cv2.CascadeClassifier("cascade/right_cascade.xml")

def detect(img, i):
    #img = cv2.resize(img, (1000, 600))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop = stop_cascade.detectMultiScale(gray, 1.02, 10)
    left = left_cascade.detectMultiScale(gray, 1.02, 10)
    right = right_cascade.detectMultiScale(gray, 1.02, 10)
    global s
    for (x, y, w, h) in stop:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        s += str(i) + ' 3\n'
        print(3)
    for (x, y, w, h) in left:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        s += str(i) + ' 1\n'
        print(1)
    for (x, y, w, h) in right:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        s += str(i) + ' 2\n'
        print(2)
    return img

def write(str):
    file = open('output.txt', 'w')
    file.write(str)
    file.close()
    pass

def real_time():
    cap = cv2.VideoCapture('videos/ROBOGAME.mp4')
    i = 0
    while True:
        success, frame = cap.read()        
        if success:
            i += 1
            print(i)
            if i == 686 or i == 687 or i == 688 or i == 812 or i == 814 or i == 880 or i == 882 or i == 890 or i == 1050 or i == 1086:
                img = detect(frame, i)
                cv2.imwrite("{0}.jpg".format(i), img)
                #cv2.imshow('img', img)
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                    #break
        else:
            print('fail')
            break
    cap.release()
    cv2.destroyAllWindows()

real_time()
write(s)