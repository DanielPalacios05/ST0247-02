from cmath import inf
from graphAl import GraphAl
from collections import deque

def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

pesoMenor = -1


def viajero(grafo : GraphAl):

    vertexDif0 = []
    distanciaMenor=inf
    
    for i in grafo.diccionarioNombre.keys():

        vertexDif0.append(i)

    del vertexDif0[0]
    
    respuestas = deque()
    
    primerNodo = next(iter(grafo.diccionarioRutas))

    for i in all_perms(vertexDif0):

        
        permutacion = [primerNodo] + i + [primerNodo]
        
        comprobante=True

        for j in range(len(permutacion)-1):

            if permutacion[j+1] not in grafo.getSuccessors(permutacion[j]):
                comprobante=False
                break
        
        if comprobante: 
            distanciaActual=0
            for i in range(len(permutacion)-1):
                distanciaActual+= float(grafo.getWeight(permutacion[i],permutacion[i+1]))
            if distanciaActual<distanciaMenor:
                distanciaMenor=distanciaActual
                    
    return distanciaMenor


def main(): 

    archivos = open("codigo\puentesColgantes.txt", 'r')
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


    print("La distancia menor es:" ,viajero(grafo))




main()
