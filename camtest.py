#!/usr/bin/env python
# coding=utf-8
import cv2
import time
#from settings import *
#from picamera.array import PiRGBArray
#from picamera import PiCamera
from pivideostream import PiVideoStream
vs = PiVideoStream((1920, 1088)).start()
time.sleep(1)
#time.sleep(3)
runVideo=True
#vs.SetParam()
while (runVideo==True):
#for i in range(0,3): 
	frame = vs.readCropped(20,36,44,15)
	#frame = vs.read()
	#qprint("shape:",frame.shape[:2])
	cv2.imshow('Test',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		runVideo=False
		break
	time.sleep(0.1)
	#runVideo=False