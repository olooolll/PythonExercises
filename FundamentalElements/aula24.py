"""
Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
metro e cresce 3 centímetros por ano. Faça um programa que calcule e imprima
quantos anos serão necessários para que Zé seja maior que Chico.
"""
chico = 1.5
ze = 1.1
ano = 0

while chico > ze:
    chico += 0.02
    ze += 0.03
    ano += 1

print(f'Demorara {ano} anos para o zé ({ze:.2f}) ser maior que o chico ({chico:.2f})')
