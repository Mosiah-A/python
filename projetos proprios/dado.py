from random import randint
from time import sleep

print('''Olá, bem vindo ao rolador de dados.
eu sou a M.A.I.A''')


#rolagem de dados

def rolagem(dado):
    if dado == 1 :
        return randint(1,6)
    if dado == 2:
        return randint(1,6)
    if dado == 3:
        return randint(1,8)
    if dado == 4:
        return randint(1,10)
    if dado == 5:
        return randint(1,12)
    if dado == 6:
        rolagem = randint(1,20)
        if rolagem == 1:
            print('Falha critica')
        if rolagem == 20:
            print('Critico')
        return rolagem
    if dado == 7:
        return randint(2,100)

        
#menu de opções
    
def menu():
    print('''

Qual dado você quer rolar?
[1] d4
[2] d6
[3] d8
[4] d10
[5] d12
[6] d20
[7] d100
''')
    
    dado = int(input(": "))# escolha do usuario
    
    print("O resultado da rolagem foi : {}".format(rolagem(dado)))
    sleep(3)

#loop	
while True:
    menu()
    
