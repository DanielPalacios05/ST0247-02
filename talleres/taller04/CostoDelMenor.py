from cmath import inf
import numpy as np
from collections import deque

from sqlalchemy import false
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

def costoDelMenorAUX(graf,start,end):
    seen=[False]*graf.size
    return costoDelMenor(graf,start,end,seen)

def costoDelMenor(graf,start:int,end:int,seen):
    seen[start]=True
    if start==end:
        return 0
    else:
        costoMasCorto=inf
        for vecino in graf.getSuccessors(start):
            if not seen[vecino]:
                costoMenorVecinoEnd=costoDelMenor(graf,vecino,end,seen)
                costoPasandoPorVeciono=graf.getWeight(start,vecino)+costoMenorVecinoEnd
                if costoPasandoPorVeciono<costoMasCorto:
                    costoMasCorto=costoPasandoPorVeciono
        return costoMasCorto

def CaminoMenorAUX(graf,start,end):
    seen=[False]*graf.size
    return CaminoMenor(graf,start,end,seen)

def CaminoMenor(graf,start,end,seen):
    seen[start]=True
    if start==end:
        listaFin=deque()
        listaFin.appendleft(end)
        return (0,listaFin)
    else:
        costoMasCorto=inf
        lista=deque()
        for vecino in graf.getSuccessors(start):
            if not seen[vecino]:
                costoMenorVecinoEnd,listaRetorno=CaminoMenor(graf,vecino,end,seen)
                listaRetorno.appendleft(start)
                costoPasandoPorVeciono=graf.getWeight(start,vecino)+costoMenorVecinoEnd
                if costoPasandoPorVeciono<costoMasCorto:
                    costoMasCorto=costoPasandoPorVeciono
                    lista=listaRetorno
            seen[vecino]=False
        
        return costoMasCorto,lista

def main():
    grafo=GraphAM(7)
    grafo.addArc(0,1,1)
    grafo.addArc(1,2,2)
    grafo.addArc(1,3,1)
    grafo.addArc(2,4,2)
    grafo.addArc(3,4,1)
    grafo.addArc(4,5,1)
    grafo.addArc(5,4,1)
    grafo.addArc(4,6,1)
    print(costoDelMenorAUX(grafo,0,4))
    print(costoDelMenorAUX(grafo,1,4))
    print(CaminoMenorAUX(grafo,0,6))
    print(CaminoMenorAUX(grafo,1,5))
main()

