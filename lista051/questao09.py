'''
9) Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2.
'''

cont = 1
acum = 0

while (cont <= 500):
    #print(cont)
    acum = acum+cont
    cont += 2

print("A soma dos valores existentes na faixa de 0 até 500, é:",acum)