#!/usr/bin/env python
import cv2
import sys
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


def usage():
	print("usage: -g gui <1/0> -s sim <1/0>")
	#simulation mode is for non- raspberry pi computers...

def guiThread():
	root = Tk()
	root.geometry("1000x1000+0+0")
	app = Window(root)
	root.mainloop()

def main(argv):	
	#todo: crop xy threshold, pipette, mask, contours 
	use_gui=0
	simulate=0
	try: 
			opts, args =getopt.getopt(sys.argv[1:], "g:s:",["gui=","sim="])
	except getopt.GetoptError as err:
		usage()
		sys.exit(2)
	#print("opts: ",opts)
	#print("args: ",sys.argv[1:])
	if len(opts)<1:
		use_gui=0
		simulate=0
	for o,a, in opts:
		if o=="-g":
			use_gui=int(a)
		elif o=="-s":
			simulate=int(a)
		
	t_gui=Thread(target=guiThread)
	if use_gui>0: 
		t_gui.start()
	else:
		load_settings()
		#print("set guiCommands nogui:",guiCommands)
		guiCommands['previewRaw']=False
	if simulate==0:
		import RPi.GPIO as GPIO
		from pivideostream import PiVideoStream
		#vs = PiVideoStream((1296, 736)).start()
		vs = PiVideoStream((1920, 1080)).start()
		time.sleep(2)
	runVideo=True
	imageCounter=0
	#print("picSavePath: ",picSavePath)
	while (runVideo==True):
		#print("mainloop")
		runVideo=guiCommands['runVideo']
		if simulate==0:
			grabbedFrame = vs.readCropped(guiCommands['cropleft'],guiCommands['croptop'],guiCommands['cropright'],guiCommands['cropbottom'])
		else:
			grabbedFrame=cv2.imread("images/image_001.png", -1)
			#runVideo=False
		if guiCommands['takePic']==True and simulate==0:
			filename="images/image_"+str(imageCounter).zfill(3)+".png"
			cv2.imwrite(filename, grabbedFrame)
			imageCounter+=1
			guiCommands['takePic']=False
		Live=ContourOperations()
		frame_hsv= cv2.cvtColor(grabbedFrame,cv2.COLOR_BGR2HSV)
		lower_red=np.array([guiCommands['lowerhue'],guiCommands['lowersat'],guiCommands['lowerval']])
		upper_red=np.array([guiCommands['upperhue'],guiCommands['uppersat'],guiCommands['upperval']])
		mask=cv2.inRange(frame_hsv, lower_red, upper_red)
		filtered= cv2.bitwise_and(grabbedFrame, grabbedFrame, mask=mask)
		blue, green, red = cv2.split(grabbedFrame)
		background=cv2.imread("background/image_000.png", -1)
		#bluebg, greenbg, redbg = cv2.split(grabbedFrame)
		#redOnly=Live.computeRedMinusGB(grabbedFrame)
		#red_Threshold=Live.computeThreshold(redOnly, guiCommands['threshold'])
		#redThresContour=red_Threshold.copy()
		contour_ext=Live.get_selected_contour(mask, 0)
		
		if guiCommands['previewRaw']==True: 
			cv2.imshow('All',grabbedFrame)
			cv2.imshow('Mask',mask)
			cv2.imshow('Filtered',filtered)
			#cv2.imshow('All-BG',cv2.subtract(grabbedFrame,background))
			Live.showContour(grabbedFrame, contour_ext)
			#cv2.imshow('red',red_Threshold)
			#cv2.imshow('RedOnly',redOnly)
			'''
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
			'''
		else:
			cv2.destroyAllWindows()
		if cv2.waitKey(1) & 0xFF == ord('q'):
			runVideo=False
			break
		#time.sleep(5)
		#time.sleep(1)
		#print("loop")
		#runVideo=False
		
if __name__ == "__main__":
    main(sys.argv[1:])