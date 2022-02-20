import pandas as pd
from matrix import Graph

data = pd.read_csv("calles_de_medellin_con_acoso.csv",
                   sep=";", usecols=[0, 1, 2, 3, 4, 5])

arrdata = data.to_numpy()


mapa = Graph()

numberofNodes = 0


for i in arrdata:

    if i[1] not in mapa.vertices.keys():
        mapa.vertices[i[1]] = numberofNodes
        numberofNodes = numberofNodes+1
    if i[2] not in mapa.vertices.keys():
        mapa.vertices[i[2]] = numberofNodes
        numberofNodes = numberofNodes+1
        
print(numberofNodes)

mapa.iniMatrix(numberofNodes)


for i in arrdata:
    mapa.matrix[mapa.vertices[i[1]]][mapa.vertices[i[2]]] = 1

print(mapa.matrix)