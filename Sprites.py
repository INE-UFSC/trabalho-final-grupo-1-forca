import pygame
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

WIDTH, HEIGHT = 650, 650
#fontes


#TELAS DO MENU
largura = WIDTH
altura = HEIGHT

tela_menu_principal = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_menu_principal_com_nome.jpg")), (largura, altura))
tela_nome = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_nome.png")), (largura, altura))
tela_tutorial = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_tutorial.png")), (largura, altura))
tela_volume = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_volume.png")), (largura, altura))
tela_ranking = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_ranking.png")), (largura, altura))
tela_jogo_principal = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_jogo_princial.png")), (largura, altura))
tela_fim = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_fim.png")), (largura, altura))

#TELAS MAIN
#carregando imagem do plano de funo
PLANO_DE_FUNDO = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_jogo_princial.png")), (WIDTH, HEIGHT))
#carregando explosão para o fim de jogo
EXPLOSAO = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "explosão.png")), (190,190))
#carregando porta de sair
PORTA = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "porta.png")), (82, 105))

# Barra Volume
imagem_volume = pygame.image.load(os.path.join(BASE_DIR, "assets", "barra_volume.png"))
barra_volume = [pygame.transform.scale(imagem_volume, (408, 30)),
                pygame.transform.scale(imagem_volume, (306, 30)),
                pygame.transform.scale(imagem_volume, (204, 30)),
                pygame.transform.scale(imagem_volume, (102, 30)),
                pygame.transform.scale(imagem_volume, (0, 0))
                ]
