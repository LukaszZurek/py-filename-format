""" 19-02-2019 - dev start

Program ma na celu zautomatyzowanie zmiany nazwy wielu plików.
Jeśli np. muszę dodać na końcu nazw kilku plików tekstowych "_red", to będę to mógł zrobić za pomocą tego programu
Albo jeśli chcę, żeby x plików rozpoczynało się od "ŁŻ_" - też zrobię to za pomocą programu.

Na początku - niech zmienia nazwy plików, które zostały wrzucone do katalogu z plikiem programu.

Co program będzie mógł robić?
1) wyrzucać listę plików w katalogu - done
2) zmieniać nazwę wszystkich plików w katalogu z rosnącą numeracją
3) umożliwiać dodawanie jakiegoś stringu do nazwy na początku lub na końcu
	- czyli zachowuję starą nazwę, ale dodaję coś do niej na końcu/na początku
4) wspólną zmianę wybranych plików w katalogu, a nie wszystkich
	- iterowanie poprzez range() (np. od pliku 1 do 10)

"""
print("*** FILE RENAMER ***")

import os, sys

index = -1

lista = os.listdir()


def re_allNum(): #wersja dla zmiany nazw plików o tym samym rozszerzeniu
	fileext = input("What is the MUTUAL file extension of the files that you want to rename? [e.g .txt] \n")
	filename = input("Write a name that you want to give to all files in this directory: \n")
	i = 0
	for file in lista:
		dst = filename + str(i) + fileext
		os.rename(file, dst)
		if file == "filenamedraft.py": #trying to prevent a program from changing its own filename
			break
			
printlist = input("Do you want to see the list of all files in the program's directory? [y/n]\n")
if printlist == "y":
	for i in lista:
		index += 1
		print(str(index) + ") " + i)
else:
	break

allfiles = input("Do you want to change ALL FILENAMES in the program's directory? [y/n]\n")
if allfiles == "y":
	#ścieżka programu ze zmianą wszystkich plików
if allfiles == "n":
	#ścieżka programu z wybraniem kilku plików