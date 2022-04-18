from collections import deque
from cmath import inf
class GraphAL:
    def __init__(self, size):
        self.size=size
        self.arregloDeListas = [0]*size # = [0,0,0,0...]      
        for i in range(size):
            self.arregloDeListas[i] = deque()

    def addArc(self, source, destination, weight):
        laListaLlegada = self.arregloDeListas[source]
        unaPareja = (destination,weight)
        laListaLlegada.append(unaPareja)

    def getWeight(self, source, destination):
        laListaLlegada = self.arregloDeListas[source]
        '''for i in range(len(laListaLlegada)):
            pareja = laListaLlegada[i] # O(n)       
            theDestination = pareja[0]
            theWeight = pareja[1]
            if theDestination == destination:
                return theWeight'''
        for (theDestination,theWeight) in laListaLlegada:
            if theDestination == destination:
                return theWeight      
        return 0    
    def getSuccessors(self, source):
        otraListica = deque()
        laListaLlegada = self.arregloDeListas[source]
        for (theDestination,theWeight) in laListaLlegada:
            otraListica.append(theDestination) 
        #otraListica = [theDestination for (theDestination,theWeight) in laListaLlegada]
        #otraListica = deque(map(lambda x : x[0],laListaLlegada)) 
        #otraListica = deque(map(f,laListaLlegada)) 
        return otraListica   

def cercano(grafo,nodo,visitados):
    sucesores=grafo.getSuccessors(nodo)
    distancia=inf
    actual=0
    for i in sucesores:
        if grafo.getWeight(nodo,i)<distancia and not visitados[i]:
            distancia=grafo.getWeight(nodo,i)
            actual=i
    return actual

def actualizar(grafo,nodo,distancia,camino):
    for sucesor in grafo.getSuccessors(nodo):
        pesoViaje=grafo.getWeight(nodo,sucesor)
        if distancia[nodo]+pesoViaje < distancia[sucesor]:
            distancia[sucesor]=distancia[nodo]+pesoViaje
            camino[sucesor]=nodo
    #return distancia, camino

def Dijiska(grafo:GraphAL,start):
    distancias=[inf]*grafo.size
    visitado=[False]*grafo.size
    distancias[0]=0
    visitado[0]=True
    camino=[-1]*grafo.size
    nodo=start
    for _ in range(0,grafo.size-1):
        actualizar(grafo,nodo,distancias,camino)
        nodo=cercano(grafo,nodo,visitado)
        visitado[nodo]=True
    return distancias,camino

def main():
    grafo=GraphAL(6)
    grafo.addArc(0,1,2)
    grafo.addArc(0,2,4)
    grafo.addArc(1,2,1)
    grafo.addArc(1,3,7)
    grafo.addArc(2,4,3)
    grafo.addArc(3,5,1)
    grafo.addArc(4,3,2)
    grafo.addArc(4,5,5)
    print(Dijiska(grafo,0))
main()