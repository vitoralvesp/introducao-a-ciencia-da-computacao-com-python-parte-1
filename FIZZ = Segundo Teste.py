n = int(input("Digite um número:"))
n2 = n // 3
n3 = n % 3

if (n3 == 0):
    print("Fizz")

else:
    if (n3 < 0) or (n3 > 0):    
        print(n)