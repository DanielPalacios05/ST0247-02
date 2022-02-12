from collections import deque

class Grapho:
    def __init__(self,vertices,aristas):
        self.diccionarioRutas=dict()
        self.diccionarioNombre=dict()
        for vertice in vertices:
            if vertice[0] not in self.diccionarioRutas:
                self.diccionarioRutas[vertice[0]]=deque()
            if vertice[0] not in self.diccionarioNombre:
                self.diccionarioNombre[vertice[0]]=vertice[3]
        self.añadirAristas(aristas)
        self.imprimirGrafo()
        
    def añadirAristas(self,aristas):
        for arista in aristas:
            self.diccionarioRutas[arista[0]].append((arista[1],arista[2]))
    
    def imprimirGrafo(self):
        for i in self.diccionarioRutas:
            print(self.diccionarioNombre[i]+" puede ir a ")
            for vertice in self.diccionarioRutas[i]:
                print("  "+self.diccionarioNombre[vertice[0]]+" y esta a "+vertice[1]+" Km")
            print("-------------------------------------------------------------------------------")



archivos = open("laboratorios\lab01\codigo\mapa.txt",'r')
aristas=deque()
vertices=deque()
a = archivos.readline()
a = archivos.readline()
if a == "\n":
    a=archivos.readline()
while a.strip() != "":
    vertices.append(a.split())
    a = archivos.readline()

a = archivos.readline()
a = archivos.readline()
if a == "\n":
    a=archivos.readline()
while  a.strip() != "":
        aristas.append(a.split())
        a = archivos.readline()

Grapho(vertices,aristas)