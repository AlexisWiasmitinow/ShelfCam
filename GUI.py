# coding: utf-8
from Tkinter import *
from loadsettings import *
#from ActorsControl import *
from threading import Thread
#from PIL import Image, ImageTk
import Queue
import string
import time
from multiprocessing import Process, Value, Queue

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
		guiCommands=load_settings()
		self.loadSettings()
		
	#Creation of init_window
	def init_window(self):   
			self.master.title("ShelfCam Configuration")
			# allowing the widget to take the full space of the root window
			self.pack(fill=BOTH, expand=1)
			slider_Length=200
			SetRow=0
			#test=Label(self, text="First")
			#test.grid(row=0)
			#self.forwardDist=StringVar()
			#Entry(self,textvariable=self.forwardDist,width=4).grid(row=SetRow, column=2)
			#self.forwardDist.set("1000")
			#Button(self, text="Vor", command=lambda: self.moveTo("forward")).grid(row=SetRow, column=3)
			#Button(self, text="Hoch", command=lambda: self.lookTo(2)).grid(row=SetRow, column=6)
			self.threshold = Scale(self, orient='horizontal', from_=0, to=255, length=slider_Length, command=self.update)
			self.threshold.grid(row=SetRow, column=0, columnspan=2)
			self.threshold.set(0)
			self.thresholdLabel=Label(self, text="Schwellwert")
			self.thresholdLabel.grid(row=SetRow, column=2)
			self.croptop = Scale(self, orient='horizontal', from_=0, to=95, length=slider_Length, command=self.update)
			self.croptop.grid(row=SetRow, column=7, columnspan=2)
			self.croptop.set(0)
			self.croptopLabel=Label(self, text="Zuschnitt Oben")
			self.croptopLabel.grid(row=SetRow, column=9)
			SetRow+=1
			
			self.lowerhue = Scale(self, orient='horizontal', from_=0, to=255, length=slider_Length, command=self.update)
			self.lowerhue.grid(row=SetRow, column=0, columnspan=2)
			self.lowerhue.set(0)
			self.lowerhueLabel=Label(self, text="Hue Limit Unten")
			self.lowerhueLabel.grid(row=SetRow, column=2)
			self.upperhue = Scale(self, orient='horizontal', from_=0, to=255, length=slider_Length, command=self.update)
			self.upperhue.grid(row=SetRow, column=3, columnspan=2)
			self.upperhue.set(0)
			self.upperhueLabel=Label(self, text="Hue Limit Oben")
			self.upperhueLabel.grid(row=SetRow, column=6)
			self.cropbottom = Scale(self, orient='horizontal', from_=0, to=95, length=slider_Length, command=self.update)
			self.cropbottom.grid(row=SetRow, column=7, columnspan=2)
			self.cropbottom.set(0)
			self.cropbottomLabel=Label(self, text="Zuschnitt Unten")
			self.cropbottomLabel.grid(row=SetRow, column=9)
			SetRow+=1
			
			self.lowersat = Scale(self, orient='horizontal', from_=0, to=255, length=slider_Length, command=self.update)
			self.lowersat.grid(row=SetRow, column=0, columnspan=2)
			self.lowersat.set(0)
			self.lowersatLabel=Label(self, text="Sat Limit Unten")
			self.lowersatLabel.grid(row=SetRow, column=2)
			self.uppersat = Scale(self, orient='horizontal', from_=0, to=255, length=slider_Length, command=self.update)
			self.uppersat.grid(row=SetRow, column=3, columnspan=2)
			self.uppersat.set(0)
			self.uppersatLabel=Label(self, text="Sat Limit Oben")
			self.uppersatLabel.grid(row=SetRow, column=6)
			self.cropleft = Scale(self, orient='horizontal', from_=0, to=95, length=slider_Length, command=self.update)
			self.cropleft.grid(row=SetRow, column=7, columnspan=2)
			self.cropleft.set(0)
			self.cropleftLabel=Label(self, text="Zuschnitt Links")
			self.cropleftLabel.grid(row=SetRow, column=9)
			SetRow+=1
			
			self.lowerval = Scale(self, orient='horizontal', from_=0, to=255, length=slider_Length, command=self.update)
			self.lowerval.grid(row=SetRow, column=0, columnspan=2)
			self.lowerval.set(0)
			self.lowervalLabel=Label(self, text="Val Limit Unten")
			self.lowervalLabel.grid(row=SetRow, column=2)
			self.upperval = Scale(self, orient='horizontal', from_=0, to=255, length=slider_Length, command=self.update)
			self.upperval.grid(row=SetRow, column=3, columnspan=2)
			self.upperval.set(0)
			self.uppervalLabel=Label(self, text="Val Limit Oben")
			self.uppervalLabel.grid(row=SetRow, column=6)
			self.cropright = Scale(self, orient='horizontal', from_=0, to=95, length=slider_Length, command=self.update)
			self.cropright.grid(row=SetRow, column=7, columnspan=2)
			self.cropright.set(0)
			self.croprightLabel=Label(self, text="Zuschnitt Rechts")
			self.croprightLabel.grid(row=SetRow, column=9)
			SetRow+=1
			SetCol=0
			self.takePicText=StringVar()
			Button(self, textvariable=self.takePicText, command=self.takePic).grid(row=SetRow, column=SetCol,columnspan=2)
			self.takePicText.set("Bild Speichern")
			SetCol+=2
			#self.autoRollText=StringVar()
			#Button(self, textvariable=self.autoRollText, command=self.autoRollSwitch).grid(row=SetRow, column=SetCol,columnspan=2)
			#self.autoRollText.set("Rollen")
			SetCol+=2
			self.SaveText=StringVar()
			Button(self, textvariable=self.SaveText, command=self.saveSettings).grid(row=SetRow, column=SetCol,columnspan=2)
			self.SaveText.set("Einstellungen Speichern")
			SetCol+=2
			self.previewText=StringVar()
			Button(self, textvariable=self.previewText, command=self.previewSwitch).grid(row=SetRow, column=SetCol,columnspan=2)
			self.previewText.set("Vorschau")
			SetCol+=2
			#SetRow+=1
			#SetCol=0
			Button(self, text="Beenden", command=self.client_exit).grid(row=SetRow, column=SetCol,columnspan=2)
	def saveSettings(self):
		save_settings(guiCommands);
		
	def loadSettings(self):
		self.upperhue.set(guiCommands['upperhue'])
		self.lowerhue.set(guiCommands['lowerhue'])
		self.upperval.set(guiCommands['upperval'])
		self.lowerval.set(guiCommands['lowerval'])
		self.uppersat.set(guiCommands['uppersat'])
		self.lowersat.set(guiCommands['lowersat'])
		self.croptop.set(guiCommands['croptop'])
		self.cropbottom.set(guiCommands['cropbottom'])
		self.cropleft.set(guiCommands['cropleft'])
		self.cropright.set(guiCommands['cropright'])
		self.threshold.set(guiCommands['threshold'])
			
	def previewSwitch(self):
		guiCommands['previewRaw']= not guiCommands['previewRaw']
		print("preview Status",guiCommands['previewRaw'])
		if guiCommands['previewRaw']==True:
			self.previewText.set("Vorschau Aus")
		else:
			self.previewText.set("Vorschau An")
			
	def takePic(self):
		guiCommands['takePic'] = True
	'''		
	def lightSwitch(self):
		guiCommands['light']= not guiCommands['light']
		print("light Status",guiCommands['light'])
		if guiCommands['light']==True:
			lightOn()
			self.lightText.set("Licht Aus")
		else:
			lightOff()
			self.lightText.set("Licht An")
	def autoServoSwitch(self):
		guiCommands['autoServo']= not guiCommands['autoServo']
		print("autoServo Status",guiCommands['autoServo'])
		if guiCommands['autoServo']==True:
			self.autoServoText.set("Schau Aus")
		else:
			self.autoServoText.set("Schauen")
			
	def autoRollSwitch(self):
		guiCommands['autoRoll']= not guiCommands['autoRoll']
		print("autoRoll Status",guiCommands['autoRoll'])
		if guiCommands['autoRoll']==True:
			self.autoRollText.set("Roll Aus")
		else:
			self.autoRollText.set("Rollen")
			guiCommands['emptyCommandQueue']=True
	def autoTurnSwitch(self):
		guiCommands['autoTurn']= not guiCommands['autoTurn']
		print("autoTurn Status",guiCommands['autoTurn'])
		if guiCommands['autoTurn']==True:
			self.autoTurnText.set("Dreh Aus")
		else:
			self.autoTurnText.set("Drehen")
			guiCommands['emptyCommandQueue']=True
	'''
	def lookTo(self,command):
		print("before look to: ",guiCommands['angle'])
		guiCommands['angle']+=command
		lookTo(guiCommands['angle'])
		print("look to: ",guiCommands['angle'])
		
	

	def update(self,value):
		guiCommands['croptop']=self.croptop.get()
		guiCommands['cropbottom']=self.cropbottom.get()
		guiCommands['cropleft']=self.cropleft.get()
		guiCommands['cropright']=self.cropright.get()
		guiCommands['threshold']=self.threshold.get()
		guiCommands['upperhue']=self.upperhue.get()
		guiCommands['lowerhue']=self.lowerhue.get()
		guiCommands['upperval']=self.upperval.get()
		guiCommands['lowerval']=self.lowerval.get()
		guiCommands['uppersat']=self.uppersat.get()
		guiCommands['lowersat']=self.lowersat.get()

	def client_exit(self):
		guiCommands['runVideo']=False
		print("exit pressed")
		time.sleep(1)
		#SetLightTo(0)
		exit()
