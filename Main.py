import cv2
import numpy as np
cap = cv2.VideoCapture(0)
imgTarget = cv2.imread('1.png')
myVideo = cv2.VideoCapture('Comp.mp4')

success, imgVideo = myVideo.read()
hT,wT,cT = imgTarget.shape
imgVideo = cv2.resize(imgVideo,(wT,hT))

# orb = cv2.ORB_create(nfeatures=1000)
# kp1, des1 = orb.detectAndCompute(imgTarget, None)
# imgTarget = cv2.drawKeypoints(imgTarget,kp1,None)
#while True:
   # success, imgWebcam = cap.read()

cv2.imshow('imgTarget', imgTarget)
cv2.imshow('MyVid', imgVideo)
#cv2.imshow('Webcam', imgWebcam)

cv2.waitKey(0)

