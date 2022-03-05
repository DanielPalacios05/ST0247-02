from collections import deque
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

def all_perms(tablero):
    if len(tablero) <= 1:
        yield tablero
    else:
        for perm in all_perms(tablero[1:]):
            for i in range(len(tablero)):
                # nb tablero[0:1] works in both string and list contexts
                yield perm[:i] + tablero[0:1] + perm[i:]



def estaEnCuadroValido(permutacion, malosCuadros):
    
    
    for i in range(len(permutacion)):
        
        for j in range(len(malosCuadros)):
            
            if permutacion[malosCuadros[j][1]] == malosCuadros[j][0]:
                return False
            
            
    
    return True


def casosPosibles (n, malosCuadros):
    
    casos = 0
    
    for permutacion in all_perms(list(range(n))):
        
        if estaEnCuadroValido(permutacion, malosCuadros) and noSeAtacan(permutacion):
            
            casos += 1
            
            
    return casos
            
            
            
            
        
        
        
        
        
        
        
    
    
    
    
    


def main():

    numTablero=int(input())
    
    listaSalidas = deque()

    
    while numTablero != 0:
        
        
        listaMalCuadro = []
        i=0
        while i<numTablero:
            
            linea = input()
            if len(linea)!=numTablero:
                print("linea invalida vuealva a ingresarla")
            else:
                for j in range(len(linea)):
                    
                    if linea[j] == '*':
                        
                        listaMalCuadro.append((i,j)) 
                i+=1
                        
                        
        listaSalidas.append(casosPosibles(numTablero,listaMalCuadro))  
        
        numTablero=int(input())
        
        
    for i,k in enumerate(listaSalidas):
        
        print("Caso "+str(i+1)+": "+str(k))

        
main()