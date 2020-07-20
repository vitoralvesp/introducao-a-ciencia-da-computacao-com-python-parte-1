#Escreva um programa que receba um número natural na entrada e imprima n! (fatorial) na saída.

n = int(input("Digite o valor de n: "))

if n == 1:
    print(n)

if (n < 0):
    print("Números fatoriais devem ser positivos, somente :-(")

if (n == 0):
    print(1)

if n > 1:
    resu = 0
    while n > 1:
        if resu == 0:
            resu = n*(n-1)
        else:
            resu=resu*(n-1)
        n=(n-1)

    print(resu)