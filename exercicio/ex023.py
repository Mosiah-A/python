#faça um programa que leia o numero de 0 á 9999 e mostre na tela cada um do digito separado

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
