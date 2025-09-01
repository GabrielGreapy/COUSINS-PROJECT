import pygame
from pygame.locals import *
from sys import exit

relogio = pygame.time.Clock()

menu = pygame.image.load("Menu_-_Estilhaços_Vesperianos.png")

imagem_fundo1 = pygame.image.load("Cenario_1.png")

lado = 0
alto = 0

def desenharFundo(cenarios_de_fundo):
    fundo_escalado = pygame.transform.scale(cenarios_de_fundo, (telargura, telaltura))
    tela.blit(fundo_escalado, (0,0))

def textomenu(texto, tamanho, cor, x, y):
    fonte_objeto = pygame.font.SysFont("arial", tamanho, False, False)
    texto_imagem = fonte_objeto.render(texto, True, cor)
    texto_rect = texto_imagem.get_rect()
    texto_rect.midtop = (x, y)
    tela.blit(texto_imagem, texto_rect)

pygame.init()

telargura = 975
telaltura = 675

tela = pygame.display.set_mode((telargura, telaltura))
pygame.display.set_caption("Estilhaços Vesperianos")

estado_jogo = "Menu"

while True:
    relogio.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if estado_jogo == "Menu":
        tela.fill((0,0,0))
        desenharFundo(menu)
        textomenu("Jogar", 40, "white", 100, 499)
        if event.type == KEYUP:
            estado_jogo = "Jogando"
    elif estado_jogo == "Jogando":
        # Quando o estado mudar, o código para desenhar o jogo em si virá aqui
        # Por enquanto, vamos apenas desenhar o fundo
        tela.fill((0,0,0))
        desenharFundo(imagem_fundo1)
        textomenu("O Jogo Começou!", 60, "yellow", telargura / 2, telaltura / 2)
    
    pygame.display.update()
