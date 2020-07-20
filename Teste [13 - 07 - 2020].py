def estrelinha():
    print("*" * 30)

def tracinho():
    print("-" * 30)

def computador_escolhe_jogada(n,m):
    equação = n % (m + 1)
    if (equação > 1) or (equação == 1):
        b = n - equação
        return b

        print("O computador retirou {} cartas da mesa...".format(b))
        cartas_atuais = b


def usuario_escolhe_jogada(n,m):
    a = int(input("Hey, é a sua vez!Fique atento e escolha a sua jogada...\nQuantas cartas você quer retirar da mesa? Informe aqui: "))

    a2 = n - a
    print("Você retirou {} cartas da mesa. Sendo assim, agora restam {} cartas na mesa...".format(a,a2))

    cartas_atuais = a2

    while (a > m) or (a == 0) or (a < 0):
        print("Oops!Jogada inválida!!!\nVocê não pode retirar mais cartas do que já foi estabelecido anteriomente e não é permitido retirar nenhuma carta. Tente novamente...")

        a = int(input("Quantas cartas você quer retirar da mesa?\nInforme aqui: "))
        return a

def Menu():
    estrelinha()
    print("SEJA BEM VINDO AO JOGO DO NIM")
    estrelinha()


    print("\nA seguir, informe o número correspondente a sua escolha. Se você deseja jogar uma partida: digite 1, ou se você quiser jogar um Campeonato: digite 2.")

    print("1 - Jogar uma partida isolada: \n2 - Jogar um campeonato: ")

    Jogar_uma_Partida = 1
    Jogar_um_Campeonato = 2

    escolha = int(input("\n\n\nInforme a sua escolha: "))

    if (escolha == 1):
            partida()

    else:
        if (escolha == 2):
            campeonato()

    while escolha > 2:

        tracinho()
        print("Oops! Escolha inválida!!!\nDigite 1 para jogar uma partida ou 2 para jogar um campeonato.")
        tracinho()
        escolha = int(input("\n\nInforme aqui: ")
        
def partida():

    estrelinha()
    print("Você escolheu jogar uma partida!")
    estrelinha()

    tracinho()
    n = int(input("INFORMAÇÃO IMPORTANTE\nDigite aqui o número de cartas que haverá sobre a mesa antes do jogo iniciar: "))
    m = int(input("INFORMAÇÃO IMPORTANTE\nDigite aqui o número MÁXIMO de cartas que um jogador pode retirar por vez: "))
    tracinho()

    computador_joga = 0
    usuario_joga = 0

    while (m > n) or (n == 0) or (m == 0):
        print("Oops!Jogada inválida!!!\nNenhum dos valores pedidos pode valer 0 e o número MÁXIMO de cartas que podem ser retiradas pelo jogador por vez não pode ser maior que o número total de cartas.\nTente novamente...")

        tracinho()
        n = int(input("INFORMAÇÃO IMPORTANTE\nDigite aqui o número de cartas que haverá sobre a mesa antes do jogo iniciar: "))
        m = int(input("INFORMAÇÃO IMPORTANTE\nDigite aqui o número MÁXIMO de cartas que um jogador pode retirar por vez: "))
        tracinho()

        equação = n % (m + 1)
        jogada = 0

        while (n == 0):
            if equação == 0:
                print("Você começa!")
                usuario_escolhe_jogada(n,m)
                jogada = 1

            else:
                print("Computador começa!")
                computador_escolhe_jogada(n,m)
                jogada = 1

        if (equação == 1) or (equação > 1):
            print("Computador começa!")
            computador_escolhe_jogada(n,m)
            jogada = 1

        else:
            print("Você começa!")
            usuario_escolhe_jogada(n,m)
            jogada = 1


Menu()
        

    