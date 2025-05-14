"""
Faça uma função recursiva para contar a quantidade um determinado elemento
em uma lista;
"""
# def Count(list):
#     if not list:
#         return 0
    
#     return 1 + Count(list[1:])

def CountItem(lista, element):
    if not lista:
        return 0
    
    if lista[0] == element:
        return 1 + CountItem(lista[1:], element)

    return CountItem(lista[1:], element)

a = [47, 12, 89, 33, 75, 6, 58, 33, 3333,333333,33,33,3,3,3333,33,33,3, 21, 94, 67]

print(CountItem(a, 33))