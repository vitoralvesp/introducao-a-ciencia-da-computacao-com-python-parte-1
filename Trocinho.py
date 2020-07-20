#Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

a = int(input("Digite um número maior que zero: "))
I = 1 
B = 1

while B <= a:
    J = (I % 2)
    if J == 1 or I==1:
        print("N ",B)
        print(I)
        B = B + 1
    I = I + 1

else:
    print("Digite um número maior que zero.")



    
