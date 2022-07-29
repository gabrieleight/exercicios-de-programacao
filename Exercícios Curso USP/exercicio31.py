def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        inicial = lista[0]
        del(lista[0])
        return inicial + soma_lista(lista)

def encontra_impares(lista):
    inicial = []
    if len(lista) == 1:
        nova_lista = []
        if lista[0] % 2 != 0:
            nova_lista.append(lista[0])
        return nova_lista
    else:
        if lista[0] % 2 != 0:
            inicial.append(lista[0])
        del(lista[0])
    return inicial + encontra_impares(lista)
 
#print(soma_lista([2,3,6,5,1,2,3]))
#print(encontra_impares([2,3,6,5,1,2,3]))