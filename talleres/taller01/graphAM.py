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
