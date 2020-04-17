'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

from time import sleep
print('=-=' * 5,'\n  Ex059','\n','=-=' * 5)

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
r = 1
m = 0
while r != 5:
    print('=-=' * 10)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    print('=-=' * 10)
    r = int(input('>>>>>>Qual sua resposta? '))
    if r == 1:
        print('     {} + {} = {}'.format(n1,n2,n1+n2))
    elif r == 2:
        print('     {} x {} = {}'.format(n1,n2,n1*n2))
    elif r == 3:
        if n1 < n2:
            print('     O numero {} é maior'.format(n2))
        else:
            print('     O numero {} é maior'.format(n1))
    elif r == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    elif r == 5:
        print('Saindo...')
    else:
        print('\033[31mNumero invalido. Tente novamente! \033[m')
    sleep(2)