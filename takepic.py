#! /usr/bin/python
# coding=utf-8

import picamera
import time
import datetime

debug=1
cam = picamera.PiCamera()
cam.resolution = (2592, 1944)
#cam.resolution = (1920, 1080)
#cam.resolution = (800, 600)
cam.rotation = 270
picSavePath='/dev/shm/'
def takePic(picNo):
	newfilename=picSavePath+picNo+'.jpg'
	if debug==1: print("filename: ",newfilename)
	if debug==1: print("time: ",time.time())
	cam.capture(newfilename)