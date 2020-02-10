#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
print('Seu IMC É {:.1f} Você esta'.format(imc), end=' ')
if imc < 18.5:
    print('\033[31mAbaixo do Peso')
elif 18.5 <= imc < 25:
    print('\033[32mno Peso Ideal')
elif 25 <= imc < 30:
    print('\033[32mSobrepeso')
elif 30 <= imc < 40:
    print('\033[32mcom Obesidade')
else:
    print('\033[32mcom Obesidade Morbida')