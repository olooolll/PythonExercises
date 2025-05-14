"""
Crie uma função para calcular o quociente da divisão inteira.
"""
n1 = 28
n2 = 4
# count = 0

# while x >= y:
#     x -= y
#     count += 1

# print(count)

def div(x, y):
    if x < y:
        return 0
    
    return 1 + div(x - y, y)


print(div(n1,n2))