#Crie um programa que leia um numero inteiro e mostre na tela se é impar ou par

n = int(input('Digite um numero: '))
r = n % 2
if (r == 0):
    print('Este numero é par')
else:
    print('Este numero é impar')