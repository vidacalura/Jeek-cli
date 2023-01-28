import sys


# Funções
def menu():
    modo = ""

    while modo != "l":
        modo = input(
            "\nJeek Online-Cli - Beta v.0.1\n\n" +
            "Jogar:\n" +
            "(l) Jogar 1v1 local\n" +
            "(on) Jogar 1v1 online (em breve)\n" +
            "(ia) Jogar contra bot (em breve)\n"
        )

        if modo.lower() == "l":
            jogo_local()
        elif modo.lower() == "on":
            # Modo online
            print("\nModo ainda não disponível.\n")
        elif modo.lower() == "ia":
            # Modo vs. IA
            print("\nModo ainda não disponível.\n")
        else:
            print("\nArgumento inválido\n")          


def mostrar_tabuleiro(tabuleiro):
    counter = 1

    for i in tabuleiro:
        print("\n" + str(counter), end=" ")
        counter += 1

        for j in i:
            print(j, end=" ")

    print("\n  a b c d")


def converter_lance(l):
    lances_convertidos = []

    if l == "q" or l == "Q":
        sys.exit()

    if l == "d" or l == "D":
        desistir()
        return None

    for i in l:
        if len(i) != 2:
            print("\nLance inválido\n")
            return None
        if i[0] == "a" or i[0] == "b" or i[0] == "c" or i[0] == "d":
            lances_convertidos.append([ord(i[0]) - 97, int(i[1]) - 1])
        else:
            print("\nLance inválido\n")
            return None

    return lances_convertidos


def validar_lance(l, tabuleiro):

    if len(l) > 3:
        print("\nLance inválido\n")
        return False

    # Verifica lance espelhado


    # Verifica se casa já foi preenchida
    for i in l:
        if tabuleiro[i[1]][i[0]] != ".":
            return False
                
    # Verifica se o lance é legal
    comum = ""
    for i in l:
        if comum == "":
            comum = list(i)
        else:
            if i[0] == comum[0]:
                comum[0] = i[0]
                comum[1] = ""
            elif i[1] == comum[1]:
                comum[1] = i[1]
                comum[0] = ""
            else:
                return False

    return True


def count_pecas(tabuleiro):
    count = 0
        for i in tabuleiro:
            for j in i:
                if j != ".":
                    count += 1


def jogo_local():
    
    tabuleiro = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]

    jogador_turno = "B"

    def restart():
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                tabuleiro[i][j] = "."

        jogador_turno = "P"

    def fim_de_jogo():
        mostrar_tabuleiro(tabuleiro)
        print("Fim de jogo. " + jogador_turno + " ganham!")
        restart()

    def desistir():
        fim_de_jogo()

    while 1:
        # Mostrar tabuleiro
        mostrar_tabuleiro(tabuleiro)

        # Receber lance
        lance = input().split(" ")
        lance = converter_lance(lance)

        if lance != None:
            # Validar lance
            if validar_lance(lance, tabuleiro):
                # Registrar lance
                for i in lance:
                    tabuleiro[i[1]][i[0]] = jogador_turno

                # Verificar se jogo acabou
                if count_pecas(tabuleiro) == 15:
                    fim_de_jogo()

                # Passar vez
                if jogador_turno == "B":
                    jogador_turno = "P"
                else:
                    jogador_turno = "B"


# Programa
menu()