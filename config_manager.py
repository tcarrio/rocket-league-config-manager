import os, sys
import subprocess as sp
import time

class SettingManager:
	def __init__(self,monitors='1'):
		self.monitors=monitors
		self.def_config="TASystemSettings.ini"
		self.conf_folder="C:\\Users\\tom\\Documents\\My Games\\Rocket League\\TAGame\\Config"
		if(self.monitors=='1'):
			self.config_file="TASystemSettings - 1440p.ini"
		elif(self.monitors=='2'):
			self.config_file="TASystemSettings - Dual1080.ini"
		else:
			self.config_file=""
	def write_config(self):
		with open(os.path.join(self.conf_folder,self.config_file),'r') as i:
			target_conf=os.path.join(self.conf_folder,self.def_config)
			os.remove(target_conf)
			with open(target_conf,'w') as o:
				for line in i:
					o.write(line)
				o.close()
		i.close()
		return

if __name__=="__main__":
	if len(sys.argv)>1:
		man = SettingManager(sys.argv[1])
	else:
		man = SettingManager()
	man.write_config()