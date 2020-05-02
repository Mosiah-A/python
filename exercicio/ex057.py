'''xercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = input('Informe seu sexo: [F/M] ').strip().upper() [0]
while sexo not in 'FM':
    print('Dado invalido')
    sexo = input('Informe seu sexo: [F/M] ').strip().upper() [0]
print('Sexo Registrado')

