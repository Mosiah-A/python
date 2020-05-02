'''enquanto não maçã
    se chão
        passo
    se buraco
        pula
    se moeda
        pega
pega

while not maçã:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega'''

'''for c in range(1,10):
    print(c)
print('fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valo: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
