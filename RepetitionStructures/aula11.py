"""
● Um matemático italiano da idade média conseguiu modelar o ritmo de
crescimento da população de coelhos através de uma sequência de números
naturais que passou a ser conhecida como Sequência de Fibonacci. O n-ésimo
número da sequência de Fibonacci Fn é dado pela seguinte fórmula: Fi = Fi-1 + Fi-2
● O resultado é a sequência {1, 1, 2, 3, 5, 8, 13, 21, ...}.
● Faça um programa que leia um número inteiro positivo N, calcula e escreve os N
primeiros números da sequência de Fibonacci.
"""

print (" Trabalho de Fibonacci ")

n =int( input(" Digite Quantos termos você deseja :"))
t1 = 0
t2 = 1
t3 = 0

while t3 <= n:
    print("{}.".format(t3), end="")
    t3 = t1 + t2
    t1 = t2
    t2 = t3

print( " Fim ")