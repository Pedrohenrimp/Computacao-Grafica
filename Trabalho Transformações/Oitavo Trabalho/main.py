import pygame, sys, math, time

from pygame.constants import KEYDOWN, K_0, K_1, K_2, K_3, K_4, K_SPACE

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

largura_tela = 1280
altura_tela = 720

screen = pygame.display.set_mode((largura_tela, altura_tela))

class ponto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def get2D(self):
        return [self.x, self.y]


class aresta:
    def __init__(self, pontoA, pontoB):
        self.pontoA = pontoA
        self.pontoB = pontoB

    def get2D(self):
        return [self.pontoA.get2D(), self.pontoB.get2D()]

class face:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas

class objeto:
    def __init__(self, vertices, arestas, faces):
        self.vertices = vertices
        self.arestas = arestas
        self.faces = faces

    def transladar(self, x, y, z):
        for vertice in self.vertices:
            vertice.x += x
            vertice.y += y
            vertice.z += z
    

    def centrarNaOrigem(self):
        maior_x = 0
        maior_y = 0
        menor_x = 9999
        menor_y = 9999
        for vertice in self.vertices:
            if vertice.x > maior_x:
                maior_x = vertice.x
            if vertice.y > maior_y:
                maior_y = vertice.y
            if vertice.x < menor_x:
                menor_x = vertice.x
            if vertice.y < menor_y:
                menor_y = vertice.y
        
        deslocamento_x = (maior_x - menor_x) / 2
        deslocamento_y = (maior_y - menor_y) / 2
        for vertice in self.vertices:
            vertice.x += -deslocamento_x
            vertice.y += -deslocamento_y

    def descentrarDaOrigem(self):
        maior_x = 0
        maior_y = 0
        menor_x = 9999
        menor_y = 9999
        for vertice in self.vertices:
            if vertice.x > maior_x:
                maior_x = vertice.x
            if vertice.y > maior_y:
                maior_y = vertice.y
            if vertice.x < menor_x:
                menor_x = vertice.x
            if vertice.y < menor_y:
                menor_y = vertice.y
        
        deslocamento_x = (maior_x - menor_x) / 2
        deslocamento_y = (maior_y - menor_y) / 2
        for vertice in self.vertices:
            vertice.x += deslocamento_x
            vertice.y += deslocamento_y


    def girarX(self, graus):
        self.centrarNaOrigem()
        rad = 2 * math.pi * graus/360
        cos = math.cos(rad)
        sen = math.sin(rad)
        for vertice in self.vertices:
            verticeZ = vertice.z * cos - vertice.y * sen
            verticeY = vertice.z * sen + vertice.y * cos
            vertice.z = verticeZ
            vertice.y = verticeY
        self.descentrarDaOrigem()

    def girarY(self, graus):
        self.centrarNaOrigem()
        rad = 2 * math.pi * graus/360
        cos = math.cos(rad)
        sen = math.sin(rad)
        for vertice in self.vertices:
            verticeX = vertice.x * cos - vertice.z * sen
            verticeZ = vertice.x * sen + vertice.z * cos
            vertice.x = verticeX
            vertice.z = verticeZ
        self.descentrarDaOrigem()

    def girarZ(self, graus):
        self.centrarNaOrigem()
        rad = 2 * math.pi * graus/360
        cos = math.cos(rad)
        sen = math.sin(rad)
        for vertice in self.vertices:
            verticeX = vertice.x * cos - vertice.y * sen
            verticeY = vertice.x * sen + vertice.y * cos
            vertice.x = verticeX
            vertice.y = verticeY
        self.descentrarDaOrigem()


    def mostrarIsometrico(self):
        obj = self
        obj.girarY(45)
        obj.girarX(35.26)
        for aresta in obj.arestas:
            pygame.draw.lines(screen,BLACK,False, aresta.get2D(), 1)
        obj.girarX(-35.26)
        obj.girarY(-45)
    
    def mostrarIsometricoCentralizado(self):
        obj = self
        obj.girarY(45)
        obj.girarX(35.26)
        obj.transladar(590, 260, 0)
        for aresta in obj.arestas:
            pygame.draw.lines(screen,BLACK,False, aresta.get2D(), 1)
        obj.transladar(-590, -260, 0)
        obj.girarX(-35.26)
        obj.girarY(-45)
    
    def mostrarFacesPrincipaisIsometricoCentralizado(self):
        obj = self
        obj.girarY(45)
        obj.girarX(35.26)
        obj.transladar(590, 260, 0)
        
        # Desenha face posterior
        for aresta in obj.faces[1].arestas:
            pygame.draw.lines(screen,BLACK,False, aresta.get2D(), 1)
        
        # Desenha face lateral direita
        for aresta in obj.faces[3].arestas:
            pygame.draw.lines(screen,BLACK,False, aresta.get2D(), 1)

        # Desenha face superior
        for aresta in obj.faces[4].arestas:
            pygame.draw.lines(screen,BLACK,False, aresta.get2D(), 1)
        obj.transladar(-590, -260, 0)
        obj.girarX(-35.26)
        obj.girarY(-45)

    def mostrarFacesPrincipais(self, pontoObservador):
        obj = self
        facesVisiveis = []
        for face in obj.faces:
            pontoMedioFace = self.getCentroFace(face)
            vetorObservador = [pontoObservador.x - pontoMedioFace.x, pontoObservador.y - pontoMedioFace.y, pontoObservador.z - pontoMedioFace.z]
            vetorAB = [face.vertices[0].x - face.vertices[1].x, face.vertices[0].y - face.vertices[1].y, face.vertices[0].z - face.vertices[1].z]
            vetorAC = [face.vertices[0].x - face.vertices[2].x, face.vertices[0].y - face.vertices[2].y, face.vertices[0].z - face.vertices[2].z]
            vetorNormal = [vetorAB[1]*vetorAC[2] - vetorAC[1]*vetorAB[2], vetorAB[2]*vetorAC[0] - vetorAC[2]*vetorAB[0], vetorAB[0]*vetorAC[1] - vetorAC[0]*vetorAB[1]]
            produtoEscalar = vetorObservador[0]*vetorNormal[0] + vetorObservador[1]*vetorNormal[1] + vetorObservador[2]*vetorNormal[2]
            if produtoEscalar > 0:
                facesVisiveis.append(face)
        

        obj.girarY(45)
        obj.girarX(35.26)
        obj.transladar(590, 260, 0)

        for face in facesVisiveis:
            for aresta in face.arestas:
                pygame.draw.lines(screen,BLACK,False, aresta.get2D(), 1)
        obj.transladar(-590, -260, 0)
        obj.girarX(-35.26)
        obj.girarY(-45)


    def mostrar2D(self):
        for aresta in self.arestas:
                pygame.draw.lines(screen,BLACK,False, aresta.get2D(), 1)

    def getCentro(self):
        somaX = 0
        somaY = 0
        somaZ = 0
        quantidadePontos = len(self.vertices)
        for p in self.vertices:
            somaX += p.x
            somaY += p.y
            somaZ += p.z
        return ponto(somaX / quantidadePontos, somaY / quantidadePontos, somaZ / quantidadePontos)

    def getCentroFace(self, face):
        somaX = 0
        somaY = 0
        somaZ = 0
        quantidadePontos = len(face.vertices)
        for p in face.vertices:
            somaX += p.x
            somaY += p.y
            somaZ += p.z
        return ponto(somaX / quantidadePontos, somaY / quantidadePontos, somaZ / quantidadePontos)
    
    def mostrarFacesPrincipaisComShading(self, luzDirecional, IndiceluzAmbiente):
        obj = self
        facesVisiveis = []
        for face in obj.faces:
            pontoMedioFace = self.getCentroFace(face)
            vetorLuzDirecional = [luzDirecional.x - pontoMedioFace.x, luzDirecional.y - pontoMedioFace.y, luzDirecional.z - pontoMedioFace.z]
            vetorAB = [face.vertices[0].x - face.vertices[1].x, face.vertices[0].y - face.vertices[1].y, face.vertices[0].z - face.vertices[1].z]
            vetorAC = [face.vertices[0].x - face.vertices[2].x, face.vertices[0].y - face.vertices[2].y, face.vertices[0].z - face.vertices[2].z]
            vetorNormal = [vetorAB[1]*vetorAC[2] - vetorAC[1]*vetorAB[2], vetorAB[2]*vetorAC[0] - vetorAC[2]*vetorAB[0], vetorAB[0]*vetorAC[1] - vetorAC[0]*vetorAB[1]]
            produtoEscalar = vetorLuzDirecional[0]*vetorNormal[0] + vetorLuzDirecional[1]*vetorNormal[1] + vetorLuzDirecional[2]*vetorNormal[2]
            if produtoEscalar > 0:
                moduloVetorLuzDirecional = math.sqrt(pow(vetorLuzDirecional[0], 2) + pow(vetorLuzDirecional[1], 2) + pow(vetorLuzDirecional[2], 2))
                moduloVetorNormal = math.sqrt(pow(vetorNormal[0], 2) + pow(vetorNormal[1], 2) + pow(vetorNormal[2], 2))
                cosseno = produtoEscalar / (moduloVetorLuzDirecional * moduloVetorNormal)
                facesVisiveis.append([face, cosseno])

        obj.girarY(45)
        obj.girarX(35.26)
        obj.transladar(590, 260, 0)

        for face in facesVisiveis:
            listaPontos2D = []
            for ponto in face[0].vertices:
                listaPontos2D.append(ponto.get2D())
            pygame.draw.polygon(screen, (0, 0, 255 * face[1] * IndiceluzAmbiente), listaPontos2D)
        obj.transladar(-590, -260, 0)
        obj.girarX(-35.26)
        obj.girarY(-45)
                
    

        

    


