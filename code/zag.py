#программа установщик
#v0.0.0.2

import os 

def list_of_programs():
	os.chdir(r"..\bashs")
	x = os.listdir()
	print (x)

	

def menu ():
	'''основная функция программы'''
	print ('----ZAG----------------------------------')
	print ("[1] - список программ")
	print ("[2] - найти на устройстве")
	print ("[3] - написать загрузочный файл")
	print ("[4] - самостоятельная установка")
	print ("[5] - история команд")
	print ("[6] - установленые программы")
	print ("[0] - выйти")
	inp = input (": ")

	if inp == "1":
		list_of_programs ()

	elif inp == "2":
		pass

	elif inp == "2":
		pass

	elif inp == "2":
		pass

	elif inp == "2":
		pass

	elif inp == "2":
		pass

	else:
		pass

menu ()
