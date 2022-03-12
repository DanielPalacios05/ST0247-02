def seAtacanHastaI(tablero, i):
    for j in range(0,i+1):
        for k in range(j+1,i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j]==tablero[k]:
                return True
    return False

def nqueenAuxPrintOne(n:int):
    nqueenPrintOne(n,0,[0]*n)

def nqueenPrintOne(n:int,casilla:int,tablero:list):
    if casilla == n:
        print(tablero)
        return True
    else:
        for f in range(n):
            tablero[casilla]=f
            if not seAtacanHastaI(tablero,casilla):
                valido=nqueenPrintOne(n,casilla+1,tablero)
                if valido:
                    #print(tablero)
                    return True
        return False