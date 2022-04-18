import numpy as np
def lcsAux(A : str, B : str, i : int, j : int):
    if i == len(A) or j == len(B):
        return 0
    elif A[i] == B[j]:
        return 1 + lcsAux(A,B,i+1,j+1)
    else:
        return max( lcsAux(A,B,i+1,j), lcsAux(A,B,i,j+1))

def lcs(A : str, B : str) :
    return lcsAux(A,B,0,0)

def lcsDP(A:str,B:str):
    a,b=len(A)+1,len(B)+1
    resultado=np.zeros((a,b))
    for i in range (1,a):
        for j in range (1,b):
            if A[i-1]==B[j-1]:
                resultado[i][j]=1+resultado[i-1][j-1]
            else:
                resultado[i][j]=max(resultado[i-1][j],resultado[i][j-1],)
    return resultado[a-1][b-1]

def lcsDP_DevolvientdoCadena(A:str,B:str):
    a,b=len(A)+1,len(B)+1
    resultado=np.zeros((a,b))
    for i in range (1,a):
        for j in range (1,b):
            if A[i-1]==B[j-1]:
                resultado[i][j]=1+resultado[i-1][j-1]
            else:
                resultado[i][j]=max(resultado[i-1][j],resultado[i][j-1],)
    i,j=a-1,b-1
    cadena=""
    while i != 0 or j != 0:
        if A[i-1]==B[j-1]:
            cadena= A[i-1]+cadena
            i,j=i-1,j-1
        else:
            if i==0:
                i,j=i,j-1
            elif j==0:
                i,j=i-1,j
            else:
                maximo = max(resultado[i,j-1],resultado[i-1,j])
                if resultado[i-1][j]==maximo:
                    i,j=i-1,j
                else:
                    i,j=i,j-1
    return cadena

print(lcsDP("AADCFTGH","ADYCTGWH"))
print(lcsDP_DevolvientdoCadena("AADCFTGH","ADYCTGWH"))