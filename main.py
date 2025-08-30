import pygame
from pygame.locals import *
from sys import exit

relogio = pygame.time.Clock()

cenario1 = pygame.image.load("Menu_-_Estilhaços_Vesperianos.png")

imagem_fundo1 = pygame.image.load("Menu_-_Estilhaços_Vesperianos.png")

lado = 0
alto = 0

def desenharFundo():
    tela.blit(imagem_fundo1, (0,0))

pygame.init()

telargura = 1024
telaltura = 1024

fontexto = pygame.font.SysFont("arial", 30, False, False)

tela = pygame.display.set_mode((telargura, telaltura))
pygame.display.set_caption("Estilhaços Vesperianos")

while True:
    relogio.tick(20)
    tela.fill((0,0,0))
    desenharFundo()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

