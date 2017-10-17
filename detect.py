import numpy as np
import cv2
import os
from moviepy.editor import VideoFileClip

s = ''
stop_cascade = cv2.CascadeClassifier("cascade/stop_cascade.xml")
left_cascade = cv2.CascadeClassifier("cascade/left_cascade.xml")
right_cascade = cv2.CascadeClassifier("cascade/right_cascade.xml")

def detect(img, i):
    img = cv2.resize(img, (250, 450))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop = stop_cascade.detectMultiScale(gray, 1.02, 10)
    left = left_cascade.detectMultiScale(gray, 1.02, 10)
    right = right_cascade.detectMultiScale(gray, 1.02, 10)
    global s
    for (x, y, w, h) in stop:
        #cv2.putText(img, 'Stop', (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        s += str(i) + ' 3 \n'
    for (x, y, w, h) in left:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        s += str(i) + ' 1 \n'
    for (x, y, w, h) in right:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        s += str(i) + ' 2 \n'
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
    i = 0
    for image in images :
        i += 1
        print('processing')
        cv2.imwrite(os.path.join('output', '{0}.jpg'.format(i)), image)
    pass

def detect_folder(folder):
    # images = load_images_from_folder(folder)
    # i = 0
    # for image in images:
    #     i += 1
    #     img = detect(image)
    #     cv2.imwrite(os.path.join('output', '{0}.jpg'.format(i)), img)

    for i in range(1, 21):
        img = cv2.imread(os.path.join(folder, '{0}.jpg'.format(i)))
        img = detect(img, i)
        cv2.imwrite(os.path.join('output', '{0}.jpg'.format(i)), img)
    pass

def detect_video(input, output):
    video = VideoFileClip(input)
    output = video.fl_image(detect)
    output.write_videofile(output, audio=False)
    pass

def write(str):
    file = open('output.txt', 'w')
    file.write(str)
    file.close()
    pass

#detect_video('videos/input.avi', 'output.mp4')
#detect_folder('test2')


def real_time():
    cap = cv2.VideoCapture('videos/7.avi')
    i = 0
    while True:
        success, frame = cap.read()        
        if success:
            i += 1
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
print(s)