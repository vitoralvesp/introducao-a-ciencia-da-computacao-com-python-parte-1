#Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro.

seg = int(input("Digite os segundos: "))


a = seg//60//60//24
b = (seg//60//60)%24
c = (seg//60)%60
d = seg%60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.") 