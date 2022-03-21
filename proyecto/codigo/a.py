import pandas as pd
from matrix import Graph
from graphAL import GraphAL
from collections import deque
from math import inf


def caminoCorto(grafo: GraphAL,n):
    
    visitados = [False] * grafo.size
    
    return caminoCortoAux(grafo, 0,n,visitados)

def caminoCortoAux(grafo:GraphAL,begin, fin,visitados):
    visitados[begin]=True
    if begin==fin:
        rutaFinal=deque()
        rutaFinal.appendleft(fin)
        return (rutaFinal,0)
    else:
        distanciaMenor=inf
        rutaCorta=deque()
        for lugar in grafo.getSuccessors(begin):
            
            if not visitados[lugar]:
                par=caminoCortoAux(grafo,int(lugar),fin,visitados)
                rutaPosible=par[0]
                distancia=par[1]
                rutaPosible.appendleft(begin)
                distanciaActual=grafo.getWeight(begin,lugar)+distancia
                if distanciaActual<=distanciaMenor:
                    rutaCorta=rutaPosible
                    distanciaMenor=distanciaActual
                visitados[lugar]=False
        return rutaCorta,distanciaMenor
    
    
    
    

data = pd.read_csv("proyecto\codigo\calles_de_medellin_con_acoso.csv",
                   sep=";", usecols=[0, 1, 2, 3, 4, 5])

arrdata = data.to_numpy()

print(arrdata)


mapa = GraphAL()


numberofNodes = 0


for i in arrdata:

    if i[1] not in mapa.vertices.keys():
        mapa.vertices[i[1]] = numberofNodes
        numberofNodes = numberofNodes+1
    if i[2] not in mapa.vertices.keys():
        mapa.vertices[i[2]] = numberofNodes
        numberofNodes = numberofNodes+1
        
print(numberofNodes)

mapa.iniList(numberofNodes)


for i in arrdata:

    if i[4]:
        mapa.addUndirArc(mapa.vertices[i[1]],mapa.vertices[i[2]],(i[0],i[3],i[5]))
    else:
         mapa.addArc(mapa.vertices[i[1]],mapa.vertices[i[2]],(i[0],i[3],i[5]))
         
print(caminoCorto(mapa,1))
    
    
