import pygame

class Hero:
    def __init__(self, x, y, nome, vida_max, ataque, principal=True, virado=False):
        self.nome = nome
        self.vida_max = vida_max
        self.ataque = ataque
        self.vivo = True
        self.x = x
        self.y = y
        self.acao = 0 # parado é 0, andando é 1, mirando é 2, atirando é 3, se machucando é 4.
        self.vida = vida_max
        self.principal = principal
        self.virado = virado
        self.animalista = []
        self.framei = 0
        self.tempoanima = pygame.time.get_ticks()
        tempolista = []
    
        for i in range(3): # animação para ele parado.
            img = pygame.transform.scale_by(pygame.image.load(f"NPCs/Protagonista/{self.nome}/parado{i}.png"), 1.3)
            tempolista.append(img)
        self.animalista.append(tempolista)
        tempolista = []

        # NÃO TERMINADO (
        for i in range(3): # animação para ele andando.
            img = pygame.transform.scale_by((pygame.image.load(f"NPCs/Protagonista/{self.nome}/andando{i}.png")), 1.3)
            tempolista.append(img)
        self.animalista.append(tempolista)
        self.imagem = self.animalista[self.acao][self.framei]
        self.retangulo = pygame.Rect(self.x, self.y, self.imagem.get_width(), self.imagem.get_height())
        self.retangulo.center = (self.x, self.y)
        tempolista = []
        # ) NÃO TERMINADO

        for i in range(1): # animação para ele mirando lateralmente.
            img = pygame.transform.scale_by(pygame.image.load(f"NPCs/Protagonista/{self.nome}/mirandolateralmente{i}.png"), 1.3)
            tempolista.append(img)
        self.animalista.append(tempolista)
        self.imagem = self.animalista[self.acao][self.framei]
        for i in range(1): # animação para ele atirando lateralmente.
            img = pygame.transform.scale_by(pygame.image.load(f"NPCs/Protagonista/{self.nome}/atirandolateralmente{i}.png"), 1.3)
            tempolista.append(img)
        self.animalista.append(tempolista)
        self.imagem = self.animalista[self.acao][self.framei]

    def atualiza(self):
        esperanima = 700
        self.animalista[self.acao][self.framei]
        self.imagem = self.animalista[self.acao][self.framei]
        self.animalista[self.acao][self.framei]
        if pygame.time.get_ticks() - self.tempoanima > esperanima:
            self.tempoanima = pygame.time.get_ticks()
            self.framei += 1
        if self.framei >= len(self.animalista[self.acao]):
            self.framei = 0
    
    def para(self):
        self.acao = 0

    def anda(self):
        self.acao = 1

    def miralado(self):
        self.acao = 2
    
    def atira(self):
        self.acao = 3

    def desenho(self, tela):
        # Desenha o personagem:
        tela.blit(self.imagem, self.retangulo)