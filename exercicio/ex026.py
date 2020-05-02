#Faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra A, em que posição ela aparece a ultima vez

nome = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes. '.format(nome.count('a')))
print('A primeira letra A aparece na posição {}'.format(nome.find('a')+1))
print('A ultima letra A aparece na posição {}'.format(nome.rfind('a')+1))
