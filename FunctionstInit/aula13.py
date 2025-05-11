"""
Faça uma função que recebe uma lista de números reais e retorna o valor do
produto desses números. Não é permitido o uso de qualquer função que não seja
da sua autoria.
"""
def MyLen(list):
    count = 0
    for i in list:
        count +=1

    return count


def ProductList(list):
    i = 0

    result = list[-1]
    while i < (MyLen(list) - 1):
        result *= list[i]

        i += 1
    
    return result

numbersList = [1,2,4,6,33,2,5,7]

print(ProductList(numbersList))
