import os
import shutil

#path = "C:\\Users\\Desktop  for windows
#path = "C:/Desktop" for linux
#destine = "C:\\Tdestine\\" for windows
#destine = "C:/Tdestine/" for linux
numb = 0
path = "D:\\Pastero IMAGERO\\09"
destine = "D:\\Destine\\"


# creates dir
def dir_makero(destine):
	os.mkdir(destine)


# transfers files from one dir to the created one
def transfer(destine, list, fit):
	fi = 0
	for fileros in list:
		shutil.move(path + "\\" + fileros, destine)
		# shutil.move(path + "/" + fileros, destine) # for linux
		fi += 1
		if fi == fit:
			break


def runmento(path, destine, fit, dirNumber = 0):
	list_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))] # lists all files
	control = destine # destination path
	numbe = dirNumber # number of files per directory
	destine = destine + str(numbe)
	print("Destination "+destine)
	x = len(list_files)
	while x != 0:
		numbe += 1
		destine = control + str(numbe)
		print("index "+destine)
		dir_makero(destine)
		transfer(destine, list_files, fit)
		list_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
		x = len(list_files)
		print("Number of files remaining " + str(x))


runmento(path, destine, 40) # runs script - last param may be blank
