'''
7) Desenvolver um programa que apresente no final a soma dos valores pares existentes na faixa de 3 até 21.
'''

acum = 0

for cont in range (3,22):
    par = cont%2

    if (par == 0):
        acum = acum + cont

    cont = cont+1

print("A soma dos números pares de 3 até 21, é: ",acum)
