"""
Faça uma função que reconhece se uma string é um palíndromo. A função deve
considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” =
“A” e retornar True se é um palíndromo e False caso contrário.
"""

def Palindrome(string):
    halfLenString = len(string) / 2
    if halfLenString % 1 != 0:
        halfLenString -= 0.5

    j = len(string) - 1
    
    for i in range(int(halfLenString)):
        if string[i].lower() != string[j].lower():
            return False
        j += -1
    
    return True

print(Palindrome('arara'))