def devuelta(cantidad, monedas): # notar que no todas las combinaciones de monedas dan la comb ideal con algoritmos voraces (pero funciona para COL) 
    monedas.sort(reverse=True)#O(Nlog(N))
    for valor in monedas:#O(N)
        numMonedas=cantidad//valor
        cantidad=cantidad%valor
        print(str(numMonedas)+" de "+str(valor))
        #todo el algor O(Nlog(N))

devuelta(1900,[1000,500,200,100])
devuelta(1900,[100,200,500,1000])
