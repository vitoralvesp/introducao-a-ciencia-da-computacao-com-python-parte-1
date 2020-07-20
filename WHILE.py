numero = int(input("Vamos fazer um joguinho hehe! Digite um número e entenda a lógica:"))

num = 1
while num < 0:
    a = numero // 1 % 10
    b = numero // 10 % 10
    c = numero // 100 % 10
    d = numero // 1000 % 10
    print("{}. O que houve?")
    