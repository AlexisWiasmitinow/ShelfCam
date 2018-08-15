#!/usr/bin/env python
import cv2
import sys
import time
import RPi.GPIO as GPIO
import datetime
import getopt
#from takepic import *
from upload import *
from threading import Thread
import time, multiprocessing, sys, getopt
import numpy as np
from loadsettings import *
from GUI import *
from contour_operations import ContourOperations
from pivideostream import PiVideoStream

def usage():
	print("usage: -g gui <1/0>")

def guiThread():
	root = Tk()
	root.geometry("800x270+0+0")
	app = Window(root)
	root.mainloop()

def main(argv):	
	vs = PiVideoStream((1296, 736)).start()
	#vs = PiVideoStream((1920, 1088)).start()
	time.sleep(1)
	#todo: crop xy threshold, pipette, mask, contours 
	use_gui=0
	try: 
			opts, args =getopt.getopt(sys.argv[1:], "g:",["gui="])
	except getopt.GetoptError as err:
		usage()
		sys.exit(2)
	#print("opts: ",opts)
	#print("args: ",sys.argv[1:])
	if len(opts)<1:
		use_gui=0
	for o,a, in opts:
		if o=="-g":
			use_gui=int(a)
		
	t_gui=Thread(target=guiThread)
	if use_gui>0: 
		t_gui.start()
	else:
		load_settings()
		#print("set guiCommands nogui:",guiCommands)
		guiCommands['previewRaw']=False
	runVideo=True
	#print("picSavePath: ",picSavePath)
	while (runVideo==True):
		#print("mainloop")
		runVideo=guiCommands['runVideo']
		grabbedFrame = vs.readCropped(guiCommands['cropleft'],guiCommands['croptop'],guiCommands['cropright'],guiCommands['cropbottom'])
		np.asarray(grabbedFrame)
		Live=ContourOperations()
		Live.split_colors(grabbedFrame)
		
		#redOnly=Live.computeRedMinusGB()
		#Live.computeThreshold(redOnly, guiCommands['threshold'])
		#frame = vs.read()
		#print("threshold:",guiCommands['threshold'])
		#print("Type grabbedFrame",grabbedFrame.name)
		if guiCommands['previewRaw']==True: 
			cv2.imshow('All',grabbedFrame)
			#cv2.imshow('RedOnly',redOnly)
			red=Live.showRed(False)
			#print("Type grabbedFrame",grabbedFrame.dtype())
			green=Live.showGreen(False)
			blue=Live.showBlue(False)
			#cv2.imshow('Red-Green',red-green)
			#cv2.imshow('Red-Blue',red-blue)
			#cv2.imshow('Red-Blue-Green',red-blue-green)
			Live.showPixelValue(cv2.subtract(cv2.subtract(red,blue),green),60,95, 'r-b-g')
			Live.showPixelValue(red-blue,60,95, 'r-b')
			Live.showPixelValue(red,60,95, 'r')
			Live.showPixelValue(red-green,60,95, 'r-g')
			red[95][60]=red[95][60]-65
			Live.showPixelValue(red,60,95, 'r new')
			Live.showPixelValue(red-green,60,95, 'r-g new')
			
		else:
			cv2.destroyAllWindows()
		if cv2.waitKey(1) & 0xFF == ord('q'):
			runVideo=False
			break
		#time.sleep(0.1)
		#runVideo=False
		
if __name__ == "__main__":
    main(sys.argv[1:])