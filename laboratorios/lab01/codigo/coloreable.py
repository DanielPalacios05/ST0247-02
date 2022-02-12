from matrix import Graph
from collections import deque
def main():
    
    graphList = deque()
    
    nodos = int(input())
    
    while nodos!=0:
        aristas=int(input())
        
        graph = Graph(nodos)
        
        for _ in range(aristas):
            
            arista = list(map(int, input().split()))
            graph.addUndirArc(arista[0],arista[1])        
        
        graphList.append(graph)
        
        nodos=int(input())
        
        
    while graphList:
        graphList.popleft().coloreable()

if __name__ == '__main__':
    main()

