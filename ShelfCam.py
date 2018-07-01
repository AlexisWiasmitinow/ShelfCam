#!/usr/bin/env python
import cv2
import sys
import time
import RPi.GPIO as GPIO
import time
import datetime
import getopt
#from takepic import *
from upload import *
from threading import Thread
import time, multiprocessing, sys, getopt
import numpy as np
from GUI import *
from pivideostream import PiVideoStream
vs = PiVideoStream((1920, 1088)).start()
time.sleep(1)


def guiThread():
	root = Tk()
	root.geometry("800x270+0+0")
	app = Window(root)
	root.mainloop()

t_gui=Thread(target=guiThread)
t_gui.start()
runVideo=True


#print("picSavePath: ",picSavePath)
while (runVideo==True):
	#print("mainloop")
	runVideo=guiCommands['runVideo']
	frame = vs.readCropped(20,36,44,15)
	#frame = vs.read()
	#print("shape:",frame.shape[:2])
	cv2.imshow('Test',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		runVideo=False
		break
	#time.sleep(0.1)
	