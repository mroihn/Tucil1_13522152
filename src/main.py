from FileSystem import *
from Solver import *

print("1. input file atau 2. random")
choice = input()


if choice == "1":
    data = input_file()
    dataParser(data)
    solveFile()
    print("Ingin menyimpan hasil (Y/N)")
    choice = input()
    if choice == "Y":
        saveFile()

if choice == "2":
    inputRand()
    solveFile()
    printMatSeq()
    print("Ingin menyimpan hasil (Y/N)")
    choice = input()
    if choice == "Y":
        saveFile()
