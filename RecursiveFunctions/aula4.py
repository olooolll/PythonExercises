"""
Crie uma função para calcular o resto da divisão inteira.
"""
n1 = 39
n2 = 7

def rest(x, y):
    if x < y:
        return x
    return rest(x - y, y)
    

print(rest(n1, n2))