"""
Faça uma função recursiva para contar a quantidade uma determinada letra em
uma string;
"""


def count(string, char):
    if not string:
        return 0
    
    if string[0] == char:
        return 1 + count(string[1:], char)
    
    return count(string[1:], char)


print(count('abracadabra', 'a'))