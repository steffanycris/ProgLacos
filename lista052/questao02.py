'''
2) Desenvolver um programa que apresente o total da soma de n números inteiros do número 1 até n, onde n é um
valor informado pelo usuário.
'''

n = int(input("Informe um número "))

acum = 0
cont = 1

for cont in range (1,n+1):
    #print(cont)
    acum = acum + cont
    cont = cont + 1

print("A soma dos número até ",n," é: ",acum,)