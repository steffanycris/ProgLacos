'''
4) Desenvolver um programa que apresente todos os números divisíveis por 5 que sejam menores que 50.
'''

print("Os números divisíveis por 5, de 1 até 50 é: ")

for cont in range (1,51):
    div5 = cont%5

    if (div5 == 0):
        print(cont)

    cont = cont + 1
