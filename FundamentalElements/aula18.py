"""
Crie um programa que leia a idade do eleitor e informe se o eleitor é facultaƟvo
(entre 16 e 17 anos) ou obrigatório (entre 18 a 65) ou dispensado (acima de 65)
ou ainda se ele não pode votar.
"""

Idade = int(input('Digite a sua idade: '))

if Idade > 65:
    print('Dispensado')
elif Idade > 17:
    print('Obrigatório')
elif Idade > 15:
    print('Facultativo')
else:
    print('Ainda não pode votar')