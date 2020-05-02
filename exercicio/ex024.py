#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'

#nome = str(input('Digite uma cidade: ')) .strip().upper().split()
#print('Essa cidade começa com santo? {}'.format('SANTO' in nome[0]))

cid = str(input('Digite uma cidade: ')).strip()
print('Essa cidade começa com santo? {}'.format(cid[:5].upper() == 'SANTO'))
