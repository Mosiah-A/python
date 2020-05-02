#Escrea um programa que faça o computador "Pensar" em um numero inteiro
# entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido
#pelo computador. O programa devera escrever na tela se o usuario perdeu ou venceu.
 
from random import randint
from time import sleep
n = randint(0,5)
 
print('--=--' * 3)
print('Pensando...')
print('--=--' * 3)
sleep(2)
 
r = int(input('Tente adivinhar qual numero de 0-5 eu pensei: '))
 
if n == r:
    print('Acertou')
else:
    print('Errou')
print('Eu pensei no numero {}'.format(n))
 
