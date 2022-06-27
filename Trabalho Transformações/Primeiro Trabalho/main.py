largura_tela = 1920
altura_tela = 1080

pontos = [[0, 0], [0, 10], [10, 10], [10, 0]]

#pontos = [[0, 0], [0, 20], [20, 20], [20, 0]]

arestas = [[[0, 0], [0, 10]], [[0, 10], [10, 10]], [[10, 10], [10, 0]], [[10, 0], [0, 0]]]

#arestas = [[[0, 0], [0, 20]], [[0, 20], [20, 20]], [[20, 20], [20, 0]], [[20, 0], [0, 0]]]

def gerar_matriz(largura, altura):
    matriz = []
    for i in range(largura):
        coluna = []
        for i in range(altura):
            coluna.append(False)
        matriz.append(coluna)
    return matriz

def criar_tela(largura, altura):
    tela = gerar_matriz(largura, altura)
    return tela


def criar_objeto(pontos, arestas):
    maior_x = 0
    maior_y = 0
    for i in range(len(pontos)):
        if pontos[i][0] > maior_x:
            maior_x = pontos[i][0]
        if pontos[i][1] > maior_y:
            maior_y = pontos[i][1]
    
    retangulo = gerar_matriz(maior_x + 1, maior_y + 1)
    retangulo = desenhar_linhas(arestas, retangulo)
    return retangulo


def desenhar_linhas(arestas, retangulo):
    for i in range(len(arestas)):
        if arestas[i][0][0] == arestas[i][1][0] and arestas[i][0][1] != arestas[i][1][1]:
            for j in range(abs(arestas[i][0][1] - arestas[i][1][1]) + 1):
                if arestas[i][0][1] <= arestas[i][1][1]:
                    retangulo[arestas[i][0][0]][arestas[i][0][1] + j - 1] = True
                elif arestas[i][0][1] >= arestas[i][1][1]:
                    retangulo[arestas[i][1][0]][arestas[i][1][1] + j - 1] = True
        elif arestas[i][0][1] == arestas[i][1][1] and arestas[i][0][0] != arestas[i][1][0]:
            for j in range(abs(arestas[i][0][0] - arestas[i][1][0]) + 1):
                if arestas[i][0][0] <= arestas[i][1][0]:
                    retangulo[arestas[i][0][0] + j - 1][arestas[i][0][1]] = True
                elif arestas[i][0][0] >= arestas[i][1][0]:
                    retangulo[arestas[i][1][0] + j - 1][arestas[i][0][1]] = True
    return retangulo


def mostrar_objeto(objeto):
    for i in range(len(objeto)):
        for j in range(len(objeto[0])):
            if objeto[i][j] == False:
                print("  ", end="")
            else:
                print("# ", end="")
        print("")


objeto = criar_objeto(pontos, arestas)
mostrar_objeto(objeto)
