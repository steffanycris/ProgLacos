'''
3) Desenvolver um programa que apresente os resultados de uma tabuada de um número qualquer informado
pelo usuário.
'''

n = int(input("Informe um número "))

for cont in range (11):
    mult = cont*n
    print(n,".",cont," = ",mult)
    cont = cont+n