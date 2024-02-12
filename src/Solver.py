import os
import random
import time

from Cell import Cell

Paths = []
seqAns = []
maxVal = 0
rowAns = []
colAns = []
runtime = 0
buffMax = 0
matWidth = 0
matHeight = 0
arr = []
numbSeq = 0
seqVal = []
sequences = []
totalToken = 0
tokens = []
maxLenSeq = 0
cekSeq = []


def dataParser(data):
    global buffMax, matWidth, matHeight, arr, numbSeq, seqVal, sequences
    buffMax = int(data[0][0])
    matWidth = int(data[1][0])
    matHeight = int(data[1][1])
    arr = []
    arrTmp = []
    cnt = 2
    cntCol = 0

    for i in range(matHeight):
        for j in range(matWidth):
            arrTmp.append(Cell(i + 1, j + 1, False, data[cnt][cntCol]))
            cntCol += 1
        arr.append(arrTmp)
        arrTmp = []
        cnt += 1
        cntCol = 0

    numbSeq = int(data[cnt][0])
    cnt += 1
    seqVal = []
    sequences = []
    arrTmp = []
    for i in range(numbSeq):
        for j in range(len(data[cnt])):
            arrTmp.append(data[cnt][j])
        sequences.append(arrTmp)
        arrTmp = []
        cnt += 1
        seqVal.append(int(data[cnt][0]))
        cnt += 1


def saveFile():
    print("Masukkan nama file output : ")
    filename = input()
    f = open("../test/" + filename, "w")
    f.write(str(maxVal))
    f.write("\n")
    for seq in seqAns:
        f.write(seq + " ")
    f.write("\n")
    for j in range(len(rowAns)):
        f.write(str(colAns[j]) + "," + str(rowAns[j]) + "\n")
    f.write("\n")
    f.write("{:.2f} ms".format(runtime))
    f.close()


def saveFileRandom():
    print("Masukkan nama file output : ")
    filename = input()
    f = open("../test/" + filename, "w")
    f.write(str(maxVal))
    f.write("\n")
    for seq in seqAns:
        f.write(seq + " ")
    f.write("\n")
    for j in range(len(rowAns)):
        f.write(str(colAns[j]) + "," + str(rowAns[j]) + "\n")
    f.write("\n" + "Random Matrix" + "\n")
    for i in range(matHeight):
        for j in range(matWidth):
            f.write(str(arr[i][j].value) + " ")
        f.write("\n")
    f.write("\n" + "Random Sequences and Reward" + "\n")
    for i in range(numbSeq):
        for j in range(len(sequences[i])):
            f.write(str(sequences[i][j]) + " ")
        f.write("\n")
        f.write(str(seqVal[i]) + "\n")

    f.write("\n")
    f.write("{:.2f} ms".format(runtime))
    f.close()


def inputRand():
    global totalToken, tokens, buffMax, matWidth, matHeight, numbSeq, maxLenSeq
    totalToken = int(input("Masukkan jumlah token unik : "))
    token = input("Masukkan token (Pisahkan dengan spasi) : ")
    tokens = token.split()
    buffMax = int(input("Masukkan ukuran buffer : "))
    print("Masukkan ukuran matrix")
    matHeight = int(input("Ukuran baris : "))
    matWidth = int(input("Ukuran kolom : "))
    numbSeq = int(input("Masukkan jumlah sekuens : "))
    maxLenSeq = int(input("Masukkan ukuran maksimal sekuens : "))
    generateRand()


def isUnique(arr):
    if len(sequences) == 0:
        return True
    for i in range(len(sequences)):
        if arr == sequences[i]:
            return False
    return True


def generateRand():
    global arr, seqVal, sequences
    arrTmp = []
    for i in range(matHeight):
        for j in range(matWidth):
            arrTmp.append(Cell(i + 1, j + 1, False, random.choice(tokens)))
        arr.append(arrTmp)
        arrTmp = []

    arrTmp = []
    for i in range(numbSeq):
        cekUniq = False
        while not cekUniq:
            for j in range(random.randint(1, maxLenSeq)):
                arrTmp.append(random.choice(tokens))
            if isUnique(arrTmp):
                cekUniq = True
            else:
                arrTmp = []
        sequences.append(arrTmp)
        arrTmp = []
        seqVal.append(random.randint(1, 100))


def printMatSeq():
    print("Random Matrix")
    for i in range(matHeight):
        for j in range(matWidth):
            print(arr[i][j].value, end=" ")
        print("")
    print("")
    print("Random Sequences and Reward")
    for i in range(numbSeq):
        for j in range(len(sequences[i])):
            print(sequences[i][j], end=" ")
        print("")
        print(seqVal[i])
    print("")


def resetArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j].visited = False


def solve(arr, sequences):
    for i in range(len(arr)):
        compareArr(arr[i], sequences)


def resetCekSeq(sequences):
    global cekSeq
    cekSeq = []
    for i in range(len(sequences)):
        cekSeq.append(False)


def compareArr(arr, sequences):
    global maxVal, seqAns, rowAns, colAns, ans
    resetCekSeq(sequences)
    ans = 0
    for i in range(len(sequences)):
        for j in range(len(arr)):
            if arr[j].value == sequences[i][0]:
                cek = True
                a = 0
                b = j
                while cek and b < len(arr) and a < len(sequences[i]):
                    if arr[b].value != sequences[i][a]:
                        cek = False
                    a += 1
                    b += 1
                if a == len(sequences[i]) and cek and (not cekSeq[i]):
                    ans += seqVal[i]
                    cekSeq[i] = True
                if ans > maxVal or (ans == maxVal and len(arr) < len(seqAns)):
                    seqAns = []
                    rowAns = []
                    colAns = []
                    maxVal = ans
                    for x in range(len(arr)):
                        seqAns.append(arr[x].value)
                        rowAns.append(arr[x].row)
                        colAns.append(arr[x].column)


def Visit(row, col, cnt, path, visitRow, buffMax, arr):
    global Paths
    cellNow = arr[row][col]
    cellNow.visited = True
    path.append(cellNow)
    Paths.append(path.copy())

    if cnt == buffMax - 1:
        Paths.append(path.copy())
        cellNow.visited = False
        path.pop()
        return
    else:
        limit = len(arr) if visitRow else len(arr[0])

        for i in range(limit):
            if visitRow:
                if arr[i][col].visited:
                    continue
                Visit(i, col, cnt + 1, path, False, buffMax, arr)
            else:
                if arr[row][i].visited:
                    continue
                Visit(row, i, cnt + 1, path, True, buffMax, arr)

    cellNow.visited = False
    path.pop()


def solveFile():
    start = time.time()

    for i in range(matWidth):
        resetArr(arr)
        Visit(0, i, 0, [], True, buffMax, arr)
    solve(Paths, sequences)

    print("Output : ")
    print(maxVal)
    for seq in seqAns:
        print(seq, end=" ")
    print("")
    for j in range(len(rowAns)):
        print(colAns[j], ",", rowAns[j])
    end = time.time()
    print("")
    print("")
    global runtime
    runtime = (end - start) * 1000
    print("{:.2f} ms".format(runtime))
