GeneralSettings={}
GeneralSettings['RunVideo']=True
GeneralSettings['StatusMessage']="initializing..."
GeneralSettings['FrameRate']=30
GeneralSettings['TranslationNo']=0
GeneralSettings['FlushTime']=0
GeneralSettings['InstallPath']='/home/pi/ShelfCam/'
#GeneralSettings['ControlImagePath']='/dev/null'
 
 
 
#guiCommands={}
#guiParams['ObjectDetectVar']=0.0
#guiParams['ImageThreshold']=80
#guiParams['zoom_x1']=50
#guiParams['zoom_x2']=100
#guiParams['zoom_y1']=0
#guiParams['zoom_y2']=100
#guiParams['contour_to_find']=0
#guiParams['ShutterSpeed']=1
#guiParams['ImgPath']='gui_images/red.png'
#guiParams['RecognitionMethod']=1
#guiParams['BoxMax']=[0,0]
#guiParams['BoxMin']=[0,0]
#guiParams['EmptyBoxes']=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#guiParams['MaxObjectArea']=0
 
def preload_settings():
    f = open(str(GeneralSettings['InstallPath'])+'settings.txt', 'r')
    readLine=f.readline()
    f.close()
    GeneralSettingsRead=eval(readLine)
    for k,v in GeneralSettingsRead.items():
        GeneralSettings[k]=v
    #print("gen sett loaded",GeneralSettings) 
     
def load_settings(newType):
    f = open(str(GeneralSettings['InstallPath'])+'settings.txt', 'r')
    readLines=f.readlines()
    f.close()
    #print(" loaded type from file:",GeneralSettings['SelectedType'])
    GeneralSettingsRead=eval(readLines[0])
    for k,v in GeneralSettingsRead.items():
        GeneralSettings[k]=v
    GeneralSettings['SelectedType']=newType
    readDict=eval(readLines[int(GeneralSettings['SelectedType'])])
    #print(" readdict:",readDict)
    #print(" readlines:",readLines[GeneralSettings['SelectedType']])
    for k,v in readDict.items():
        guiParams[k]=v
    #print("gui Params loaded",guiParams)
     
def save_settings(guiCommands):
	print("guiCommands:", guiCommands)
	f = open(str(GeneralSettings['InstallPath'])+'settings.txt', 'w')
	f.write(str(guiCommands)+"\n")
	f.close()
	'''
        f = open(str(GeneralSettings['InstallPath'])+'settings.txt', 'r')
        readLines=f.readlines()
        f.close()
        f = open(str(GeneralSettings['InstallPath'])+'settings.txt', 'w')
        writeDict=guiParams.copy()
        #print("to_save: ",to_save)
        GeneralSettingsSave=GeneralSettings.copy()
        del GeneralSettingsSave['StatusMessage']
        #del GeneralSettingsSave['RunVideo']
        del GeneralSettingsSave['TranslationNo']
        
		#print("all save")
		f.write(str(GeneralSettingsSave)+"\n")
		for i in range(0,GeneralSettings['TotalTypes']):
			if i == GeneralSettings['SelectedType']-1:
				f.write(str(writeDict)+"\n")
				#print("save dict line "+str(i)+" selected: "+str(GeneralSettings['SelectedType'])+" write "+str(writeDict))
			else: 
				f.write(readLines[i+1])
        #f.write(str(guiParams)+"\n")
        f.close()
      '''