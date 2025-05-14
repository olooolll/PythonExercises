"""
Faça uma função recursiva para eliminar todas as ocorrências de uma
determinada letra de uma string;
"""

def removeChar(string, char):
    if not string:
        return ''
    
    if string[0] == char:
        return removeChar(string[1:], char)
    
    return string[0] + removeChar(string[1:], char)

print(removeChar('abracadabra', 'b'))