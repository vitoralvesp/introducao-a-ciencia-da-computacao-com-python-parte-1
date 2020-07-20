#O Programa deve calcular as raízes de uma equação de segundo grau.

import math 

a = float(input("Insira o valor de a: "))
b = float (input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b ** 2 - 4 * a * c

if (delta == 0):
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raiz é: ", raiz1) 

else:
    if (delta < 0):
        print("esta equação não possui raízes reais")


    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a) 
        print("A primeira raiz é",raiz2)
        print("A segunda raiz é:",raiz1)


    
