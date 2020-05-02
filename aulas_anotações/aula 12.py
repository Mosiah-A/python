#if, else,elife.

nome = str(input('Qualo o seu nome: ')).title()
if nome == 'Mosiah':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular!')
elif nome in 'Ana Claudia Jessica':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, \033[32m{}\033[m! '.format(nome))
