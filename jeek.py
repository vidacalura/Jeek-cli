import sys

# Funções
def mostrarMenu():
    modo = input(
        "\n" +
        "Jeek Online-Cli - Beta v.0.1\n\n" +
        "Jogar:\n" +
        "(l) Jogar 1v1 local\n" +
        "(on) Jogar 1v1 online (em breve)\n" +
        "(ia) Jogar contra bot (em breve)\n"
    )

    return modo

def menu():
    modo = mostrarMenu()

    if modo.lower() == "l":
        jogoLocal()
    elif modo.lower() == "on":
        # Modo online
        print("\nModo ainda não disponível.\n")
        menu()
    elif modo.lower() == "ia":
        # Modo vs. IA
        print("\nModo ainda não disponível.\n")
        menu()
    else:
        print("\nArgumento inválido\n")
        menu()

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

    if l.lower() == "d":
        desistir()
        return None

    for i in l:
        if i[0].lower() == "a" or i[0].lower() == "b" or i[0].lower() == "c" or i[0].lower() == "d":
            i = i.lower()
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

def 

def fimDeJogo(tabuleiro):
    count = 0

    for i in tabuleiro:
        for j in i:
            if j != ".":
                count += 1

    if count == 15:
        return True

    return False


def desistir():
    # restart

def jogoLocal():
    tabuleiro = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]
    jogadorTurno = "B"

    # Verificar se jogo encerrou
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

                if fimDeJogo(tabuleiro):
                    mostrarTabuleiro(tabuleiro)
                    print("Fim de jogo. " + jogadorTurno + " ganham!")
                    # restart()
                    sys.exit()

                # Passar vez
                if jogadorTurno == "B":
                    jogadorTurno = "P"
                else:
                    jogadorTurno = "B"


# Programa
menu()