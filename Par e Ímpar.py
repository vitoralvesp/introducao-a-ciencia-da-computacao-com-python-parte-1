#Par ou Ímpar?
par = float(input("Digite um número:"))
numero = par // 2
numero2 = par % 2

if (numero2 >= 0):
    print("par")

else:
    if (numero2 < 0):
        print("ímpar")
              