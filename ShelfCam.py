#!/usr/bin/env python
import cv2
import sys
import time
import RPi.GPIO as GPIO
import time
import datetime
import getopt
from takepic import *
from upload import *

switchPin=21
voltagePin=16
picNo=0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(voltagePin,GPIO.OUT)
GPIO.output(voltagePin, True)
GPIO.setup(switchPin,GPIO.IN)
lastValue=0
picDelay=1
lastTime=0
print("picSavePath: ",picSavePath)
while True:
	now=time.time()
	value = GPIO.input(switchPin)
	#print("we read: ",value)
	#if value==1 and lastValue==0:
	if value==1 and now-lastTime>=picDelay:
		print("take picNo: ",picNo)
		takePic(str(picNo).zfill(3))
		picNo=picNo+1
		lastTime=now
	elif value==0 and lastValue==1:
		print("last picNo: ",picNo)
		if now-lastTime>=picDelay:
			upload(str(picNo-1).zfill(3),picSavePath)
			DeleteImages()
		else:
			upload(str(picNo-2).zfill(3),picSavePath)
			DeleteImages()
	lastValue=value
	if value==0: time.sleep(0.1)