"""
Faça uma função que recebe duas strings e retorna True se as strings são anagrama
ou False caso contrário. Ex.:
roma, amor > True
ovo, vov > False
"""

def BubbleSort(list_):
    list__ = list_

    for i in range(len(list__)):
        for j in range(len(list__) - 1):
            if list__[j] > list__[j + 1]:
                list__[j], list__[j + 1] = list__[j + 1], list__[j] 

    return list__

def Anagrama(string1, string2):
    list1 = []
    list2 = []
    if len(string1) == len(string2):
        
        for i in string1:
            list1.append(i.lower())

        for i in string2:
            list2.append(i.lower())
        
        if BubbleSort(list1) != BubbleSort(list2):
            return False
        
        return True
        
    return False


print(Anagrama('ovo', 'vov'))
