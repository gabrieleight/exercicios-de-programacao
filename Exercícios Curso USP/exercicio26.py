def bolha(lista):
    fim = len(lista)
    
    for i in range(fim-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

lista = [10, 3, 8, -10, 200, 17, 32]

print(bolha(lista))