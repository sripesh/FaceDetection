# FaceDetection
Face detection in image, video or camera using python and open-cv.

face.xml can be obtained from [GitHub](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).

In [faceDetection_img.py](https://github.com/sripesh/FaceDetection/blob/main/faceDetection_img.py) the imported ***one.jpg*** needs to be replaced by the *src* of the image on which face detection needs to be run.

In [faceDetection_vid.py](https://github.com/sripesh/FaceDetection/blob/main/faceDetection_vid.py) the imported <emp>two.mp4</emp> needs to be replaced by the *src* of the video on which face detection needs to be run.

In [faceDetection_cam.py](https://github.com/sripesh/FaceDetection/blob/main/faceDetection_cam.py) if camera is not opening, then try to change the argument of the function `VideoCapture()`.