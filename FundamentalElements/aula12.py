"""
Flíper é um Ɵpo de jogo onde uma bolinha de metal cai por um
labirinto de caminhos até chegar na parte de baixo do labirinto. A
quanƟdade de pontos que o jogador ganha depende do caminho
que a bolinha seguir. O jogador pode controlar o percurso da
bolinha mudando a posição de algumas porƟnhas do labirinto. Cada
porƟnha pode estar na posição 0, que significa virada para a
esquerda, ou na posição 1 que quer dizer virada para a direita.
Considere o flíper da figura abaixo, que tem duas porƟnhas. A
porƟnha P está na posição 1 e a porƟnha R, na posição 0. Desse
jeito, a bolinha vai cair pelo caminho B.
● Você deve escrever um programa que, dadas as posições das
porƟnhas P e R, neste flíper da figura, diga por qual dos três
caminhos, A, B ou C, a bolinha vai cair
"""


p = int(input('Informe o valor da porta P: '))
r = int(input('Informe o valor da porta R: '))

if not p:
    print('A bolinha irá cair no caminho C')
elif not r:
    print('A bolinha irá cair no caminho B')
else:
    print('A bolinha irá cair no caminho A')
