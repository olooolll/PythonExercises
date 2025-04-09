"""
Utilizando a string “ Iracema – a lenda do Ceará ”, sem alterar seu valor original e sem
utilizar métodos (apenas lower() e upper() são permitidos), elabore programas que mostrem
na tela:
a) Todas as letras em maiúsculo;
b) Somente a primeira letra em maiúsculo;
c) Todas as iniciais em maiúsculo;
d) Troque os espaços em branco do início por “#” ;
e) Troque os espaços do final por “*”;
f) Retire todos os espaços em branco do início e do fim;
g) Mostre o índice da primeira ocorrência do caractere “a”:
h) Mostre o índice da última ocorrência do caractere “a”;
i) Mostre a quantidade de letras “e”;
j) Mostre a inversão de todos os caracteres (maiúsculas/minúsculas).

"""
String = ' Iracema – a lenda do Ceará '
Alfabet = 'abcdefghijklmnopqrstuvwxyzáàâãäéèêëíìîïóòôõöúùûüçñ'

print('a) Todas as letras em maiúsculo: ', end='')
for i in String:
    for j in Alfabet:
        if i == j:
            print(i, end=' ')

print()
print('b) Somente a primeira letra em maiúsculo: ', end='')
Count = 0
for i in String:
    for j in Alfabet:
        if i == j and Count < 1:
            print(i)
            Count += 1
            
print('c) Todas as iniciais em maiúsculo: ', end='')
LastChar = ''
for i in String:
    for j in Alfabet:
        if i == j and LastChar == ' ':
            print(i, end=' ')
    LastChar = i

print()
print('d) Troque os espaços em branco do início por “#” : ', end='')
NewString = ''
Count = 0
for i in String:
    if i == ' ' and Count < 1:
        NewString += '#'
        Count += 1
    else: 
        NewString += i

print(NewString)


print('e) Troque os espaços do final por “*”: ', end='')
NewString = ''
Count = 0
for i in String:

    if i == ' ':
        Count += 1

        if Count == 7:
            NewString += '*'
        else:
            NewString += ' '
    
    else: 
        NewString += i

print(NewString)

print('f) Retire todos os espaços em branco do início e do fim: ', end='')
NewString = ''
Count = 0
for i in String:

    if i == ' ':
        NewString += ''
    
    else: 
        NewString += i

print(NewString)

print('g) Mostre o índice da primeira ocorrência do caractere “a”: ', end='')
Count = 0
index = 0
for i in String:
    
    if i == 'a' and Count < 1:
        Count += 1
        print(index)
        
    index += 1

print('h) Mostre o índice da última ocorrência do caractere “a”: ', end='')
Count = 0
index = 0
LenString = len(String) - 1

for i in String:

    if String[LenString] == 'a' and Count < 1:
        Count += 1
        print(index)

    LenString -= 1

    index += 1


print('i) Mostre a quantidade de letras “e”: ', end='')
Count = 0

for i in String:
    if i == 'e':
        Count += 1

print(Count)

print('j) Mostre a inversão de todos os caracteres (maiúsculas/minúsculas): ', end='')

for i in String:

    for j in Alfabet:
        if i == j.lower() or i == j.upper():
            if i == i.lower():
                print(i.upper(), end='')
            if i == i.upper():
                print(i.lower(), end='')
