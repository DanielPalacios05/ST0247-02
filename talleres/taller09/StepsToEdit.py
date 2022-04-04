import numpy as np
def levenshteinAUX(A,B):
    return levenshtein(A,B,len(A),len(B))

def levenshtein(A,B,n,m):
    if m==0:
        return n
    if n==0:
        return m
    if A[n-1]==B[m-1]:
        return levenshtein(A,B,n-1,m-1)
    min(levenshtein(A,B,n-1,m-1),levenshtein(A,B,n-1,m),levenshtein(A,B,n,m-1))+1

def levenshteinAUXDP(A,B):
    n = len(A)+1
    m = len(B)+1
    tabla=np.zeros((n,m))
    for i in range (n+1):
        for j in range (m+1):
            if i == 0:
                tabla[i][j]=j
            elif j == 0:
                tabla[i][j]=i
            elif A[i-1]==B[j-1]:
                tabla[i][j]=tabla[i-1][j-1]
            else:
                    tabla[i][j]=min(tabla[i-1][j-1],tabla[i-1][j],tabla[i][j-1])
    return tabla[n][m]