#Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

#Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima longe na saída. Caso o contrário, quando a distância for menor que 10, imprima perto.

x1 = float(input("Digite o valor correpondente à coordenada x: "))
y1 = float(input("Digite o valor correspondente à coordenada y: "))

x2 = float(input("Insira agora, o valor correspondente ao outro ponto do mesmo plano, respectivamente ao x:"))
y2 = float(input("Insira agora, o valor correspondente ao outro ponto do mesmo plano, respectivamente ao y:"))

import math

#Hora de aplicar a fórmula d(x,y)=(x1​−x2​)* 2 +(y1​−y2​)* 2

dxy = (x1 - x2)* 2 + (y1 - y2)* 2
math.sqrt (dxy)

if (dxy >= 10):
    print("longe")

else:
    if (dxy <= 10):
        print("perto")