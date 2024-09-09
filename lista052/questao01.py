'''
1) Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 1000
a 1500.
'''


for contador in range(1000,1501):
    imp = contador%2

    if (imp == 1):
        print(contador)

    contador = contador+1