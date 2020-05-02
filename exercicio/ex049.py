#xercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

t = int(input("A tabuada de qual numero voce quer ver? "))
for c in range(0, 11):
    print("| {:2} x {:2} = {:2} |".format(t, c, (c*t)))
