import pygame, sys, math, time

from pygame.constants import KEYDOWN, K_0, K_1, K_2, K_3, K_4, K_SPACE

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

largura_tela = 1280
altura_tela = 720

screen = pygame.display.set_mode((largura_tela, altura_tela))


class objeto:
    def __init__(this, pontos, arestas):
        this.pontos = pontos
        this.arestas = arestas
    
    def rotacionar(self, graus):
        rad = 2 * math.pi * graus/360
        cos = math.cos(rad)
        sen = math.sin(rad)
        for ponto in self.pontos:
            ponto0 = ponto[0] * cos - ponto[1] * sen
            ponto1 = ponto[0] * sen + ponto[1] * cos
            ponto[0] = ponto0
            ponto[1] = ponto1
        

    def redimensionarX(self, proporcao):
        for ponto in self.pontos:
            ponto[0] *= proporcao
        
    
    def redimensionarY(self, proporcao):
        for ponto in self.pontos:
            ponto[1] *= proporcao
        

    def redimensionar(self, proporcao):
        for ponto in self.pontos:
            ponto[0] *= proporcao
            ponto[1] *= proporcao

    def transladar(self, x, y):
        for ponto in self.pontos:
            ponto[0] += x
            ponto[1] += y
    
    def cisalhar(self, x, y):
        for ponto in self.pontos:
            ponto0 = ponto[0] + x * ponto[1]
            ponto1 = ponto[1] + y * ponto[0]
            ponto[0] = ponto0
            ponto[1] = ponto1

    def refletirX(self):
        for ponto in self.pontos:
            ponto[0] = largura_tela -ponto[0]

    def refletirY(self):
        for ponto in self.pontos:
            ponto[1] = altura_tela -ponto[1]     

    def refletir(self):
        for ponto in self.pontos:
            ponto[0] = largura_tela -ponto[0]
            ponto[1] = altura_tela -ponto[1] 

    def mostrar(self):
        for aresta in self.arestas:
            pygame.draw.lines(screen,BLACK,False, aresta, 1)
    
    def mostrarRED(self):
        for aresta in self.arestas:
            pygame.draw.lines(screen,RED,False, aresta, 1)
        
    


# Triângulo Médio
pontoA = [0, 0]
pontoB = [200, 0]
pontoC = [0, 200]

pontosTM = [pontoA, pontoB, pontoC]
arestasTM = [[pontoA, pontoB], [pontoB, pontoC], [pontoC, pontoA]]
trianguloMedio = objeto(pontosTM, arestasTM)


# Triângulo Pequeno 1
pontoD = [0, 200]
pontoE = [100, 300]
pontoF = [0, 400]

pontosTP1 = [pontoD, pontoE, pontoF]
arestasTP1 = [[pontoD, pontoE], [pontoE, pontoF], [pontoF, pontoD]]
trianguloP1 = objeto(pontosTP1, arestasTP1)


# Triângulo pequeno 2
pontoG = [100, 100]
pontoH = [300, 100]
pontoI = [200, 200]

pontosTP2 = [pontoG, pontoH, pontoI]
arestasTP2 = [[pontoG, pontoH], [pontoH, pontoI], [pontoI, pontoG]]
trianguloP2 = objeto(pontosTP2, arestasTP2)


# Quadrado
pontoJ = [0, 200]
pontoK = [100, 100]
pontoL = [200, 200]
pontoM = [100, 300]

pontosQ = [pontoJ, pontoK, pontoL, pontoM]
arestasQ = [[pontoJ, pontoK], [pontoK, pontoL], [pontoL, pontoM], [pontoM, pontoJ]]
quadrado = objeto(pontosQ, arestasQ)


# Losango
pontoO = [200, 0]
pontoP = [400, 0]
pontoQ = [300, 100]
pontoR = [100, 100]

pontosL = [pontoO, pontoP, pontoQ, pontoR]
arestasL = [[pontoO, pontoP], [pontoP, pontoQ], [pontoQ, pontoR], [pontoR, pontoO]]
losango = objeto(pontosL, arestasL)


# Triângulo grande 1
pontoS = [0, 400]
pontoT = [200, 200]
pontoU = [400, 400]

