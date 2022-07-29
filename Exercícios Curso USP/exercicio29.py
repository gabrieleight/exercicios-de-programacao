def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n-1)

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1
    
    if max < min:
        return False
    else:
        meio = min + (max - min)//2
    
    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)
    else:
        return meio
    
#print(fatorial(5))
    
#print(fibonacci(9))