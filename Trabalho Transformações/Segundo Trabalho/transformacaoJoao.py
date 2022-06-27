import pygame, sys, math, time

from pygame.constants import KEYDOWN, K_SPACE

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
        

    def transladarX(self, x):
        for ponto in self.pontos:
            ponto[0] += x

        

    def transladarY(self, y):
        for ponto in self.pontos:
            ponto[1] += y
        

    def transladar(self, x, y):
        for ponto in self.pontos:
            ponto[0] += x
            ponto[1] += y
        
        
    def cisalharX(self, k):
        for ponto in self.pontos:
            ponto[0] += k * ponto[1]
        
    
    def cisalharY(self, k):
        for ponto in self.pontos:
            ponto[1] += k * ponto[0]
        
    
    def cisalhar(self, k):
        for ponto in self.pontos:
            ponto0 = ponto[0] + k * ponto[1]
            ponto1 = ponto[1] + k * ponto[0]
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
    

'''Meu Quadrado'''
pontoA = [0, 0]
pontoB = [0, 100]
pontoC = [100, 100]
pontoD = [100, 0]
pontos = [pontoA, pontoB, pontoC, pontoD]
arestas = [[pontoA, pontoB], [pontoB, pontoC], [pontoC, pontoD], [pontoD, pontoA]]
quadrado = objeto(pontos, arestas)

screen.fill(WHITE)


'''Quadrado do João'''
pontoJoaoA = [20, 20]
pontoJoaoB = [320, 20]
pontoJoaoC = [320, 320]
pontoJoaoD = [20, 320]
pontosJoao = [pontoJoaoA, pontoJoaoB, pontoJoaoC, pontoJoaoD]
arestasJoao = [[pontoJoaoA, pontoJoaoB], [pontoJoaoB, pontoJoaoC], [pontoJoaoC, pontoJoaoD], [pontoJoaoD, pontoJoaoA]]
quadradoJoao = objeto(pontosJoao, arestasJoao)



executando = True

while executando:
    screen.fill(WHITE)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN and evento.key == K_SPACE:
            for i in range (0, 1):
                screen.fill(WHITE)
                quadrado.redimensionar(3)
                quadrado.mostrar()
                quadradoJoao.mostrarRED()
                time.sleep(0.05)
                pygame.display.update()
            for i in range (0, 20):
                screen.fill(WHITE)
                quadrado.transladar(1, 1)
                quadrado.mostrar()
                quadradoJoao.mostrarRED()
                time.sleep(0.05)
                pygame.display.update()
            
    quadrado.mostrar()
    quadradoJoao.mostrarRED()

    pygame.display.update()


