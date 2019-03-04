print("*** FILE RENAMER by Łukasz Żurek (2019) ***")

import functions

index = 0

print("LIST OF FILES IN THE PROGRAM'S FOLDER (in short - PF):\n")

for i in functions.lista:
	if i == "filenamedraft.py" or i == "__pycache__" or i == "functions.py":
		continue
	index += 1
	print(str(index) + ") " + i)

allfilesoptions = input("Here's a list of functions that can change all files's names that you've copied into the PF:\n(1) Same name - different number (e.g. text1, text2, text3)\n(2) Add smtn at the begining/end of the filename (e.g. James_essay, James_notes, James_diary)\n")
if allfilesoptions == "1":
	functions.re_allNum()
if allfilesoptions == "2":
	functions.re_allStartEnd()