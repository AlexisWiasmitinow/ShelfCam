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
	if use_gui>0: t_gui.start()
	runVideo=True
	#print("picSavePath: ",picSavePath)
	while (runVideo==True):
		#print("mainloop")
		runVideo=guiCommands['runVideo']
		grabbedFrame = vs.readCropped(20,36,44,15)
		Live=ContourOperations()
		Live.split_colors(grabbedFrame)
		#frame = vs.read()
		#print("shape:",frame.shape[:2])
		if guiCommands['previewRaw']==True: 
			cv2.imshow('All',grabbedFrame)
			Live.showRed()
			Live.showGreen()
			Live.showBlue()
		else:
			cv2.destroyAllWindows()
		if cv2.waitKey(1) & 0xFF == ord('q'):
			runVideo=False
			break
		#time.sleep(0.1)
		#runVideo=False
		
if __name__ == "__main__":
    main(sys.argv[1:])