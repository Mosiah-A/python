#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letas maiusculas
# minusculas
# quantas letras ao todo sem espaço
#  quantas letras tem o primeiro nome

nome = str(input('digite seu nome completo: ')).strip()
print('seu nome em maiusculo: ',nome.upper())
print('seu nome em minusculo: ',nome.lower())
print('seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome tem {} letras: '.format(len(separa[0])))
