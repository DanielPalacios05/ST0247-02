from collections import deque
def seAtacanHastaI(tablero, i):
    for j in range(0,i+1):
        for k in range(j+1,i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j]==tablero[k]:
                return True
    return False

def seAtacan(tablero):
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

def validacion(posicion, tablero):
    control=True
    if not seAtacan(posicion):
        for i in range(len(posicion)):
            if tablero[posicion[i]][i] == '*':
                control = False
    return control

tamaño=int(input())
caso=0
while tamaño!=0: 
    caso+=1
    posiciones= list(range(tamaño))
    posicionesPosibles=deque()
    for i in all_perms(posiciones):
        posicionesPosibles.append(i)
    tablero=[" "]*tamaño
    j=0
    while j < tamaño:
        linea=input()
        if len(linea)==tamaño:
            tablero[j]=linea
            j+=1
        else:
            print("linea invalida prueba de nuevo")
    contador=0
    for revisar in posicionesPosibles:
        if validacion(revisar,tablero):
            contador+=1
    print("Caso "+str(caso)+": "+str(contador))
    tamaño=int(input())




    for _ in range(10): #Sirve para un solo caso por el momento, cambiar a 10 para full testing
        
        numTablero = int(input())
        
        for i in range(numTablero):
            
            linea = input()
            listaMalCuadro = []
        
            for j in range(len(linea)):
                
               if linea[j] == "*":
                    
                    listaMalCuadro.append((i,j))    
                    
                    
        casosPosibles(numTablero,listaMalCuadro) 