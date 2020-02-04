#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.


n = int(input('Digite um numero inteiro: '))
print('''Escolha uma das basespara a comversão:
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
r = int(input('Sua opção: '))
if r == 1:
    print('{}'.format(bin(n)[2:]))
elif r == 2:
    print('{}'.format(oct(n[2:])))
elif r == 3:
    print('{}'.format(hex(n)[2:]))
else:
    print('\033[31mERRO!')
