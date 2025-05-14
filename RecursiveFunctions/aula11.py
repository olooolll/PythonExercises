"""
Faça uma função recursiva para eliminar os números pares de uma lista de
números inteiros;
"""

numbers = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def delPar(lista):
    if not lista:
        return []

    if lista[0] % 2 != 0:
        return [lista[0]] + delPar(lista[1:])

    return delPar(lista[1:])

print(delPar(numbers))