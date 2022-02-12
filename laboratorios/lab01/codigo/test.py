with open("codigo\mapa.txt",'r') as archivos:
    a = archivos.readline()

    while a.strip() != "":
        print(a.split())
        a = archivos.readline()

    a = archivos.readline()
    print("==========================edges===========================")

    while  a.strip() != "":
        print(a.split())
        a = archivos.readline()

