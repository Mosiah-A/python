casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salario: R$'))
parcela = int(input('Quantas parcelas? '))
min = salario * 30/100
mensalidade = casa / (parcela * 12)
if mensalidade <= min:
    print('\033[32:1m APROVADO\033[m')
    print('O valor á ser pago por mês será de : \033[33:1mR$ {:.2f}'.format(mensalidade))
else:
    print('\033[31mNEGADO')