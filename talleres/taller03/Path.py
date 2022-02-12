def path(grafo,inicio,meta):
    if inicio==meta:
        return True
    else:
        for vecino in grafo.getSuccesor(inicio):
            delVecinoAMeta=path(grafo,vecino,meta)
            if delVecinoAMeta:
                return True
    return False