'''
12) Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
'''

num = int(input("Informe um número. (-1 encerra o programa)"))

maior = num
menor = num
cont = 0
soma = 0

while(num != -1):
    if(maior > num):
        maior = num

    if(menor < num):
        menor = num

soma = soma + num

num = int(input("Informe um número. (-1 encerra o programa)"))

cont = cont + 1

if (menor == -1):

    print("Você respondeu -1 na primeira pergunta.")

else:

    media = soma / cont

    print("O maior número escrito: ", maior)
    print("O menor número escrito: ", menor)
    print("Média dos números inseridos: ", media)

    print("---- fim do programa ----")
