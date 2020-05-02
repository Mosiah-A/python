#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('Sexo\n[1] Masculino\n[2] Feminino')
sexo = int(input('Digite a resposta: '))
if sexo == 2:
    print('O serviço nao é obrigatorio pra você.')
    print('saindo...')
elif sexo == 1:
    ano = int(input('Qual ano você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - ano
    if ano > ano_atual:
        print('\033[31mERRO, TENTE NOVAMENTE')
    else:
        print("Quem nasceu no ano {} tem \033[32m{} anos \033[mem {}".format(ano, idade, ano_atual))
        if idade == 18:
            print('Você deve se alistar \033[31mIMEDIATAMENTE. ')
        elif idade > 18:
            print('Você já devia ter se alistado há \033[31m{} anos\033[m.'.format(idade-18))
            print('Seu alistamento foi em \033[31m{}'.format(ano + 18))
        elif idade < 18:
            falta = 18 - idade
            if falta == 1:
                print('Ainda falta \033[32m{} ano\033[m para seu alistamento.'.format(falta))
            else:
                print('Ainda faltam \033[32m{} anos\033[m para seu alistamento.'.format(falta))
            print('Seu alstamento será em \033[32m{}.'.format(ano + 18))
else:
    print('\033[31mERRO')
    
