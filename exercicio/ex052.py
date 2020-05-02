'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
x = int(input('Digite um numero: '))
cont = 0
for c in range (1, x+1):
    if x % c == 0:
        print('\033[32m', end= ' ')
        cont += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end= ' ')
if cont == 2:
    print('\n\033[mO numero {} é primo'.format(x))
else:
    print('\n\033[mO numero {} não é primo'.format(x))
