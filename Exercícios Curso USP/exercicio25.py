def ordenada(lista):
    leng = len(lista)
    for i in range(leng):
        menor_elemento = lista[i]
        j = i + 1
        if j >= leng:
            break
        elemento_consecutivo = lista[j]
        if menor_elemento < elemento_consecutivo:
            continue
        else:
            return False
    return True


def busca(lista, elemento):
    leng = len(lista)
    for i in range(leng):
        if lista[i] == elemento:
            return i
    return False

"""
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 7, 2, 5, 1]

print(ordenada(lista1))
print(ordenada(lista2))

lista3 = ['a', 'e', 'i', 'o', 'u']
print(busca(lista3, 'e'))
"""