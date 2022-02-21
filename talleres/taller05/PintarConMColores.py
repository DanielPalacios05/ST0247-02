from cmath import inf
import numpy as np
from collections import deque
class GraphAM:#AM significa con matrizes de adyacencia
    def __init__(self, size):
        self.size=size
        self.__Array__=np.zeros((size,size))

    def addArc(self, vertex, edge, weight):
        self.__Array__[vertex][edge]=weight

    def addDiArc(self, vertex, edge, weight):
        self.__Array__[vertex][edge]=weight
        self.__Array__[edge][vertex]=weight

    def getSuccessors(self, vertice):
        sucesor=deque()
        for i in range (0,self.size):
            if self.__Array__[vertice][i]!=0:
                sucesor.append(i)
        return sucesor

    def getWeight(self, source, destination):
        return self.__Array__[source][destination]
    
    def __str__(self):
        return str(self.__Array__)

def bienPintado(arreglo,grafo):
    prueba=False
    for i in range (0,len(arreglo)):
        prueba=pintadoHastaI(arreglo,i,grafo)
    return prueba

def pintadoHastaI(Colores:list,i:int,grafo)->bool:
    for vertice in  range(0,i+1):
        ColorActual=Colores[vertice]
        for sucesor in grafo.getSuccessors(vertice):
            if sucesor<=i:
                ColorSucesor=Colores[sucesor]
                if ColorActual==ColorSucesor:
                    return False
    return True

def pintadosConM_AUX(grafo,numeroDeColores):
    pintadosConM(grafo,[0]*grafo.size,numeroDeColores,0)

def pintadosConM(grafo,colores,numeroDeColores,indice):
    if indice==len(colores):
        print(colores)
        return True
    for color in range (0,numeroDeColores):
        colores[indice]=color
        if pintadoHastaI(colores,indice,grafo):
            puedeSeguir=pintadosConM(grafo,colores,numeroDeColores,indice+1)
            """if puedeSeguir:
                return True
    return False"""

def pintadosConM_One_AUX(grafo,numeroDeColores):
    return pintadosConM_One(grafo,[0]*grafo.size,numeroDeColores,0)


def pintadosConM_One(grafo,colores,numeroDeColores,indice):
    if indice==len(colores):
        print(colores)
        return True
    for color in range (0,numeroDeColores):
        colores[indice]=color
        if pintadoHastaI(colores,indice,grafo):
            puedeSeguir=pintadosConM_One(grafo,colores,numeroDeColores,indice+1)
            if puedeSeguir:
                return True
    return False

def main():
    grafo=GraphAM(7)
    grafo.addDiArc(0,1,1)
    grafo.addDiArc(1,3,2)
    grafo.addDiArc(1,6,1)
    grafo.addDiArc(2,3,2)
    grafo.addDiArc(2,4,1)
    grafo.addDiArc(2,5,1)
    grafo.addDiArc(3,6,1)
    grafo.addDiArc(4,6,1)
    grafo.addDiArc(4,5,1)
    #print(bienPintado([1, 2, 1, 0, 2, 0, 1],grafo))
    #print(bienPintado([2, 0, 0, 2, 2, 1, 1],grafo))
    #print(bienPintado([2, 0, 2, 1, 1, 0, 2],grafo))
    print(pintadosConM_One_AUX(grafo,3))
    print(pintadosConM_One_AUX(grafo,2))
    print(pintadosConM_AUX(grafo,3))
    print(pintadosConM_AUX(grafo,2))
    #pintadosConM_AUX(grafo,3)
main()