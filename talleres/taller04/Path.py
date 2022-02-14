

import numpy as np
from collections import deque
class GraphAM:#AM significa con matrizes de adyacencia
    def __init__(self, size):
        self.size=size
        self.__Array__=np.zeros((size,size))

    def addArc(self, vertex, edge, weight):
        self.__Array__[vertex][edge]=weight

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

def pathAUX(grafo,inicio:int,fin:int):
    Visitados=[False]*grafo.size #guardar los visitados
    return path(grafo,inicio,fin,Visitados)

def path(grafo,inicio:int,meta:int,Visitados):
    Visitados[inicio]=True #marcar el que ya visite
    if inicio==meta:
        return True
    else:
        for vecino in grafo.getSuccessors(inicio): #por cada sucesor
            if not Visitados[vecino]:#si no se ha visitado
                delVecinoAMeta=path(grafo,vecino,meta,Visitados)
                if delVecinoAMeta:
                    return True
    return False

def main():
    grafo=GraphAM(5)
    grafo.addArc(0,1,5)
    grafo.addArc(0,2,2)
    grafo.addArc(2,3,1)
    grafo.addArc(3,3,1)
    grafo.addArc(3,0,1)
    grafo.addArc(3,4,1)
    print(pathAUX(grafo,0,4))
    print(pathAUX(grafo,1,4))
main()