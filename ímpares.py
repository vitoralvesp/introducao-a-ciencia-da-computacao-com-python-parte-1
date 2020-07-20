#Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.

def main():
    '''
    Programe que lê um inteiro positivo n e imprime os n 
    primeiros inteiros positivos.

    Exemplo de execução:

    Digite o valor de n: 3
    1
    3
    5
    >>>
    '''
    
    print("Gerador do n primeiros números ímpares positivos\n")

    # leia o valor de n
    n = int(input("Digite o valor de n: "))

    # contador de ímpares impressos
    i = 0

    # primeiro número ímpar
    ímpar = 1

    # imprima os n primeiros impares, um por linha
    while i < n: 
        # imprima o próximo número ímpar
        print(ímpar)

        # incremente p contador
        i = i + 1

        # determine o próximo ímpar
        ímpar = ímpar + 2
           

        
