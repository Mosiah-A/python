'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um
palíndromo, desconsiderando os espaços.'''
nome = str(input('Digite um texto: ')).strip().upper()
palavras = nome.strip()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]
'''for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palíndromo')
else:
    print("A frase não é palíndromo")