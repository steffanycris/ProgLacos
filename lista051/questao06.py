'''
6) Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da
multiplicação sucessiva de n por 3 enquanto o produto for menor que 250. (n x 3; n x 3 x 3; n x 3 x 3 x 3 etc...).
'''

n = int(input("Informe um número "))

cont = 1

if(n <= 50):
 print("A multiplicação sucessiva desse número por 3, enquanto o produto for menor que 250, é: ")
 while (n <= 250):

  print(n, "(x", cont, ")")
  n =  n * 3
  cont = cont + 1


else:
 print("O número informado não é menor ou igual a 50 ")

