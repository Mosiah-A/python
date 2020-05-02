'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('=' * 30)
print('{:^30}'.format('Termos de uma PA'))
print('=' * 30)
x = int(input("Digite o primeiro termo: "))
y = int(input("Digiete a razão: "))
termo = x
cont = 1
q=10
q1=0
while cont <= q:
    print('{} -> '.format(termo), end='')
    termo += y
    cont += 1
    if cont == q+1:
        #print('{} ->'.format(termo), end='')
        print('Pausa')
        q1 = int(input('Quantos termos você quer mostrar a mais: '))
        q += q1
print('Progressao finalizada com {} Termos Mostrados'.format(cont-1))
print('FIM')

#guanabara resolução
'''
print('=' * 30)
print('{:^30}'.format('10 termos de uma PA'))
print('=' * 30)
x = int(input("Digite o primeiro termo: "))
y = int(input("Digiete a razão: "))
termo = x
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += y
        cont += 1
    print('Pausa')
    mais=int(input('Quantos termos você quer ver a mais? '))
print('Progressao finalizada com {} Termos Mostrados'.format(total))
'''