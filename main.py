import pygame
from pygame.locals import *
from sys import exit
from NPCs.Vesperianos.verdinhos import Verdinho
from NPCs.Protagonista.jax import Hero   # agora o Jax entra de novo

pygame.init()

# Configurações da tela
telargura = 975
telaltura = 675
tela = pygame.display.set_mode((telargura, telaltura))
pygame.display.set_caption("Estilhaços Vesperianos")
relogio = pygame.time.Clock()

# Carregar imagens
menu = pygame.image.load("Menu_-_Estilhaços_Vesperianos.png")
imagem_fundo1 = pygame.image.load("Cenario_1.png")

# Funções utilitárias
def desenharFundo(cenarios_de_fundo):
    fundo_escalado = pygame.transform.scale(cenarios_de_fundo, (telargura, telaltura))
    tela.blit(fundo_escalado, (0,0))

def textomenu(texto, tamanho, cor, x, y):
    fonte_objeto = pygame.font.SysFont("helvetica", tamanho, False, False)
    texto_imagem = fonte_objeto.render(texto, True, cor)
    texto_rect = texto_imagem.get_rect()
    texto_rect.midtop = (x, y)
    tela.blit(texto_imagem, texto_rect)

# Instâncias dos personagens
Jax = Hero(200, 500, "Jax", 100, 10, True, False)  
Berilima = Verdinho(400, 420, 100, 800)

# Estado inicial
estado_jogo = "Menu"

# Loop principal
while True:
    relogio.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if estado_jogo == "Menu":
            if event.type == KEYUP:
                estado_jogo = "Jogando"

        elif estado_jogo == "Jogando":
            if event.type == KEYDOWN:
                if event.key == K_k:
                    Jax.atira()
            if pygame.key.get_pressed()[K_j]:
                Jax.miralado()

    # Renderização
    if estado_jogo == "Menu":
        tela.fill((0,0,0))
        desenharFundo(menu)
        textomenu("JOGAR", 40, "white", 100, 499)

    elif estado_jogo == "Jogando":
        tela.fill((0,0,0))
        desenharFundo(imagem_fundo1)
        textomenu("O Jogo Começou!", 60, "yellow", telargura // 2, telaltura // 2)
        
        # Desenha os personagens
        Jax.desenho(tela)    
        Berilima.update()
        Berilima.spawnar(tela)

    pygame.display.update()
