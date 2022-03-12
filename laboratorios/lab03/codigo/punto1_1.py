from collections import deque
from cmath import inf
class GraphAl:
    def __init__(self,vertices,aristas):
        self.diccionarioRutas=dict()
        self.diccionarioNombre=dict()
        self.diccionarioVisita=dict()
        self.size=len(vertices)
        for vertice in vertices:
            if vertice[0] not in self.diccionarioRutas:
                self.diccionarioRutas[vertice[0]]=deque()
            if vertice[0] not in self.diccionarioNombre:
                self.diccionarioNombre[vertice[0]]=vertice[3]
            if vertice[0] not in self.diccionarioVisita:
                self.diccionarioVisita[vertice[0]]=False
        self.añadirAristas(aristas)
        
    def añadirAristas(self,aristas):
        for arista in aristas:
            self.diccionarioRutas[arista[0]].append((arista[1],arista[2]))
    
    def getSuccessors(self,vertice):
        sucesores=[]
        for i in self.diccionarioRutas[str(vertice)]:
            sucesores.append(i[0])
        return sucesores

    def getWeight(self,source:str,destination:str):
        for vertice in self.diccionarioRutas[source]:
            if vertice[0] == destination:
                return vertice[1]

    def imprimirGrafo(self):
        for i in self.diccionarioRutas:
            print(self.diccionarioNombre[i]+" puede ir a ")
            for vertice in self.diccionarioRutas[i]:
                print("  "+self.diccionarioNombre[vertice[0]]+" y esta a "+vertice[1]+" Km")
            print("-------------------------------------------------------------------------------")


def caminoCorto(grafo:GraphAl,begin, fin):
    grafo.diccionarioVisita[begin]=True
    if begin==fin:
        rutaFinal=deque()
        rutaFinal.appendleft(fin)
        #grafo.diccionarioVisita[begin]=False
        return (rutaFinal,0)
    else:
        distanciaMenor=inf
        rutaCorta=deque()
        for lugar in grafo.getSuccessors(begin):
            
            if not grafo.diccionarioVisita[lugar]:
                par=caminoCorto(grafo,lugar,fin)
                rutaPosible=par[0]
                distancia=par[1]
                rutaPosible.appendleft(str(begin))
                distanciaActual=float(grafo.getWeight(str(begin),str(lugar)))+distancia
                if distanciaActual<=distanciaMenor:
                    rutaCorta=rutaPosible
                    distanciaMenor=distanciaActual
                grafo.diccionarioVisita[lugar]=False
        return rutaCorta,distanciaMenor

archivos = open("puentesColgantes.txt",'r')
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

a = archivos.readline()
a = archivos.readline()
if a == "\n":
    a=archivos.readline()
while  a.strip() != "":
        aristas.append(a.split())
        a = archivos.readline()

grafo=GraphAl(vertices,aristas)
print(grafo.getSuccessors('3'))
print(caminoCorto(grafo,'1','4'))
archivos.close
