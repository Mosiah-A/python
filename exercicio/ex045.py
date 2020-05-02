#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('''
[ 0 ] Papel
[ 1 ] Tesoura
[ 2 ] Pedra''')
r = int(input('Faça sua escolha: '))

opçao = ['Papel', 'Tesoura','Pedra']

player = opçao[r]
comp = randint(0,2)
cpu = opçao[comp]
if r >= 0 and r <= 2:
    if r == 0:
        if comp == 0:
            res = 2
        elif comp == 1:
            res = 1
        elif comp == 2:
           res = 0

    if r == 1:
        if comp == 0:
            res = 0
        elif comp == 1:
            res = 2
        elif comp == 2:
            res = 1

    if r == 2:
        if comp == 0:
            res =1
        elif comp == 1:
            res = 0
        elif comp == 2:
            res = 2
    op = ['ganhou', 'perdeu', 'empatou']
    resultado = op[res]
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    print(20*'-=')
    print('''Você escolheu \033[34m{}.\033[m
o computador escolheu \033[34m{}.\033[m
Você \033[36m{}!\033[m'''.format(player,cpu,resultado))
    print(20*'=-')
else:
    print('ERRO')
'''res = 0 -> ganhou
1 -> perdeu
2 -> empate'''
