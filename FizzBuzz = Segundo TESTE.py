n = int(input("Digite um número:"))
n2 = n // 3 
n3 = n // 5
n4 = n % 3 
n5 = n % 5

if (n4 == 0) and (n5 == 0):
    print("FizzBuzz")

else:
    print(n)