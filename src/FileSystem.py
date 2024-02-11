def input_file():
    global data
    print("Masukkan nama file (Pastikan file telah berada di folder test)")
    fileName = input()
    data = []
    with open("../test/"+fileName) as my_file:
        dataTmp = []
        for line in my_file:
            splitedLine = line.split(" ")
            for arr in splitedLine:
                dataTmp.append(arr.rstrip())
            data.append(dataTmp)
            dataTmp = []
    return data
