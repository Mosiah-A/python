#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).title().strip().split()

print('Muito prazer em te conhecer')
print('seu primeiro nome é ({}) '.format(nome[0]))
print('E seu ultimo nome é ({})'.format(nome[-1]))
