"""
Faça uma função que recebe uma lista de números reais e retorna o valor da soma
de todos os números. Não é permitido o uso de qualquer função que não seja da
sua autoria.
"""

def SumList(list):
    sumItem = 0
    for i in list:
        sumItem += i
    
    return sumItem


numbersList = [1,2,4,6,33,2,5,7]

print(SumList(numbersList))