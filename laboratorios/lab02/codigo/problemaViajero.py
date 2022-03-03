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
    comprobante=False
    respuestas = deque()

    for i in all_perms(vertexDif0):

        permutacion = [next(iter(grafo.diccionarioRutas))] + i + [next(iter(grafo.diccionarioRutas))]
        comprobante=False

        for j in range(len(permutacion)-1):

            if permutacion[j+1] in grafo.getSuccessors(permutacion[j]):
                comprobante=True
            else:
                comprobante=False
                break
        
        if comprobante:
            respuestas.append(permutacion)
    print(respuestas)
    for lista in respuestas:
        distanciaActul=0
        for i in range(len(lista)-1):
            distanciaActul+= float(grafo.getWeight(lista[i],lista[i+1]))
        if distanciaActul<distanciaMenor:
            distanciaMenor=distanciaActul
    return distanciaMenor


def main(): 

    archivos = open("laboratorios\lab02\codigo\puentesColgantes.txt", 'r')
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


    print(viajero(grafo))




main()
