def subCadenaAux(cadena):
    subCadena(cadena,"")

def subCadena(inicio,respuesta):
    if len(inicio)==0:
        print(respuesta)
        return None
    else:
        subCadena(inicio[1:],respuesta+inicio[0])
        subCadena(inicio[1:],respuesta)

def permutacionesSinAux(cadena):
    permutacionesSin(cadena,"")

def permutacionesSin(cadena,respuesta):
    if len(cadena)==0:
        print(respuesta)
        return None
    else:
        for i in range(0,len(cadena)):
            nuevo=cadena[0:i]+cadena[i+1:]
            permutacionesSin(nuevo,respuesta+cadena[i])

def permutacionesAux(cadena):
    permutaciones(cadena,"")

def permutaciones(cadena,respuesta):
    if len(cadena)==len(respuesta):
        print(respuesta)
        return None
    else:
        for i in range(0,len(cadena)):
            permutaciones(cadena,respuesta+cadena[i])
        
    

permutacionesAux("abc")