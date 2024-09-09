'''
11) Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();)
'''



base = int(input("Informe a base da sua potência: "))

ex = int(input("Agora, o expoente: "))

poten = 1
cont = 0

while(cont < ex):
    poten = poten * base
    cont = cont + 1


print(base, " elevado à ", ex, " = ", poten)

    