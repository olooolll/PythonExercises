"""
Faça uma função que recebe uma lista de números reais e retorna o valor da média
entre seus elementos. Não é permitido o uso de qualquer função que não seja da
sua autoria
"""

def MyLen(value):
    count = 0
    for i in value:
        count +=1

    return count


def Mean(list_):
    lenList = MyLen(list_)
    sumNumbers = 0
    for i in list_:
        sumNumbers += i
    
    return (sumNumbers / lenList)


numbersList = [1,2,4,6,33,2,5,7]

print(Mean(numbersList))