""" 19-02-2019 - dev start

Program ma na celu zautomatyzowanie zmiany nazwy wielu plików.
Jeśli np. muszę dodać na końcu nazw kilku plików tekstowych ".red", to będę to mógł zrobić za pomocą tego programu
Albo jeśli chcę, żeby x plików rozpoczynało się od "ŁŻ" - też zrobię to za pomocą programu.

Na początku - niech zmienia nazwy plików, które zostały wrzucone do katalogu z plikiem programu.

Co program będzie mógł robić?
1) wyrzucać listę plików w katalogu
2) umożliwiać dodawanie jakiegoś stringu do nazwy na początku lub na końcu
*3) wspólną zmianę wybranych plików w katalogu, a nie wszystkich

"""
print("*** FILE RENAMER ***")

import os, sys

lista = os.listdir()

printlist = input("Do you want to see the list of all files in the program's directory?[y/n]\n")
if printlist == "y":
	print(lista)