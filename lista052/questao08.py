'''
8) Desenvolver um programa que pergunte 20 vezes o nome inteiro de uma pessoa, sexo e idade, e exiba o nome
inteiro das pessoas que são do sexo masculino e possuem 21 anos ou mais.
'''

for cont in range(1,21):
    nome = input("Qual o seu nome completo? ")
    idade = int(input("Quantos anos você tem? "))
    sexo = input("Qual o seu sexo? ")

    if (idade >= 21) and (sexo == "Masculino"):
        print(nome)

    
