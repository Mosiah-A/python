'''um professor quer sortear um dos seus quatro alunos para apagar o quadro.
faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhiido'''

from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
l = [n1,n2,n3,n4]
r = choice(l)
print('O aluno escolhido foi {}'.format(r))