pontosTG1 = [pontoS, pontoT, pontoU]
arestasTG1 = [[pontoS, pontoT], [pontoT, pontoU], [pontoU, pontoS]]
trianguloG1 = objeto(pontosTG1, arestasTG1)


# Triângulo grande 2
pontoV = [400, 0]
pontoW = [400, 400]
pontoX = [200, 200]

pontosTG2 = [pontoV, pontoW, pontoX]
arestasTG2 = [[pontoV, pontoW], [pontoW, pontoX], [pontoX, pontoV]]
trianguloG2 = objeto(pontosTG2, arestasTG2)



screen.fill(WHITE)


while True:
    screen.fill(WHITE)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN and evento.key == K_0:
            for i in range (0, 10):
                screen.fill(WHITE)

                trianguloMedio.redimensionar(1.02)
                trianguloP1.redimensionar(1.02)
                trianguloP2.redimensionar(1.02)
                quadrado.redimensionar(1.02)
                losango.redimensionar(1.02)
                trianguloG1.redimensionar(1.02)
                trianguloG2.redimensionar(1.02)

                trianguloMedio.mostrar()
                trianguloP1.mostrar()
                trianguloP2.mostrar()
                quadrado.mostrar()
                losango.mostrar()
                trianguloG1.mostrar()
                trianguloG2.mostrar()

                time.sleep(0.02)
                pygame.display.update()
        if evento.type == KEYDOWN and evento.key == K_1: 
            for i in range (0, 10):
                screen.fill(WHITE)

                trianguloMedio.transladar(1, 1)
                trianguloP1.transladar(1, 1)
                trianguloP2.transladar(1, 1)
                quadrado.transladar(1, 1)
                losango.transladar(1, 1)
                trianguloG1.transladar(1, 1)
                trianguloG2.transladar(1, 1)

                trianguloMedio.mostrar()
                trianguloP1.mostrar()
                trianguloP2.mostrar()
                quadrado.mostrar()
                losango.mostrar()
                trianguloG1.mostrar()
                trianguloG2.mostrar()

                time.sleep(0.02)
                pygame.display.update()
        if evento.type == KEYDOWN and evento.key == K_2: 
            for i in range (0, 45):
                screen.fill(WHITE)

                trianguloMedio.rotacionar(1)
                trianguloP1.rotacionar(1)
                trianguloP2.rotacionar(1)
                quadrado.rotacionar(1)
                losango.rotacionar(1)
                trianguloG1.rotacionar(1)
                trianguloG2.rotacionar(1)

                trianguloMedio.mostrar()
                trianguloP1.mostrar()
                trianguloP2.mostrar()
                quadrado.mostrar()
                losango.mostrar()
                trianguloG1.mostrar()
                trianguloG2.mostrar()

                time.sleep(0.02)
                pygame.display.update()
        if evento.type == KEYDOWN and evento.key == K_3: 
            screen.fill(WHITE)

            trianguloMedio.refletir()
            trianguloP1.refletir()
            trianguloP2.refletir()
            quadrado.refletir()
            losango.refletir()
            trianguloG1.refletir()
            trianguloG2.refletir()

            trianguloMedio.mostrar()
            trianguloP1.mostrar()
            trianguloP2.mostrar()
            quadrado.mostrar()
            losango.mostrar()
            trianguloG1.mostrar()
            trianguloG2.mostrar()

            pygame.display.update()
        if evento.type == KEYDOWN and evento.key == K_4: 
                screen.fill(WHITE)
                
                trianguloMedio.cisalhar(2, 2)
                trianguloP1.cisalhar(2, 2)
                trianguloP2.cisalhar(2, 2)
                quadrado.cisalhar(2, 2)
                losango.cisalhar(2, 2)
                trianguloG1.cisalhar(2, 2)
                trianguloG2.cisalhar(2, 2)

                trianguloMedio.mostrar()
                trianguloP1.mostrar()
                trianguloP2.mostrar()
                quadrado.mostrar()
                losango.mostrar()
                trianguloG1.mostrar()
                trianguloG2.mostrar()

                pygame.display.update()    
            
    trianguloMedio.mostrar()
    trianguloP1.mostrar()
    trianguloP2.mostrar()
    quadrado.mostrar()
    losango.mostrar()
    trianguloG1.mostrar()
    trianguloG2.mostrar()

    pygame.display.update()

