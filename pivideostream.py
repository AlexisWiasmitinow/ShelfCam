# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread
import cv2

class PiVideoStream:
	def __init__(self, resolution=(1920, 1088)):
		# initialize the camera and stream
		self.camera = PiCamera()
		#resolution=(1296,736)
		self.camera.resolution = resolution
		self.camera.framerate = 5 
		#self.camera.framerate = 49
		self.camera.video_stabilization=False
		self.camera.vflip = True
		#self.camera.rotation = 270
		self.camera.hflip = True
		self.rawCapture = PiRGBArray(self.camera, size=resolution)
		self.stream = self.camera.capture_continuous(self.rawCapture,format="bgr", use_video_port=True)
		#self.camera.sharpness=100
		#self.camera.iso=500
		# initialize the frame and the variable used to indicate
		# if the thread should be stopped
		print("resolution: ",self.camera.resolution)
		self.frame = None
		self.stopped = False

	def start(self):
		# start the thread to read frames from the video stream
		#print("thread started resolution: ", self.camera.resolution)
		t = Thread(target=self.update, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		# keep looping infinitely until the thread is stopped
		for f in self.stream:
			# grab the frame from the stream and clear the stream in
			# preparation for the next frame
			#print("iso", self.camera.iso)
			self.frame = f.array
			self.rawCapture.truncate(0)

			# if the thread indicator variable is set, stop the thread
			# and resource camera resources
			if self.stopped:
				self.stream.close()
				self.rawCapture.close()
				self.camera.close()
				return

	def read(self):
		# return the frame most recently read
		return self.frame

	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True
		
	def SetParam(self):
		self.camera.shutter_speed=500
		self.camera.iso=500
		print("shutter: ",self.camera.shutter_speed)
		print("iso: ",self.camera.iso)
		#self.camera.resolution = resolution
		
	def readCropped(self,x1,y1,x2,y2):
		h,w=self.frame.shape[:2]
		self.cropX1=int(x1*w/100)
		self.cropX2=int((100-x2)*w/100)
		self.cropY1=int(y1*h/100)
		self.cropY2=int((100-y2)*h/100)
		if self.cropX2<self.cropX1:
			self.cropX2=self.cropX1+5
		if self.cropY2<self.cropY1:
			self.cropY2=self.cropY1+5
		self.cropped=self.frame[self.cropY1:self.cropY2, self.cropX1:self.cropX2]
		#print("cropx1: ",self.cropX1)
		#print("cropx2: ",self.cropX2)
		#print("x1: ",x1)
		#print("x2: ",x2)
		#self.cropped=self.frame[10:400, 10:600]
		return self.cropped
		
