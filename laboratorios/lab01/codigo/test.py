archivos = open("laboratorios\lab01\codigo\mapa.txt",'r')
a = archivos.readline()
a = archivos.readline()
a = archivos.readline()
while a.strip() != "":
    print(a.split())
    a = archivos.readline()

a = archivos.readline()
a = archivos.readline()
a = archivos.readline()
while  a.strip() != "":
        print(a.split())
        a = archivos.readline()


