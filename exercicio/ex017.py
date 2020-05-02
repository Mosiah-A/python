'''faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triangulo calcule e mostre o
comprimento da hipotenusa'''

from math import hypot

'''x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjacente: '))
h = hypot(x,y)
print('O valor da hipotenuza de cateto oposto {} e cateto adjacente {} é {:.2f}'. format(x, y, h))'''

x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjacente: '))
h = (x ** 2 + y ** 2) ** (1/2)
print('O valor da hipotenuza de cateto oposto {} e  cateto adjacente {} é {:.2f}'. format(x, y, h))
