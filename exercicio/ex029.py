# Escreva um programa que leia a velocidade de um carro, se ele ultrapassar
# 80Km/h. mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar R$:7,00 por cada Km acima do limite

km = float(input('Digite a velocidade do carro: '))
if km > 80:
    print('Voce foi multado.')
    multa = (km - 80) * 7
    print('O valor a ser pago é de R$:{:.2f}'.format(multa))
