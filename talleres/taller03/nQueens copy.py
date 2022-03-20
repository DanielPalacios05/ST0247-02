from collections import deque
import math
def checkQueens(table, i):
    for j in range(i):
        for k in range(j+1,i+1):
            if math.fabs(table[j]-table[k]) == math.fabs(j-k) or table[j] == table[k]:
                return True
        
    return False



def nreinas(n:int):
    li = deque()
    nreinasAux(n,0,[0]*n,li)
    return li
    
    
def nreinasAux(n: int, c:int, l:list, lista:deque):
    if c==n:
        lista.append(l)
        return
        
    for f in range(n):
        l[c]=f
        
        if not checkQueens(l,c):
            nreinasAux(n,c+1,l,lista)
            
            
if __name__ == '__main__':
    print(nreinas(4))