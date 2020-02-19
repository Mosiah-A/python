# for c range (1.10);
#   passo
#pega

#-----------------------------#

# for c range (1.10);
#   if coin;
#       pega
#   passo
#   pula
#pega

#------------------------------#
'''for c in range(0,6):
    print('Oi')
print('FIM')'''

'''for c in range(6, 0, -1,): # (INICIO, FIM, PASSO,)
    print(c)'''
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n # s = s + n
print('O somatorio de todos os numeros é {}'.format(s))