'''----------   Cubo   ----------'''

#Vértices Frontais
pontoA = ponto(0, 0, 0)
pontoB = ponto(0, 100, 0)
pontoC = ponto(100, 100, 0)
pontoD = ponto(100, 0, 0)

#Vértices Posteriores
pontoW = ponto(0, 0, 100)
pontoX = ponto(0, 100, 100)
pontoY = ponto(100, 100, 100)
pontoZ = ponto(100, 0, 100)

# Arestas Frontais
arestaAB = aresta(pontoA, pontoB)
arestaBC = aresta(pontoB, pontoC)
arestaCD = aresta(pontoC, pontoD)
arestaDA = aresta(pontoD, pontoA)

# Arestas Posteriores
arestaWX = aresta(pontoW, pontoX)
arestaXY = aresta(pontoX, pontoY)
arestaYZ = aresta(pontoY, pontoZ)
arestaZW = aresta(pontoZ, pontoW)

# Arestas Laterais Esquerdas
arestaAW = aresta(pontoA, pontoW)
arestaBX = aresta(pontoB, pontoX)

# Arestas Laterais Direitas
arestaCY = aresta(pontoC, pontoY)
arestaDZ = aresta(pontoD, pontoZ)

# Face Frontal
faceABCD = face([pontoA, pontoB, pontoC, pontoD], [arestaAB, arestaBC, arestaCD, arestaDA])

