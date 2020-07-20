#Imprimir na tela FizzBuzz se o número inserido pelo usuário for divisível por 3 e 5. Caso contrário, deve imprimir o número novamente.

f1 = int(input("Insira um número:"))
f2 = int(input("Insira outro número:"))

n = f1 // 3
n2 = f1 % 3

#Agora vai o f2
m = f2 // 5
m2 = f2 % 5

if (n2 == 0) and (m2 == 0):
    print("FizzBuzz")

else:
    if (n2 > 0) and (m2 > 0):
        print(f1)
        print(f2)