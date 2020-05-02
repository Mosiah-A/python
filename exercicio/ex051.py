'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
print('=' * 30)
print('{:^30}'.format('10 termos de uma PA'))
print('=' * 30)
x = int(input("Digite o primeiro termo: "))
y = int(input("Digiete a razão: "))
v = x + (10 - 1) * y
for c in range (x,v + y,y):
    print('{}'.format(c), end=' - ')
print('FIM')