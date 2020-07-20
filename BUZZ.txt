#O programa deve imprimir na tela BUZZ se o número inserido for divisível por 5. Caso contrário, deve imprimir o número inserido pelo usuário.

b = int(input("Digite um número:"))
b2 = b // 5
b3 = b % 5

if (b3 == 0):
    print("Buzz")

else:
    print(b)