# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.

# Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.

N = int(input("Digite um número inteiro: "))
div = 10
a = 1
b = N // 1 % 10
c = 1
d = 0
soma = 0

while a <= b:
    a = N // div % 10
    c = N // (div*div) % 10
    d = a + b + c
    print(d)
    break

if d >= 101:
    soma2 = 1 + 0 + 1
    print(soma2)
    

else:
    if d == 10 or 10**2 and 10**3:
        soma = 1 + 0  
        print(soma)




