#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

l1 = float(input('Primeiro Seguimento: '))
l2 = float(input('Segundo Seguimento: '))
l3 = float(input('Tereiro Seguimento: '))
count = 0
if l2 < l1 + l3 and l1 < l2 + l3 and l3 < l1 + l2:
    print('Pode formar um triangulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('ISÓSCELES.')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO.')
else:
    print('\033[31mNão é um triangulo')
