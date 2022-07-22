# import open-cv
import cv2

# training data using "face.xml"
dataset=cv2.CascadeClassifier('face.xml')

# import the video "two.mp4"
cap = cv2.VideoCapture('two.mp4')

# loop for every frame of catured video
while True:
    # read one frame at a time
    success, image = cap.read()

    # convert the image to gray-color image
    grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # face detection using the trained dataset
    faces=dataset.detectMultiScale(grayimg)

    # loop to mark the detected faces
    for face in faces:
        x,y,w,h=face
        # make the rectangle using the coordinates
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    
    # displaying all detected face in single frame
    cv2.imshow('hello',image)

    # to make the frame move faster
    x=cv2.waitKey(1)

    # to break out of frame loop when 'q' is pressed
    if x == ord('q'):
        break

# release the video variable
cap.release()

# close the windows
cv2.destroyAllWindows()
