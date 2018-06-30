import requests
import os

def upload(picNo,picSavePath):
	newfilename=picSavePath+picNo+'.jpg'
	print("start upload of: ",newfilename)
	URL = 'http://alexis.wiasmitinow.ch/uploads/upload.php'
	files = {'upfile' : open(newfilename, 'rb')}
	r = requests.post(URL, files = files)
	print(r.text)
	
def DeleteImages():
	os.system("rm /dev/shm/*.jpg")