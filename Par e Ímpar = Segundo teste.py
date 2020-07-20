#O programa deve identificar se o número é par ou ímpar

n = int(input("Digite um número:"))
n2 = n // 2
n3 = n % 2

if (n3 == 0):
    print("par")

else:
    print("ímpar")