##Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#modulo (Bibliotecas)
from datetime import date
print('=' * 29)
print('=' * 3 , 'Analizar Ano Bissexto', '='* 3)
print('=' * 29)
ano = int(input('Qual ano você deseja analizar? Coloque 0 (zero) para o ano atual: ')) #Entrada
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0: # anos que são divisiveis por 4 e 400 são Bixesto exeto os que são divisiveis por 400
    print('O Ano {} é BISSExTO'.format(ano)) #Saida para ano bissexto
else:
    print('O Ano {} não é BISSExTO'.format(ano)) #Saida para anos não bissexto
