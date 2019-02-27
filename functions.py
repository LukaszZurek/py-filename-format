#import os, sys

from os import rename, listdir

lista = listdir()

badsigns = ['"', "*", ":", "<", ">","?","/","\\","|"]

def re_allNum():
	filename = input("Write a name that you want to give to all files in this directory: \n")
	for sign in badsigns:
		if sign in filename:
			print("Sorry, {} is not allowed as a sign used in filenames".format(sign))
			re_allNum()
	i = 0
	for file in lista:
		i += 1
		if file == "filenamedraft.py" or file == "__pycache__" or file == "functions.py": #a code that prevents the script from changing *.py filename
			i -= 1
			continue
		dot = file.rfind(".") #saving file's extensions
		getext = slice((dot + 1), len(file))
		fileext = "." + (file[getext])
		dst = filename + str(i) + fileext
		rename(file, dst)

def re_allStartEnd():
	addition = input("Write smt that you want to add:\n")
	for sign in badsigns:
		if sign in addition:
			print("Sorry, {} is not allowed as a sign used in filenames".format(sign))
	startorend = input("Do you want to add smt at the begining [b] or the end [e] of the filenames?\n")
	for file in lista:
		if file == "filenamedraft.py" or file == "__pycache__" or file == "functions.py":
			continue
		if startorend == "b":
			dst = addition + file
			rename(file, dst)
		if startorend == "e":
			dot = file.rfind(".") #saving file's extensions
			getext = slice((dot + 1), len(file))
			fileext = "." + (file[getext])
			filenoext = file.replace(fileext, "") #removing the extension from filename so it won't double
			dst = filenoext + addition + fileext
			rename(file, dst)