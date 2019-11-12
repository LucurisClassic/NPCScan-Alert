import os
import sys
import time
import datetime
import subprocess
screenshotsfolder = 'C:\\Program Files (x86)\\World of Warcraft_classic_\\Screenshots'
def eventTrigger(unixtimestamp,filename):
	print ("Detected file %s @ %s" % (os.path.join(screenshotsfolder,"ScreenShot_"+filename+".jpeg"), unixtimestamp))
	if sys.argv[1] == '-Hinterlands':
		filePicker = 'C:\\Users\\lucuris\\Downloads\\NPCscan_Alert\\Hinterlands.py'
	elif sys.argv[1] == '-Ashenvale':
		filePicker = 'C:\\Users\\lucuris\\Downloads\\NPCscan_Alert\\Ashenvale.py'
	elif sys.argv[1] == '-Feralas':
		filePicker = 'C:\\Users\\lucuris\\Downloads\\NPCscan_Alert\\Feralas.py'
	elif sys.argv[1] == '-Duskwood':
		filePicker = 'C:\\Users\\lucuris\\Downloads\\NPCscan_Alert\\Duskwood.py'
	elif sys.argv[1] == '-Kazzak':
		filePicker = 'C:\\Users\\lucuris\\Downloads\\NPCscan_Alert\\Kazzak.py'
	elif sys.argv[1] == '-Azuregos':
		filePicker = 'C:\\Users\\lucuris\\Downloads\\NPCscan_Alert\\Azuregos.py'
	else:
		filePicker = 'C:\\Users\\lucuris\\Downloads\\NPCscan_Alert\\noZoneSpecified.py' 	
	cmd = ['python3',filePicker]
	subprocess.Popen(cmd)

def activeScanner():
	first_ran_time = time.time()
	data = {}
	try:
		while True:
			for file in os.listdir(screenshotsfolder):
				if file.startswith("ScreenShot_") and file.endswith(".jpeg"):
					fndtstr =  file.replace("ScreenShot_",'').replace(".jpeg",'')
					fndt = time.mktime(datetime.datetime.strptime(fndtstr, "%m%d%y_%H%M%S").timetuple())
					if fndt not in data.keys():
						if fndt > first_ran_time:
							data[fndt]=fndtstr				 
							msg = eventTrigger(fndt,fndtstr)
						else:
							#not from this session, ignore
							pass
					else:
						#already know about it, ignore
						pass
	except KeyboardInterrupt:
		pass
def main():
	activeScanner()
if __name__ == '__main__':
	main()








