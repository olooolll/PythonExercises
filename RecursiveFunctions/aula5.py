"""
Crie uma função para retornar a quantidade de caracteres de
uma string.
"""
string = 'string'

def Mylen(string):
    if not string[1:]:
        return 1
    
    return 1 + Mylen(string[1:])

print(Mylen(string))
