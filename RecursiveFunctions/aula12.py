"""
Faça uma função recursiva para retornar o produto dos elementos de uma lista
de números inteiros;
"""

def Prod(lista):
    if not lista:
        return 1
    
    return lista[0] * Prod(lista[1:])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(Prod(numbers))