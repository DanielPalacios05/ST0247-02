from collections import deque
from math import inf
from graphAl import GraphAl

#  Python3 program for the above approach
 
from typing import DefaultDict
 
 
INT_MAX = 9999999
 
# Function to find the minimum
# cost path for all the paths
def findMinRoute(tsp : GraphAl):
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = INT_MAX
    visitedRouteList = DefaultDict(int)
 
    # Starting from the 0th indexed
    # city i.e., the first city
    visitedRouteList[0] = 1
    route = [0] * tsp.size
 
    # Traverse the adjacency
    # matrix tsp[][]
    while i < tsp.size and j < tsp.size:
 
        # Corner of the Matrix
        if counter >= tsp.size - 1:
            break
 
        # If this path is unvisited then
        # and if the cost is less then
        # update the cost
        if j != i and (visitedRouteList[j] == 0):
            if tsp.getWeight(tsp.diccionarioVertices[i],tsp.diccionarioVertices[j]) < min:
                min = tsp.getWeight(tsp.diccionarioVertices[i],tsp.diccionarioVertices[j])
                route[counter] = j + 1
 
        j += 1
 
        # Check all paths from the
        # ith indexed city
        if j == tsp.size:
            sum += min
            min = INT_MAX
            visitedRouteList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1
 
    # Update the ending city in array
    # from city which was last visited
    i = route[counter - 1] - 1
 
    if i +
    in route:
        min = tsp.getWeight(tsp.diccionarioVertices[i],tsp.diccionarioVertices[0])
    else:
         for j in range(tsp.size):
 
            if (i != j) and tsp.getWeight(tsp.diccionarioVertices[i],tsp.diccionarioVertices[j]) < min:
                min = tsp.getWeight(tsp.diccionarioVertices[i],tsp.diccionarioVertices[j])
                route[counter] = j + 1
 
    sum += min
 
    # Started from the node where
    # we finished as well.
    return(sum, [0] + list(map(lambda x: x -1, route[:-1])) + [0])

# Driver Code
def main(): 

    archivos = open("laboratorios\lab04\codigo\puentesColgantes.txt", 'r')
    aristas = deque()
    vertices = deque()
    a = archivos.readline()
    a = archivos.readline()
    if a == "\n":
        a = archivos.readline()
    while a.strip() != "":
        if len(a.split()) == 4:
            añadir = a.split()
        else:
            añadir = a.split()
            añadir.append("Nombre Desconocido")
        vertices.append(añadir)
        a = archivos.readline()

    a = archivos.readline()
    a = archivos.readline()
    if a == "\n":
        a = archivos.readline()
    while a.strip() != "":
        aristas.append(a.split())
        a = archivos.readline()

    grafo = GraphAl(vertices, aristas)
    print("Distancia mas corta:", findMinRoute(grafo))
    
    
    



main()
