import numpy as np
import cv2
import os
from moviepy.editor import VideoFileClip

stop_casade = cv2.CascadeClassifier("cascade/stop_cascade.xml")
left_casade = cv2.CascadeClassifier("cascade/left_cascade.xml")
right_casade = cv2.CascadeClassifier("cascade/right_cascade.xml")

def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop = stop_casade.detectMultiScale(gray, 1.02, 10)
    left = left_casade.detectMultiScale(gray, 1.02, 10)
    right = right_casade.detectMultiScale(gray)
    for (x, y, w, h) in stop:
        if w > 100:
            cv2.putText(img, 'Stop', (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2, cv2.LINE_AA)
            #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    return img

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def rename_files(folder):
    images = load_images_from_folder(folder)
    i = 1318
    for image in images :
        i += 1
        print('processing')
        cv2.imwrite(os.path.join('output', '{0}.jpg'.format(i)), image)
    pass

def detect_folder(folder):
    images = load_images_from_folder(folder)
    i = 0
    for image in images:
        i += 1
        try:
            print('processing')
            image = detect(image)
            cv2.imwrite(os.path.join('output', '{0}.jpg'.format(i)), image)
        except:
            pass
    pass

def detect_video(input, output):
    video = VideoFileClip(input)
    output = video.fl_image(detect)
    output.write_videofile(output, audio=False)
    pass

def detect_image(input, output):
    image = cv2.imread(input)
    image = detect(image)
    cv2.imwrite(output, image)
    pass

def write(str):
    file = open('output.txt', 'w')
    file.write(str)
    file.close()
    pass

#detect_video('videos/input.avi', 'output.mp4')
detect_image('test/stop.jpg', 'output.jpg')
