from random import shuffle
from sys import exit
import sys
from copy import deepcopy

sys.setrecursionlimit(1500000)

class Jogo:
    def __init__(self):
        self.movimentos = [] # Lista de todos os movimentos
        self.turno = "B"     # B - Brancas, P - Pretas
        self.tabuleiro = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]

    def mostrar_tabuleiro(self):
        counter = 1
        for linha in self.tabuleiro:
            print("\n" + str(counter), end=" ")
            counter += 1

            for casa in linha:
                print(casa, end=" ")

        print("\n  a b c d")


    def registrar_movimento(self, movimento):
        if self.validar_movimento(movimento):
            self.movimentos.append(movimento)
            
            movimento = converter_movimento(movimento)
            for i in movimento:
                self.tabuleiro[i[1]][i[0]] = self.turno

            if self.turno == "B":
                self.turno = "P"
            else:
                self.turno = "B"


    def validar_movimento(self, movimento):
        movimento = converter_movimento(movimento)

        if movimento == None:
            return False

        if len(movimento) > 3:
            print("\nLance inválido\n")
            return False

        # Verifica lance espelhado
        if len(self.movimentos) == 1:
            movimento_brancas = converter_movimento(self.movimentos[0])

            if len(movimento_brancas) == len(movimento):
                if len(movimento_brancas) == 1:
                    if movimento_brancas[0][0] + movimento_brancas[0][1] + movimento[0][0] + movimento[0][1] == 6:
                        return False

                elif len(movimento_brancas) == 2:
                    if (movimento_brancas[0][0] + movimento_brancas[0][1] + movimento[0][0] + movimento[0][1]
                    + movimento_brancas[1][0] + movimento_brancas[1][1] + movimento[1][0] + movimento[1][1] == 12):
                        return False

                elif len(movimento_brancas) == 3:
                    if (movimento_brancas[0][0] + movimento_brancas[0][1] + movimento[0][0] + movimento[0][1]
                    + movimento_brancas[1][0] + movimento_brancas[1][1] + movimento[1][0] + movimento[1][1]
                    + movimento_brancas[2][0] + movimento_brancas[2][1] + movimento[2][0] + movimento[2][1] == 18):
                        return False 

        # Verifica se casa já foi preenchida
        for i in movimento:
            if self.tabuleiro[i[1]][i[0]] != ".":
                return False

        if len(movimento) == 1:
            return True            
        
        # Verifica se o lance é legal
        comum = ""
        for i in movimento:
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

        # Verifica se peças estão conectadas
        movimentos_ok_lista = [
            [0, 1], [1, 2], [2, 3],
            [1, 0], [2, 1], [3, 2],
            [0, 1, 2], [1, 2, 3],
            [1, 0, 2], [2, 1, 3],
            [2, 1, 0], [3, 2, 1],
            [1, 2, 0], [2, 3, 1],
            [2, 3, 1], [3, 1, 2],
            [3, 2, 1], [1, 3, 2],
        ]

        nao_comum_lista = []
        if comum[1] == '':
            for i in movimento:
                nao_comum_lista.append(i[1])
        else:
            for i in movimento:
                nao_comum_lista.append(i[0])

        if nao_comum_lista not in movimentos_ok_lista:
            return False

        return True


    def get_count_pecas(self):
        count = 0
        for linha in self.tabuleiro:
            for casa in linha:
                if casa != ".":
                    count += 1

        return count


    def verificar_vitoria(self):
        if self.get_count_pecas() == 15:
            if self.turno == "B":
                return "P"
            else:
                return "B"

        elif self.get_count_pecas() > 15:
            return self.turno

        else:
            return None


def converter_movimento(movimento):
    if movimento == None:
        return None

    movimentos_convertidos = []

    if movimento == "q":
        print("\nSaindo do jogo...\n")
        exit()

    if movimento == "d":
        print("\nVocê desistiu.\nJeekens ganha.\n")
        exit()

    for i in movimento:
        i = i.lower()
        if len(i) != 2:
            print("\nMovimento inválido\n")
            return None
        if i[0] == "a" or i[0] == "b" or i[0] == "c" or i[0] == "d":
            movimentos_convertidos.append([ord(i[0]) - 97, int(i[1]) - 1])
        else:
            print("\nMovimento inválido\n")
            return None

    return movimentos_convertidos


def tirar_lado():
    lados = ["P", "B"]
    shuffle(lados)

    return lados[0], lados[1]


