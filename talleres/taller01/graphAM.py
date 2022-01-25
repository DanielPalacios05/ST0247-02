import numpy as np
from collections import deque

class GraphAM:

    def __init__(self, size):
        self.size = size
        self.adMatrix = np.zeros((size, size))

    def addArc(self, source, destination, weight):

        self.adMatrix[source][destination] = weight

    def getSuccessors(self, vertice):

        succesors = deque()

        for i in range(self.size):
            
            if self.adMatrix[vertice][i] != 0:
                succesors.append(i)

        return succesors

    def getWeight(self, source, destination):

        return self.adMatrix[source][destination]


def __main__():
    grafo=GraphAM(3)
    grafo.addArc(0,1,5)
    grafo.addArc(0,2,2)
    grafo.addArc(1,2,1)
    grafo.addArc(1, 1, 9)
    print(grafo.getSuccessors(0))
    print(grafo.getSuccessors(1))
    print(grafo.getWeight(1,1))
__main__()
