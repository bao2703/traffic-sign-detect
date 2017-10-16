import numpy as np
import cv2
import os
from moviepy.editor import VideoFileClip

classifier = cv2.CascadeClassifier("classifier/stop-classifier.xml")

def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_signs = classifier.detectMultiScale(gray, 1.02, 10)
    for (x, y, w, h) in stop_signs:
        cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 255), 2)
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
    i = 1115
    for image in images :
        i += 1
        print('processing')
        cv2.imwrite(os.path.join('output', '{0}.jpg'.format(i)), image)
    pass

# images = load_images_from_folder('images')
# i = 0
# for image in images :
#     i += 1
#     try:        
#         print('processing')
#         image = detect(image)
#         cv2.imwrite(os.path.join('output', '{0}.jpg'.format(i)), image)
#     except:
#         pass
#     pass

# video = VideoFileClip("videos/input.avi")
# output = video.fl_image(detect)
# output.write_videofile("output.mp4", audio=False)

rename_files('negatives')