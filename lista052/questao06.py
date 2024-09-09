'''
6) Desenvolver um programa que apresente o valor de uma potência de uma base qualquer elevada a um expoente
qualquer, ou seja, de b^e
, onde os valores de b e e são fornecidos pelo usuário, sem utilizar Math.pow().
'''

base = int(input("Informe a base da sua potência: "))

ex = int(input("Agora, o expoente: "))

for cont in range (ex):
    poten = base*base

    cont = cont+1
print("O valor da potência fornecida é: ",poten)
