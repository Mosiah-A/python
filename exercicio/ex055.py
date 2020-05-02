'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos.

maior = 0.0
menor = 0
peso = 0.0
for c in range(1,6):
    peso = float(input("Digite o peso da {}° pessoa: ".format(c)))
    if c == 1:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi de {}Kg\nO menor peso lido foi de {}Kg'.format(maior,menor))'''
peso = []
for c in range (1,6):
    peso.append(float(input('Peso da {}ª pessoa:'.format(c))))
print('O maior peso lido foi {}kg.'.format(max(peso)))
print('O menor peso lido foi {}kg.'.format(min(peso)))



