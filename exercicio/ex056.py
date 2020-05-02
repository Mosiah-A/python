'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.'''

media=0
soma = 0
hv = 0
nomev = ''
m = 0
for c in range(1, 5):

#tabela
    print('----- {}° Pessoa -----'.format(c))
    nome = input('Nome: ').title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

# mulher mais nova que 20 anos
    if sexo == 'F':
        if idade < 20:
            m += 1

# homem mais velho
    if sexo == 'M':
        if idade > hv:
            nomev = nome
            hv = idade

# media das idades
    soma += idade
media = soma/4

# mostrar analise
print('A media de idade do grupo é de {} anos\nO homem mais velho tem {} anos e se chama {}\nAo todo são {} com menos de 20 anos'.format(media,hv,nomev,m))