# Face Posterior
faceWXYZ = face([pontoZ, pontoY, pontoX, pontoW], [arestaWX, arestaXY, arestaYZ, arestaZW])

# Face Lateral Esquerda
faceABWX = face([pontoW, pontoX, pontoB, pontoA], [arestaAB, arestaWX, arestaAW, arestaBX])

# Face Lateral Direita
faceCDYZ = face([pontoD, pontoC, pontoY, pontoZ], [arestaCD, arestaYZ, arestaCY, arestaDZ])

# Face Superior
faceADWZ = face([pontoW, pontoA, pontoD, pontoZ], [arestaDA, arestaZW, arestaAW, arestaDZ])

# Face Inferior
faceBCXY = face([pontoB, pontoX, pontoY, pontoC], [arestaBC, arestaXY, arestaBX, arestaCY])

# Parâmetros do objeto Cubo
vertices = [pontoA, pontoB, pontoC, pontoD, pontoW, pontoX, pontoY, pontoZ]
arestas = [arestaAB, arestaBC, arestaCD, arestaDA, arestaWX, arestaXY, arestaYZ, arestaZW, arestaAW, arestaBX, arestaCY, arestaDZ]
faces = [faceABCD, faceWXYZ, faceABWX, faceCDYZ, faceADWZ, faceBCXY]

cubo = objeto(vertices, arestas, faces)


luzDir = ponto(300, -200, 300)
pontosLuzDir = [ponto(luzDir.x - 5, luzDir.y - 5, luzDir.z), ponto(luzDir.x + 5, luzDir.y - 5, luzDir.z), ponto(luzDir.x - 5, luzDir.y + 5, luzDir.z), ponto(luzDir.x + 5, luzDir.y + 5, luzDir.z)]
arestasLuzDir = [aresta(pontosLuzDir[0], pontosLuzDir[1]), aresta(pontosLuzDir[0], pontosLuzDir[2]), aresta(pontosLuzDir[2], pontosLuzDir[3]), aresta(pontosLuzDir[1], pontosLuzDir[3])]
objetoLuzDir = objeto(pontosLuzDir, arestasLuzDir, [])

indiceLuzAmbiente = 0.8

screen.fill(WHITE)


while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN and evento.key == K_0:
            screen.fill(WHITE)
            cubo.mostrarIsometrico()
            
        if evento.type == KEYDOWN and evento.key == K_1:
            screen.fill(WHITE)
            cubo.mostrarIsometricoCentralizado()
        if evento.type == KEYDOWN and evento.key == K_2:
            screen.fill(WHITE)
            cubo.mostrarFacesPrincipaisIsometricoCentralizado()
        if evento.type == KEYDOWN and evento.key == K_3:
            screen.fill(WHITE)
            cubo.mostrarFacesPrincipaisComShading(luzDir, indiceLuzAmbiente)
            cubo.transladar(10, 500, 0)
            cubo.mostrar2D()
            objetoLuzDir.transladar(10, 500, 0)
            objetoLuzDir.mostrar2D()
            pygame.draw.lines(screen, RED, False, [cubo.getCentro().get2D(), objetoLuzDir.getCentro().get2D()], 1)


            
    pygame.display.update()

