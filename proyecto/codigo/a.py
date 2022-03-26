import pandas as pd
from matrix import Graph
from graphAL import GraphAL
from collections import deque
from math import inf


def caminoCorto(grafo: GraphAL,begin, fin , riesgoMaximo):
    return caminoCortoAux(grafo, begin, fin, riesgoMaximo)

def caminoCortoAux(grafo:GraphAL,begin, fin,riesgoMaximo):
    n=grafo.size
    visitados = [False] * n
    distancias = [inf] * n
    riesgos=[0]*n
    posiciones = [-1] * n
    distancias[begin] = 0

    for i in range(n):
        visitando = -1
        for j in range(n):
            if (not visitados[j]) and (visitando==-1 or distancias[j]<distancias[visitando]):
                visitando=j
        if distancias[visitando]==inf:
            break
        visitados[visitando]=True
        
        for vecino in grafo.getSuccessors(visitando):
            metros=grafo.getWeight(visitando,vecino)
            riesgo=grafo.getRisk(visitando,vecino)
            if riesgos[visitando]+riesgo<riesgoMaximo:
                if distancias[visitando]+metros<distancias[vecino]:
                    distancias[vecino]=distancias[visitando]+metros
                    riesgos[vecino]=riesgos[visitando]+riesgo
                    posiciones[vecino] = visitando
    
    caminar=distancias[fin]
    asalto=riesgos[fin]
    camino=deque()
    actual=fin
    while actual!=begin:
        camino.appendleft(actual)
        actual=posiciones[actual]
    return camino, caminar, asalto

data = pd.read_csv("proyecto\codigo\calles_de_medellin_con_acoso.csv",sep=";", usecols=[0, 1, 2, 3, 4, 5])

arrdata = data.to_numpy()

#print(arrdata)


mapa = GraphAL()


numberofNodes = 0


for i in arrdata:

    if i[1] not in mapa.vertices.keys():
        mapa.vertices[i[1]] = numberofNodes
        numberofNodes = numberofNodes+1
    if i[2] not in mapa.vertices.keys():
        mapa.vertices[i[2]] = numberofNodes
        numberofNodes = numberofNodes+1
        
#print(numberofNodes)

mapa.iniList(numberofNodes)


for i in arrdata:

    if i[4]:
        mapa.addUndirArc(mapa.vertices[i[1]],mapa.vertices[i[2]],(i[0],i[3],i[5]))
    else:
        mapa.addArc(mapa.vertices[i[1]],mapa.vertices[i[2]],(i[0],i[3],i[5]))
        
print(caminoCorto(mapa,0,6,2))
    
    
