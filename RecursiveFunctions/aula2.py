""""
Crie uma função para calcular a potência xy.
"""
# y = 3
# x = 3
# restut = 0

# for i in range(y):
#     restut += x * x

# print(restut)


def pontenc(x, y):
    if y == 1:
        return x
    
    return pontenc(x, y - 1) * pontenc(x, 1)

print(pontenc(3, 9))