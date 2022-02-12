import numpy as np

class Graph:
    
    def __init__(self, nodes):
        
        self.matrix = np.zeros((nodes,nodes))
        self.colors = [None]*nodes
    
    def addUndirArc(self,ini,fin):
        
        self.matrix[ini][fin] = 1
        self.matrix[fin][ini] = 1
        
        
    def coloreable(self):
        
        self.colors[0] = True
        
        
        matrixlen = len(self.matrix)
        
        for i in range(matrixlen):
            prueba = not self.colors[i]
            
            for j in range(matrixlen):
                
                if self.matrix[i][j] !=0:
                    if self.colors[j]!= None and self.colors[j]!= prueba:
                            print("NOT BICOLORABLE")
                            return False
                    else:
                        self.colors[j] = prueba
                        
                        
                        
        print("COLOREABLE")
            
        
        
    