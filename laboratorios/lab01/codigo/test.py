from collections import deque
archivos = open("laboratorios\lab01\codigo\mapa.txt",'r')
archivos = open("laboratorios\lab01\codigo\medellin_colombia-grande.txt",'r')
aristas=deque()
vertices=deque()
a = archivos.readline()
a = archivos.readline()
if a == "\n":
    a=archivos.readline()
while a.strip() != "":
    if len(a.split())== 4:
        añadir=a.split()
    else:
        añadir=a.split()
        añadir.append("Nombre Desconocido")
    vertices.append(añadir)
    a = archivos.readline()
print (vertices)

