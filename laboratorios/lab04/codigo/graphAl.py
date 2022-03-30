from cmath import inf
from collections import deque

class GraphAl:
    def __init__(self,vertices,aristas):
        
        self.diccionarioVertices = {}
        self.diccionarioIndices = {}

        self.diccionarioRutas= {}
        
        self.diccionarioNombre= {}
        
        self.size=len(vertices)
        
        
        for vertice in vertices:
            if vertice[0] not in self.diccionarioRutas:
                self.diccionarioRutas[vertice[0]]=deque()
            if vertice[0] not in self.diccionarioNombre:
                self.diccionarioNombre[vertice[0]]=vertice[3]
        self.añadirAristas(aristas)
        
        
        for indice,valor in enumerate(self.diccionarioNombre.keys()):
            
            self.diccionarioVertices[indice] = valor
            self.diccionarioIndices[valor] = indice
            
            
            
            
        
        
        
    def añadirAristas(self,aristas):
        for arista in aristas:
            self.diccionarioRutas[arista[0]].append((arista[1],arista[2]))
    
    def getSuccessors(self,vertice):
        sucesores=[]
        for i in self.diccionarioRutas[vertice]:
            sucesores.append(i[0])
        return sucesores

    def getWeight(self,source,destination):
        
        if source == destination:
            return 0
        
        if destination not in self.getSuccessors(source):
            
            return inf
            
        
        for vertice in self.diccionarioRutas[source]:
            if vertice[0] == destination:
                return float(vertice[1])

    def imprimirGrafo(self):
        for i in self.diccionarioRutas:
            print(self.diccionarioNombre[i]+" puede ir a ")
            for vertice in self.diccionarioRutas[i]:
                print("  "+self.diccionarioNombre[vertice[0]]+" y esta a "+vertice[1]+" Km")
            print("-------------------------------------------------------------------------------")



    



