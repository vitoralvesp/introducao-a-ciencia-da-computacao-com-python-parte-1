#O Programa deve ler os números inseridos pelo usuário e imprimir na tela se eles estão em ordem crescente.

n = int(input("Insira um número:"))
n2 = int(input("Insira outro número:"))
n3 = int(input("Insira mais outro número:"))

if (n < n2 < n3 ):
    print("crescente")

else:
    print("não está em ordem crescente")