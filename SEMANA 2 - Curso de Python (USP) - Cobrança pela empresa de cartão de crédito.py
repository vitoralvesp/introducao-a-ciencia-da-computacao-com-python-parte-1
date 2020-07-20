#Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.

print("Preencha corretamente as informações a seguir")

n = input("Insira o seu nome completo:")
i = input("Insira o dia que a sua conta irá vencer:")
p = input("Insira o mês desta conta:")
m = input("Insira o valor da fatura(somente em REAIS R$):")

print("Olá, {}. A sua fatura com o vencimento no dia {} de {} no valor de {} está fechada.".format (n,i,p,m))