"""
Faça uma função recursiva para eliminar apenas a primeira ocorrência de uma
determinada letra de uma string;
"""

def uniqueRemove(string, char, removed=False):
    if not string:
        return ''
    
    if not removed:
        if string[0] == char:
            return '' + uniqueRemove(string[1:], char, True)

        return string[0] + uniqueRemove(string[1:], char, False)
        
    return string[0] + uniqueRemove(string[1:], char, True)


print(uniqueRemove('abracadabra', 'a'))