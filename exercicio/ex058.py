'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
from time import sleep
n = randint(0,10)

print('--=--' * 3)
print('Pensando...')
print('--=--' * 3)
sleep(2)

r = int(input('Tente adivinhar qual numero de 0-10 que eu pensei: '))
tente=1
while r != n:
    print('Errou :(')
    tente += 1
    if r > n:
        r = int(input('menos: '))
    else:
        r = int(input('mais: '))
print('Acertou! voce teve  {} tentativas'.format(tente))
