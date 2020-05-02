#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o valor de um seguimento: '))
b = float(input('Digite outro: '))
c = float(input('Digite mais um: '))
count = 0 # 0 = Folse; 1 = True
if b < a + c and a < b + c and c < a + b:
    count = 1
if count == 1: # if True
    print('\033[32mÉ um triangulo')
else:
    print('\033[31mNão é um triangulo')
