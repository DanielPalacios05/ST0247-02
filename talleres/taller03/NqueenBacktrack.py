from collections import deque
def seAtacanHastaI(tablero, i):
    for j in range(0,i+1):
        for k in range(j+1,i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j]==tablero[k]:
                return True
    return False

def nqueenAuxPrint(n:int):
    nqueenPrint(n,0,[0]*n)

def nqueenPrint(n:int,casilla:int,tablero:list):
    if casilla == n:
        print(tablero)
    else:
        for f in range(n):
            tablero[casilla]=f
            if seAtacanHastaI(tablero,casilla):
                pass
            else:
                nqueenPrint(n,casilla+1,tablero)

def nqueenAuxSave(n:int):
    lista=deque()
    nqueenSave(n,0,[0]*n,lista)
    return lista

def nqueenSave(n:int,casilla:int,tablero:list,lista):
    if casilla == n:
        lista.append(tablero.copy())
    else:
        for f in range(n):
            tablero[casilla]=f
            if seAtacanHastaI(tablero,casilla):
                pass
            else:
                nqueenSave(n,casilla+1,tablero,lista)

nqueenAuxPrint(4)
print(nqueenAuxSave(4))