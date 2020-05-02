'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.'''
print('=' * 30)
print('{:^30}'.format('10 termos de uma PA'))
print('=' * 30)
x = int(input("Digite o primeiro termo: "))
y = int(input("Digiete a razão: "))
termo = x
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += y
    cont += 1
print('FIM')
