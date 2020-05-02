'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.
'''

r ='S'
maior = menor = cont = soma = 0

while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Deseja continuar? [S/N]')).upper().strip()
    cont += 1
    soma += n
    if n > maior:
        maior = n
    if cont == 1:
        menor = n
    if n < menor and n > 0:
        menor = n
print('O numero {} foi o maior numero digitado e o menor numero foi {}\nA média dos numeros digitados foi {}'.format(maior,menor,soma/cont))
