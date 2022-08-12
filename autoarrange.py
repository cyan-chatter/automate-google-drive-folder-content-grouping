import os
import shutil
basepath = "."
dirs = [d for d in os.listdir(basepath) if os.path.isdir(d) and d[:6]=="Algo++"]
finalfoldername = "algovids"
groupbasepath = os.path.join(basepath,finalfoldername)
if finalfoldername not in os.listdir(basepath):
	os.mkdir(groupbasepath)
rn=0
for odir in dirs:
	for odir2 in os.listdir(os.path.join(basepath,odir)):
		rn += 1
		basedirpath = os.path.join(basepath,odir,odir2)
		for dir in os.listdir(basedirpath):
			src = os.path.join(basedirpath,dir)
			if os.path.isdir(src):
				dest = os.path.join(groupbasepath,dir)
				if dir not in os.listdir(groupbasepath):
					os.mkdir(dest)
				for filename in os.listdir(src):
					file = os.path.join(src,filename)
					shutil.copy2(file,dest)
					print(f"File: {filename} Copied from {src} to {dest}")
			else:
				dest = os.path.join(groupbasepath,"Misc")
				if "Misc" not in os.listdir(groupbasepath):
					os.mkdir(dest)
				shutil.copy(src,dest)
				print(f"File: {src} Copied to {dest}")
		print(f"Copy Round {rn} Complete Successfully")






