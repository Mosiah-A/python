"""nome = str(input('Digite seu nome: ')).strip().title()
if nome == 'Mosiah':                 #condicional simples
    print('Quenome lindo você tem')
else:                                #condicional composta
    print('Seu nomeé tão normal!')
print('bom dia, {}!'.format(nome))"""

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Aprovado')
else:
    print('recuperação')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('Aprovado' if m >= 6.0 else 'Reprovado')
