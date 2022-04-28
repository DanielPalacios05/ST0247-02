from collections import deque
from sqlite3 import adapt


class GraphAL:
    
    def __init__(self): 
        
        self.diccionarioVisita = {}
        
        self.vertices = {}
        
        self.size = 0
        
        self.adList = None
        
        

        # Array of linked Lists with tuples where ( vertex, weight)

    def checkVertex(self, vertex):

        return 0 <= vertex < self.size
    
    def iniList(self,size):
        
        self.size = size
        
        self.adList = [0]*self.size
        
        for i in range(len(self.adList)):
            self.adList[i] = deque()

    def addArc(self, vertex, vertex2, weight):

        if self.checkVertex(vertex) and self.checkVertex(vertex2):
            self.adList[vertex].append((vertex2, weight[0],weight[1],weight[2]))     # 0 -> (0,nombre,peso,indice))
        else:
            print("Check if the chosen vertex are valid")
            
    def addUndirArc(self, vertex, vertex2, weight):
        
        self.addArc(vertex,vertex2,weight)
        self.addArc(vertex2,vertex,weight)
        
        

    def getSuccessors(self, vertex):
    
        if self.checkVertex(vertex):
            
            list1 = []
        
            vertexSuccesors = self.adList[vertex]
            
            for i in range(len(vertexSuccesors)):
                list1.append(vertexSuccesors[i][0])
                
            return list1

    def getData(self, source, destination):
        
        if self.checkVertex(source) and self.checkVertex(destination):
        
            sourceAdjacent = self.adList[source]
            
            for i in sourceAdjacent:
                
                if i[0] == destination:
                    return i
        
        else:
            print("Check if the chosen vertex are valid")
            
    def getWeight(self,source,destination):
        return self.getData(source,destination)[2]
    
    def getRisk(self,source,destination):
        return self.getData(source,destination)[3]
            

            
            
