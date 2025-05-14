"""
Crie uma função que exiba verticalmente uma string.
"""

def printl(string):
    if not string[1:]:
        print(string[0])
        return 0
    
    print(string[0])
    return printl(string[1:])

printl('string')