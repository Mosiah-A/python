import random
n = int(random.uniform(0,6))
print('Pensando...')
r = int(input('Tente adivinhar qual numero de 0-5 eu pensei: '))
if n == r:
    print('Acertou')
else:
    print('Errou')
print('Eu pensei no numero {}'.format(n))
