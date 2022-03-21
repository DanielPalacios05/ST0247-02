from collections import deque


class GraphAL:
    
    def __init__(self, size):
        
        
        self.size = size
        self.adList = [0]*size
        
        for i in range(len(self.adList)):
            self.adList[i] = deque()
        

        # Array of linked Lists with tuples where ( vertex, weight)

    def checkVertex(self, vertex):

        return 0 <= vertex < self.size

    def addArc(self, vertex, vertex2, weight):

        if self.checkVertex(vertex) and self.checkVertex(vertex2):
            self.adList[vertex].append((vertex2, weight))
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

    def getWeight(self, source, destination):
        
        if self.checkVertex(source) and self.checkVertex(destination):
        
            sourceAdjacent = self.adList[source]
            
            for i in sourceAdjacent:
                
                if i[0] == destination:
                    return i[1]
        
        else:
            print("Check if the chosen vertex are valid")
