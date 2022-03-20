from graphAL import GraphAL

def giveChange( denominaciones : list, cantidad: int):
    for denominacion in denominaciones:
        numeroMoNEDAS = cantidad // denominacion
        
        cantidad = cantidad % denominacion
        
        print( numeroMoNEDAS, "de", denominacion)
        
        
        
giveChange([500,200,100,50],900)



def circuitoHalmitoniano(grafo : GraphAL):
    
    recorrido = []
    visitados = [False]*grafo.size
    
    
    recorrido.append(0)
    visitados[0] = True
    

    
    
    for vertice in range(grafo.size):
        
        if not visitados[vertice]:
            continue
        
        sucesores = sorted(grafo.getSuccessors(vertice), key = lambda x : x[1])
        
        
        todosVisitados = True
        
        for sucesor in sucesores:
            
            
            if not visitados[sucesor[0]]:
                
                todosVisitados = False
                
                recorrido.append(sucesor[0])
                visitados[sucesor[0]] = True
                break
            
            
        if todosVisitados:
            recorrido.append(0)
            print("grafo", recorrido)
        
        return recorrido
            
            
        
        
    
                
                
                
        
        
        
          
    
            
            
grafo1 = GraphAL(4)
    
grafo1.addArc(0,1,7)
grafo1.addArc(1,0,7)
grafo1.addArc(0,2,15)
grafo1.addArc(2,0,9)
grafo1.addArc(0,3,6)
grafo1.addArc(3,0,10)
grafo1.addArc(1,2,7)
grafo1.addArc(2,1,6)
grafo1.addArc(2,3,12)
grafo1.addArc(3,2,8)

# (Id, weight)

# [ (id, weight) (id, weight)] 

print(circuitoHalmitoniano(grafo1))


print("A")
            