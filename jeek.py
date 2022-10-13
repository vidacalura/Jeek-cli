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
            jogoLocal()
        elif modo.lower() == "on":
            # Modo online
            print("\nModo ainda não disponível.\n")
        elif modo.lower() == "ia":
            # Modo vs. IA
            print("\nModo ainda não disponível.\n")
        else:
            print("\nArgumento inválido\n")          

def mostrarTabuleiro(tabuleiro):
    counter = 1

    for i in tabuleiro:
        print("\n" + str(counter), end=" ")
        counter += 1

        for j in i:
            print(j, end=" ")

    print("\n  a b c d")

def converterLance(l):
    lancesConvertidos = []

    if l == "q" or l == "Q":
        sys.exit()

    if l == "d" or l == "D":
        desistir()
        return None

    for i in l:
        if i[0] == "a" or i[0] == "b" or i[0] == "c" or i[0] == "d":
            lancesConvertidos.append([ord(i[0]) - 97, int(i[1]) - 1])
        else:
            print("\nLance inválido\n")
            return None

    return lancesConvertidos

def validarLance(l):

    if len(l) > 3:
        print("\nLance inválido\n")
        return False

    return True

def jogoLocal():

    tabuleiro = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]
    jogadorTurno = "B"

    def restart():
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                tabuleiro[i][j] = "."

        jogadorTurno = "P"

    def fimDeJogo():
        mostrarTabuleiro(tabuleiro)
        print("Fim de jogo. " + jogadorTurno + " ganham!")
        restart()

    def desistir():
        fimDeJogo()

    while 1:
        # Mostrar tabuleiro
        mostrarTabuleiro(tabuleiro)

        # Receber lance
        lance = input().split(" ")
        lance = converterLance(lance)

        if lance != None:
            # Validar lance
            if validarLance(lance):
                # Registrar lance
                for i in lance:
                    tabuleiro[i[1]][i[0]] = jogadorTurno

                # Verificar se jogo acabou
                count = 0
                for i in tabuleiro:
                    for j in i:
                        if j != ".":
                            count += 1

                if count == 15:
                    fimDeJogo()

                # Passar vez
                if jogadorTurno == "B":
                    jogadorTurno = "P"
                else:
                    jogadorTurno = "B"


# Programa
menu()