from FileSystem import *
from Solver import *
import os

os.system("cls")
print("Pilih Cara Input")
print("1. Input File atau 2. Random")
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
    printMatSeq()
    solveFile()
    print("Ingin menyimpan hasil (Y/N)")
    choice = input()
    if choice == "Y":
        saveFileRandom()