def jeekens_movimento():
    movimentos_legais = deepcopy(todos_movimentos)
    melhor_pontuacao = None
    melhor_movimento = None

    movimentos_aberturas = ["a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4", "c2 c3", "b2 b3"]

    if len(jogo.movimentos) == 0:
        shuffle(movimentos_aberturas)
        return movimentos_aberturas[0]

    if jeekens == "B":
        melhor_pontuacao = -1
    else:
        melhor_pontuacao = 2

    i = 0
    while i < len(movimentos_legais):
        if jogo.validar_movimento(movimentos_legais[i].split(" ")) == False:
            movimentos_legais.remove(movimentos_legais[i])
        else:
            jogo_simul = deepcopy(jogo)
            jogo_simul.registrar_movimento(movimentos_legais[i].split(" "))
            m = movimentos_legais[i]
            if jeekens == "B":
                pontuacao_movimento = minimax(jogo_simul, profundidade_jeekens, False)
                if pontuacao_movimento > melhor_pontuacao:
                    melhor_pontuacao = pontuacao_movimento
                    melhor_movimento = m
            else:
                pontuacao_movimento = minimax(jogo_simul, profundidade_jeekens, True)
                if pontuacao_movimento < melhor_pontuacao:
                    melhor_pontuacao = pontuacao_movimento
                    melhor_movimento = m
        
            i += 1
    
    if melhor_movimento == None:
        shuffle(movimentos_legais)
        melhor_movimento = movimentos_legais[0] 

    return melhor_movimento


def minimax(jogo_copia, profundidade, is_brancas):
    # Verifica vitória
    jogador_vitorioso = jogo_copia.verificar_vitoria()
    if jogador_vitorioso == humano:
        return 0
    elif jogador_vitorioso == jeekens:
        return 1

    if profundidade == 0:
        return 0

    if is_brancas:
        movimentos_legais = deepcopy(todos_movimentos)
        melhor_pontuacao = -1
        melhor_movimento = None

        i = 0
        while i < len(movimentos_legais):
            m = movimentos_legais[i]
            if jogo_copia.validar_movimento(m.split(" ")) == False:
                movimentos_legais.remove(m)
            else:
                jogo_simul = deepcopy(jogo_copia)
                jogo_simul.registrar_movimento(m.split(" "))
                if jeekens == "B":
                    pontuacao_movimento = minimax(jogo_simul, profundidade - 1, False)
                    if pontuacao_movimento > melhor_pontuacao:
                        melhor_pontuacao = pontuacao_movimento
                        melhor_movimento = m
                else:
                    pontuacao_movimento = minimax(jogo_simul, profundidade - 1, True)
                    if pontuacao_movimento < melhor_pontuacao:
                        melhor_pontuacao = pontuacao_movimento
                        melhor_movimento = m

                i += 1

        return melhor_pontuacao

    else:
        movimentos_legais = deepcopy(todos_movimentos)
        melhor_pontuacao = 1
        melhor_movimento = None

        i = 0
        while i < len(movimentos_legais):
            m = movimentos_legais[i]
            if jogo_copia.validar_movimento(m.split(" ")) == False:
                movimentos_legais.remove(m)
            else:
                jogo_simul = deepcopy(jogo_copia)
                jogo_simul.registrar_movimento(m.split(" "))
                if jeekens == "B":
                    pontuacao_movimento = minimax(jogo_simul, profundidade - 1, True)
                    if pontuacao_movimento < melhor_pontuacao:
                        melhor_pontuacao = pontuacao_movimento
                        melhor_movimento = m
                else:
                    pontuacao_movimento = minimax(jogo_simul, profundidade - 1, False)
                    if pontuacao_movimento > melhor_pontuacao:
                        melhor_pontuacao = pontuacao_movimento
                        melhor_movimento = m

                i += 1

        return melhor_pontuacao


# Início do programa
print("Jeek-CLI v.0.0.3\n* Feito por Vidacalura *")
profundidade_jeekens = int(input("Escolha a profundidade do Jeekens (1 a 4): "))

print("\nIniciando jogo contra Jeekens (" + str(200 + (profundidade_jeekens - 1) * 100) + ")")

jogo = Jogo()
humano, jeekens = tirar_lado()

todos_movimentos = [
    "a1", "a2", "a3", "a4",
    "b1", "b2", "b3", "b4",
    "c1", "c2", "c3", "c4",
    "d1", "d2", "d3", "d4",
    "a1 a2", "a2 a3", "a3 a4",
    "b1 b2", "b2 b3", "b3 b4",
    "c1 c2", "c2 c3", "c3 c4",
    "d1 d2", "d2 d3", "d3 d4",
    "a1 a2 a3", "a2 a3 a4",
    "b1 b2 b3", "b2 b3 b4",
    "c1 c2 c3", "c2 c3 c4",
    "d1 d2 d3", "d2 d3 d4",
]

#jogo = Jogo()
#jogo.turno = "P"
#jogo.tabuleiro = [
#    ["B", "P", "P", "B"],
#    [".", ".", ".", "B"],
#    [".", ".", ".", "B"],
#    ["B", "B", "B", "B"]
#]

#humano = "B"
#jeekens = "P"

#print(jeekens_movimento())

# loop do jogo
while 1:
    movimento = None
    if jogo.turno == humano:
        movimento = input("\nSua vez: ").split(" ")
    
    else:
        # Jeekens faz um movimento
        movimento = jeekens_movimento().split(" ")

    jogo.registrar_movimento(movimento)

    jogador_vitorioso = jogo.verificar_vitoria()
    if jogador_vitorioso != None:
        if jogador_vitorioso == humano:
            print("\nVocê venceu! Humanos vencem das máquinas! :D")
        else:
            print("\nVocê perdeu! Jeekens vence! D:")

        exit()

    jogo.mostrar_tabuleiro()