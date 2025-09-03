import pygame


class Verdinho:
    def __init__(self, x, y, limite_esquerda, limite_direita):
        super().__init__()
        self.image = pygame.Surface(( 50, 70))
        
        #Testes de Gustavo
        #self.image = pygame.transform.scale_by(pygame.image.load("img/{self.nome}{i}.png"), 1.3)
        #self.retangulo = pygame.Rect(self.x, self.y, self.imagem.get_width(), self.imagem.get_height())
        #self.retangulo.center = (self.x, self.y)

        self.image.fill((0, 200, 0))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocidade = 2
        self.direcao = "direita"
        self.limite_esquerda = limite_esquerda
        self.limite_direita = limite_direita
    def update(self):
        if self.direcao == "direita":
            self.rect.x += self.velocidade
            if self.rect.right >= self.limite_direita:
                self.direcao = "esquerda"
        elif self.direcao == "esquerda":
            self.rect.x += self.velocidade
            if self.rect.left <= self.limite_esquerda:
                self.direcao = "direita"


    def spawnar(self, tela):
        tela.blit(self.image, self.rect)