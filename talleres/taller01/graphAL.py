from collections import deque
from re import S
import numpy as np


class GraphAL:
    
    def __init__(self, size):

        self.adList = []
        
        for i in range(size):
            self.adList.append(deque())
    
        self.size = size

        # Array of linked Lists with tuples where ( vertex, weight)

    def checkVertex(self, vertex):

        return 0 <= vertex < self.size

    def addArc(self, vertex, vertex2, weight):

        if self.checkVertex(vertex) and self.checkVertex(vertex2):
            self.adList[vertex].append((vertex2, weight))
        else:
            print("Check if the chosen vertex are valid")

    def getSuccessors(self, vertex):
    
        if self.checkVertex(vertex):
            
            list1 = []
        
            vertexSuccesors = self.adList[vertex]
            
            for i in range(len(vertexSuccesors)):
                list1.append(vertexSuccesors[i][0])
                
            return list1

    def getWeight(self, source, destination):
        
        if self.checkVertex(source) and self.checkVertex(destination):
        
            sourceAdjacent = self.adList[source]
            
            for i in sourceAdjacent:
                
                if i[0] == destination:
                    return i[1]
        
        else:
            print("Check if the chosen vertex are valid")
            
            
            

def __main__():
    grafo=GraphAL(3)
    grafo.addArc(0,1,5)
    grafo.addArc(0,2,2)
    grafo.addArc(1,2,1)
    grafo.addArc(1, 1, 9)
    print(grafo.getSuccessors(0))
    print(grafo.getSuccessors(1))
    print(grafo.getWeight(1,1))
__main__()
