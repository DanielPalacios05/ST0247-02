import numpy as np

class Graph:
    
    def __init__(self):
        self.vertices = {}
        self.matrix = None
    
    def addUndirArc(self,ini,fin):
        
        self.matrix[ini][fin] = 1
        self.matrix[fin][ini] = 1
        
    def adddirArc(self,ini,fin):
        self.matrix[ini][fin] = 1
        
    def iniMatrix(self,nodes):
        
        self.matrix = np.empty((nodes,nodes), dtype = np.object)
        
        
        
   