from graphAL import GraphAL
from collections import deque
from math import inf


def caminoCorto(grafo: GraphAL,n):
    
    visitados = [False] * grafo.size
    
    return caminoCortoAux(grafo, 0,n,visitados)[0]

def caminoCortoAux(grafo:GraphAL,begin, fin,visitados):
    visitados[begin]=True
    if begin==fin:
        rutaFinal=deque()
        rutaFinal.appendleft(fin)
        #grafo.diccionarioVisita[begin]=False
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
                distanciaActual=float(grafo.getWeight(begin,lugar))+distancia
                if distanciaActual<=distanciaMenor:
                    rutaCorta=rutaPosible
                    distanciaMenor=distanciaActual
                visitados[lugar]=False
        return rutaCorta,distanciaMenor
    
    
    
    
def main():
    entry = list(map(int,input().split(" ")))
    
    vertices = entry[0]
    aristas = entry[1]
    
    
    grafo = GraphAL(vertices)
    
    for _ in range(aristas):
        
        arcEntry = list(map(int,input().split(" ")))

        
        grafo.addUndirArc(arcEntry[0]-1,arcEntry[1]-1, arcEntry[2])
        
        
    print(" ".join(map(lambda x : str(x+1), caminoCorto(grafo,grafo.size-1))))
    
    

        
        
        
        
        
    
    
    
    
if __name__ == '__main__':
    main()   
     