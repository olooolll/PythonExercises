"""
Faça uma função que recebe uma lista de números reais e retorna o valor do menor
elemento e sua posição na lista. Não é permitido o uso de qualquer função que não
seja da sua autoria.
"""

def MyLen(value):
    count = 0
    for i in value:
        count +=1

    return count

def NumberAndIndex(list_):
    moreNumber = list_[0]
    index = 0

    i = 0
    while i < MyLen(list_):
        if list_[i] < moreNumber:
            moreNumber = list_[i]
            index = i
        
        i += 1

    return [moreNumber, index]

numbersList = [1,2,4,6,33,2,5,7]

print(NumberAndIndex(numbersList))