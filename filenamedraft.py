""" 19-02-2019 - dev start

Program ma na celu zautomatyzowanie zmiany nazwy wielu plików.
Jeśli np. muszę dodać na końcu nazw kilku plików tekstowych "_red", to będę to mógł zrobić za pomocą tego programu
Albo jeśli chcę, żeby x plików rozpoczynało się od "ŁŻ_" - też zrobię to za pomocą programu.

Na początku - niech zmienia nazwy plików, które zostały wrzucone do katalogu z plikiem programu.

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

index = -1

lista = os.listdir()

def re_allNum():
	fileext = input("What is the MUTUAL file extension of the files that you want to rename? [e.g .txt] \n")
	filename = input("Write a name that you want to give to all files in this directory: \n")
	i = -1
	for file in lista:
		i += 1
		if file == "filenamedraft.py": #a code that prevents the script from changing *.py filename
			i -= 1
			continue
		dst = filename + str(i) + fileext
		os.rename(file, dst)
		

def re_allStartEnd():
	fileext = input("What is the MUTUAL file extension of the files that you want to rename? [e.g .txt] \n") #it's a bit WET now... I will use fleep.py in future to determine file extension automatically
	filenamestart = input("Write smt that you want to add:\n")
	startorend = input("Do you want to add smt to the begining [b] or the end [e] of the filenames?\n")
	for file in lista:
		if file == "filenamedraft.py":
			continue
		if startorend == "b":
			dst = filenamestart + file + fileext
			os.rename(file, dst)
		if startorend == "e":
			dst = file + filenamestart + fileext
			os.rename(file, dst)

printlist = input("Do you want to see the list of all files in the program's directory (in short: PD)? [y/n]\n")
if printlist == "y":
	for i in lista:
		index += 1
		print(str(index) + ") " + i)
if printlist == "n":
	None

allfiles = input("Do you want to change ALL FILENAMES in the PD? [y/n]\n")
if allfiles == "y":
	allfilesoptions = input("Here's a list of functions that can change all files that you've copied into the PD:\n(1) Same name - different number (e.g. text1, text2, text3)\n(2) Add smtn at the begining/end of the filename (e.g. James_essay, James_notes, James_diary)\n(3) tbc\n")
	if allfilesoptions == "1":
		re_allNum()
	if allfilesoptions == "2":
		re_allStartEnd()
if allfiles == "n":
	print("tbc")
	#ścieżka programu z wybraniem kilku plików