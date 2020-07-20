#Receba um número inteiro positivo na entrada e imprima os primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

n = int(input("Digite o valor de n:"))
soma = 0

while n != 0 and n > 0:
    soma = n % 10
    n = int(n / 10)
    print(soma)

    

    


    


    
