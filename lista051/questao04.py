'''
4) Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100)
'''

cont = 1
acum = 0

while (cont <= 100):

    acum = acum + cont  #acum += cont
    cont = cont + 1

print("A soma dos cem primeiros números inteiros é: ", acum)
