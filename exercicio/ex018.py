'''ex018
faça um programa que leia um angulo e mostre na tela o valor do seno, cosseno e tangente desse angulo'''

from math import sin,cos,tan,radians

a = float(input('Digite o ângulo que ocê deseja: '))
s = sin(radians(a))
print('O ângulo {} tem o seno de {:.2f}'.format(a,s))
c = cos(radians(a))
print('O ângulo {} tem o cosseno de {:.2f}'.format(a,c))
tg = tan(radians(a))
print('O ângulo {} tem a Tangente de {:.2f}'. format(a,tg))
