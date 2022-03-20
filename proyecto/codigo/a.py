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
    
    visitados = [False] * grafo.size
    
    return caminoCortoAux(grafo, inicio,final,visitados,riesgoMaximo)[0]

def caminoCortoAux(grafo:GraphAL,begin, fin,visitados,riesgoMaximo):
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
                trio=caminoCortoAux(grafo,int(lugar),fin,visitados)
                rutaPosible=trio[0]
                distancia=trio[1]
                rutaPosible.appendleft(begin)
                distanciaActual=float(grafo.getWeight(begin,lugar))+distancia
                riesgoActual = 0;
                if distanciaActual<=distanciaMenor:
                    rutaCorta=rutaPosible
                    distanciaMenor=distanciaActual
                visitados[lugar]=False
        return rutaCorta,distanciaMenor,riesgoActual
    
    