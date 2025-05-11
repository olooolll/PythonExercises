"""
Faça uma função que recebe uma lista de números reais e retorna a lista ordenada
do menor para o maior valor. Não é permitido o uso de qualquer função que não
seja da sua autoria.
"""
def MyLen(value):
    count = 0
    for i in value:
        count +=1

    return count

def SmallerToLarger(list_):
    list__ = list_
    i = 0
    while i < MyLen(list_):
        j = 0
        while j < (MyLen(list__) - 1):
            if list__[j] > list__[j + 1]:
                list__[j], list__[j + 1] = list__[j + 1], list__[j]
            j += 1
        i += 1

    return list__

numbersList = [1,2,4,6,33,2,5,7]
print(numbersList)
print(SmallerToLarger(numbersList))