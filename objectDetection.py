import cv2 
import os 
import matplotlib.pyplot as plt
def imagesSav(image,anchor):
    filename = 'images/savedImage{}.jpg'.format(anchor)
    cv2.imwrite(filename, image)
    
import numpy as np 

def imageExtrctor(filePath):
    video = cv2.VideoCapture(filePath)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    threshold = 110.

    ret, frame1 = video.read()
    prev_frame = frame1

    a = 0
    b = 0
    c = 0

    while True:
        ret, frame = video.read()
        if ret is True:
            if (((np.sum(np.absolute(frame-prev_frame))/np.size(frame)) > threshold)):
                imagesSav(frame , a)
                prev_frame = frame
                a += 1



            c += 1
        else:
            break
    return a

import cv2

def faceExtractor(a,b):
    imageLocation = f"images\savedImage{a}.jpg"
    image = cv2.imread(imageLocation)


    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(image, scaleFactor=1.07, minNeighbors=30)
    c = b
    face = []

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        fileName = 'faces/savedImage{}.jpg'.format(b)
        cv2.resize(face,(240,240))
        cv2.imwrite(fileName, face)
        c = b+1
    
    return [c,face]
   


def faceList():
    a = imageExtrctor(r"temp_file_1.mp4")
    c = 0
    imageList = []
    for i in range(a):
        [c,imageFace] = faceExtractor(i+1,c)
        if(len(imageFace) != 0):
            imageList.append(imageFace)
        
    return imageList


