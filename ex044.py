#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print('{:~^30}'.format(' Simulador de Loja '))
preço = float(input('Qual o preço da compra: R$ '))
print('''Qual a forma de pagamento?
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
r = int(input('Digite sua resposta: '))
if r ==1:
    npreço = preço - (preço * 10/100)
    print('A compra de R${:.2f} vai para R${:.2f}'.format(preço,npreço))
elif r == 2:
    npreço = preço - (preço * 5/100)
    print('A compra de R${:.2f} vai para R${:.2f}'.format(preço,npreço))
elif r == 3:
    parcela = preço / 2
    print('A compra foi parcelada em 2x no valor de R${:.2f}'.format(parcela))
elif r == 4:
    npreço = preço + (preço * 20/100)
    vezes= int(input('Em quantas vezes voce quer pagar? '))
    parcela = npreço / vezes
    print('A compra de R${:.2f} vai ser paga em {} vezes de R${:.2f}.\ndando um total de R${:.2f}'.format(preço,vezes,parcela,npreço))
else:
    print('\033[31mOPÇÃO INVALIDA')
