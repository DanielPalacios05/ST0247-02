def seAtacanHastaI(tablero, i):
    for j in range(0,i+1):
        for k in range(j+1,i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j]==tablero[k]:
                return True
    return False





def noSeAtacan(tablero):
    valor=False
    for i in range(len(tablero)):
        valor=not seAtacanHastaI(tablero,i)
    return valor




print(noSeAtacan([1,2,3,4]))