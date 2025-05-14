"""
Crie uma função retornar o maior elemento inteiro de uma lista. Não
será permitido o uso de função que não seja da sua autoria.
"""

# def Count(list):
#     if not list:
#         return 0
    
#     return 1 + Count(list[1:])

# lista = []
lista = [47, 12, 89, 33, 75, 6, 58, 21, 94, 67]

def MoreItem(list):

    if not list[1:]:
        return list[0]
    
    if list[0] > list[-1]:
        list[-1] = list[0]

    return MoreItem(list[1:])

print(MoreItem(lista))