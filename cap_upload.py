#! /usr/bin/python
# coding=utf-8
import time, sys
import picamera
#import ftplib
import requests

cam = picamera.PiCamera()
cam.resolution = (2592, 1944)
#cam.resolution = (1920, 1080)
#cam.resolution = (800, 600)
cam.rotation = 90
#nummer = 1
#newfilename=['bild02%d.jpg' % nummer]
newfilename='/dev/shm/bild.jpg'

def upload():
	#session = ftplib.FTP ('login-156.hoststar.ch' , 'uploads' , 'Safe4uploads?' )
	#directory = "/"
	#session.cwd(directory)
	#file = open('newfilename' , 'rb')
	#session.storbinary('STOR newfilename' , file)
	#file.close()
	#session.quit()
	URL = 'http://alexis.wiasmitinow.ch/uploads/upload.php'
	files = {'upfile' : open(newfilename, 'rb')}
	r = requests.post(URL, files = files)

	print(r.text) 
	return
	
try:
    while True:
		cam.capture(newfilename)
		
		#nummer += 1
		print("image captured")
		#if nummer==11:
		#	nummer=1
		URL = 'http://alexis.wiasmitinow.ch/uploads/upload.php'
		files = {'upfile' : open(newfilename, 'rb')}
		r = requests.post(URL, files = files)
		print(r.text)
		time.sleep(5)
		#upload()
		#else:	
			#upload()
		
except KeyboardInterrupt:
	cam.close()
	sys.exit()