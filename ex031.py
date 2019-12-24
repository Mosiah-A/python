#Desenvolvaum programa que pergunte a distancia de uma viagem em Km. calcule o preço da passagem.
#cobrando R$:0,50 po Km para viagens ate 200Km e R$:0,45 para viagens mais longas

from time import sleep

km = float(input('Quantos km é a viagem: '))

print('Calculando...')
sleep(3)

'''if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45'''

preço = km * 0.50 if km <= 200 else km * 0.45

print('O valor é R$:{:.2f}'.format(preço))
