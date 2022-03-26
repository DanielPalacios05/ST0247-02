import pandas as pd
from matrix import Graph
from graphAL import GraphAL
from collections import deque
from math import inf

data = pd.read_csv("proyecto\codigo\calles_de_medellin_con_acoso.csv",
                   sep=";", usecols=[0, 1, 2, 3, 4, 5])

arrdata = data.to_numpy()


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
         


    
    
def caminoCorto(grafo: GraphAL,inicio,final,riesgoMaximo):
    
    
    
    return caminoCortoAux(grafo, inicio,final,riesgoMaximo)[0]

def caminoCortoAux(grafo:GraphAL,begin, fin,riesgoMaximo):
    visitados = [False] * grafo.size
    visitados[begin]=True
    distancias = [inf] * grafo.size
    posiciones = [-1] * grafo.size
    distancias[begin] = 0
    v = -1

    for i in range(n):
        v = -1
        for j in range(n):
            if not 

    