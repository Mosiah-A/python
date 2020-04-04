'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
mr = 0
mn = 0
idade = 0
for c in range (1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - ano
    if idade <= 21:
        mn += 1
    else:
        mr += 1
print('temos {} maior de idade \ntemos {} menor de idade'.format(mr,mn))
