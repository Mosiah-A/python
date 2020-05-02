'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
from math import factorial
titulo = ' Fatorizando um  numero '
print(f'{titulo:#^45}')

n = int(input('Digite um numero: '))
cont = n
fac = 1 #sem a bilioteca
print('{}! = '.format(n),end='')
if n == 0:
    print(1)
else:
    while cont != 0:
        if n < 0:
            print('ERRo')
            print('Diite um numero positivo')
            n = int(input('Digite um numero: '))
            cont = n
        else:
            print('{}'.format(cont), end='')
            print(' x ' if cont > 1 else ' = ', end = '')
            fac *= cont  #sem a bilioteca
            cont -= 1
    print(fac)
    #print(factorial(n))

