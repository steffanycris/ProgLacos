'''
5) Desenvolver um programa que apresente as potências de 2, variando de 0 a 10.
'''
import math

cont = 0

for cont in range (1,11):
    print(f"2 elevado a {cont} = {math.pow(cont,2)}")

    cont = cont + 1

