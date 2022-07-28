def busca(lista, x):
        primeiro = 0
        ultimo = len(lista) - 1
        
        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            print(meio)
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return False
    
def bubble_sort(lista):
    fim = len(lista)
    
    for i in range(fim-1, 0, -1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                print(lista)
        if not trocou:
            break 
    return lista

"""
print(busca(['a', 'e', 'i'], 'e'))
print()
print(busca([1, 2, 3, 4, 5], 6))
print()
print(busca([1, 2, 3, 4, 5, 6], 4))
"""
"""
print(bubble_sort([5,1,4,2]))
"""