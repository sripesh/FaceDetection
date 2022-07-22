# import open-cv
import cv2

# training data using "face.xml"
dataset=cv2.CascadeClassifier('face.xml')

# import the image "one.jpg"
img=cv2.imread('one.jpg')

# convert the image to gray-color image
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# face detection using the trained dataset
faces=dataset.detectMultiScale(grayimg)

# loop to mark the detected faces
for face in faces:
    x,y,w,h=face
    # make the rectangle using the coordinates
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

# displaying all detected face
cv2.imshow('hello',img)

# to make the frame more visible
cv2.waitKey()
