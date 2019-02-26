""" 19-02-2019 - dev start

Co program będzie mógł robić?
1) wyrzucać listę plików w katalogu - done (19-02-2019)
2) zmieniać nazwę wszystkich plików w katalogu z rosnącą numeracją - done (20-02-2019)
3) umożliwiać dodawanie jakiegoś stringu do nazwy na początku lub na końcu - done (20-02-2019)
	- czyli zachowuję starą nazwę, ale dodaję coś do niej na końcu/na początku
x) usunięcie określonych znaków z nazwy
4) wspólną zmianę wybranych plików w katalogu, a nie wszystkich
	- iterowanie poprzez range() (np. od pliku 1 do 10)

"""
print("*** FILE RENAMER by Łukasz Żurek (2019) ***")

import os, sys

index = 0

lista = os.listdir()

print("LIST OF FILES IN THE PROGRAM DIRECTORY (in short - PD):\n")

for i in lista:
	index += 1
	print(str(index) + ") " + i)

def re_allNum():
	filename = input("Write a name that you want to give to all files in this directory: \n")
	i = -1
	for file in lista:
		i += 1
		if file == "filenamedraft.py": #a code that prevents the script from changing *.py filename
			i -= 1
			continue
		dot = file.rfind(".") #saving file's extensions
		getext = slice((dot + 1), len(file))
		fileext = "." + (file[getext])
		dst = filename + str(i) + fileext
		os.rename(file, dst)
		
def re_allStartEnd():
	filenamestart = input("Write smt that you want to add:\n")
	startorend = input("Do you want to add smt at the begining [b] or the end [e] of the filenames?\n")
	for file in lista:
		if file == "filenamedraft.py":
			continue
		if startorend == "b":
			dst = filenamestart + file + fileext
			os.rename(file, dst)
		if startorend == "e":
			dst = file + filenamestart + fileext
			os.rename(file, dst)

allfiles = input("Do you want to change ALL FILENAMES in the PD? [y/n]\n")
if allfiles == "y":
	allfilesoptions = input("Here's a list of functions that can change all files's names that you've copied into the PD:\n(1) Same name - different number (e.g. text1, text2, text3)\n(2) Add smtn at the begining/end of the filename (e.g. James_essay, James_notes, James_diary)\n(3) tbc\n")
	if allfilesoptions == "1":
		re_allNum()
	if allfilesoptions == "2":
		re_allStartEnd()
if allfiles == "n":
	print("tbc")
	#ścieżka programu z wybraniem kilku plików