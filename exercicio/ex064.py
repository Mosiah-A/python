'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

n = s = cont = 0
while n != 999:
    n = int(input('Digit um numero [999 para parar]: '))
    if n == 999:
        print('Saindo')
        print('¨'*50)
    else:
        s += n
        cont +=1
print('Voce Digitou {} numero e a soma entre eles é {}'.format(cont,s))