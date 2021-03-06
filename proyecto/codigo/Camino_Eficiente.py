import pandas as pd
from matrix import Graph
from graphAL import GraphAL
from collections import deque
from math import inf
import time


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
        if (actual==-1):
            camino = deque()
            break
    return camino, caminar, asalto

def caminoSeguro(grafo: GraphAL,begin, fin , distanciaMaximo):
    return caminoSeguroAux(grafo, begin, fin, distanciaMaximo)

def caminoSeguroAux(grafo:GraphAL,begin, fin,distanciaMaximo):
    n=grafo.size
    visitados = [False] * n
    distancias = [0] * n
    riesgos=[inf]*n
    posiciones = [-1] * n
    riesgos[begin] = 0

    for i in range(n):
        visitando = -1
        for j in range(n):
            if (not visitados[j]) and (visitando==-1 or riesgos[j]<riesgos[visitando]):
                visitando=j
        if riesgos[visitando]==inf:
            break
        visitados[visitando]=True
        for vecino in grafo.getSuccessors(visitando):
            metros=grafo.getWeight(visitando,vecino)
            riesgo=grafo.getRisk(visitando,vecino)
            if distancias[visitando]+metros<distanciaMaximo:
                if riesgos[visitando]+riesgo<riesgos[vecino]:
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
        if (actual==-1):
            camino = deque()
            break
    return camino, caminar, asalto

#data = pd.read_csv("calles_de_medellin_con_acoso.csv",sep=";", usecols=[0, 1, 2, 3, 4, 5])

#arrdata = data.to_numpy()

#print(arrdata)
arrdata = pd.read_csv("proyecto\codigo\calles_de_medellin_con_acoso.csv",sep=";", usecols=[0, 1, 2, 3, 4, 5])

mapa = GraphAL()


numberofNodes = 0

for i in range(len(arrdata)):
    if arrdata["origin"][i] not in mapa.vertices.keys():
        mapa.vertices[arrdata["origin"][i]] = numberofNodes
        numberofNodes = numberofNodes+1
    if arrdata["destination"][i] not in mapa.vertices.keys():
        mapa.vertices[arrdata["destination"][i]] = numberofNodes
        numberofNodes = numberofNodes+1      
#print(numberofNodes)
mapa.iniList(numberofNodes)

for i in range(len(arrdata)):
    if arrdata["oneway"][i]:
        mapa.addUndirArc(mapa.vertices[arrdata["origin"][i]],mapa.vertices[arrdata["destination"][i]],(arrdata["name"][i],arrdata["length"][i],arrdata["harassmentRisk"][i]))
    else:
        mapa.addArc(mapa.vertices[arrdata["origin"][i]],mapa.vertices[arrdata["destination"][i]],(arrdata["name"][i],arrdata["length"][i],arrdata["harassmentRisk"][i]))


start=time.time()
print(caminoCorto(mapa,8462,11296,100))
print(caminoSeguro(mapa,8462,11296,8000))
end=time.time()
print(end-start)
print("--------------------------------------------------------------------------")
start=time.time()
print(caminoCorto(mapa,2199,1112,45))
print(caminoSeguro(mapa,2199,1112,7000))
end=time.time()
print(end-start)
print("--------------------------------------------------------------------------")
start=time.time()
print(caminoCorto(mapa,1112,1413,10))
print(caminoSeguro(mapa,1112,1413,6500))
end=time.time()
print(end-start)
print("--------------------------------------------------------------------------")