'''cont = 1
while True:
    print(cont, ' -> ', end='')
    cont += 1
print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
# print('A Soma vale {}'.format(s))
print(f'A soma vale {s}')'''

nome = 'Jose'
idade = 33
salario = 987.3
print(f'O {nome:-^6} tem {idade} anos e ganha R${salario:.2f}')

