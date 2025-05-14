"""
Crie uma função para calcular o fatorial de um número.
"""
# x = 10
# result = 1
# print(f'{x}! = ', end='')
# for i in range((x + 1)):
#     if i == x:
#         print(i)
    
#     else:
#         print(i, end=' * ')

#     if i != 0:
#         result *= i
    
# print(result)


x = 5

def fato(n1):
    if n1 == 0:
        return 1
    
    return n1 * fato(n1 - 1)

print(fato(x))