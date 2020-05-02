#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
at = date.today().year
idade = at - ano
print('O atleta tem \033[34m{} Anos\033[m'.format(idade))
if idade <= 9:
    print('Classificação: \033[32mMIRIM')
elif idade <= 14:
    print('Classificação: \033[32mINFANTIL')
elif idade <= 19:
    print('Classificação: \033[32mJÚNIOR')
elif idade <= 25:
    print('Classificação: \033[32mSÊNIOR')
else:
    print('Classificação: \033[32mMASTER')