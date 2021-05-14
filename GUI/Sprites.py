import pygame
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WIDTH, HEIGHT = 650, 650

#TELAS DO MENU
largura = int(WIDTH)
altura = int(HEIGHT)

tela_menu_principal = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_menu.jpeg")), (largura, altura))
tela_nome = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_nome.png")), (largura, altura))
tela_tutorial = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_tutorial.png")), (largura, altura))
tela_volume = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_volume.png")), (largura, altura))
tela_ranking = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_ranking.png")), (largura, altura))
tela_jogo_principal = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_jogo_princial.png")), (largura, altura))
tela_fim = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_fim.png")), (largura, altura))
opcoes_barra = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "opcoes_barra.png")), (61, 90))

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

#SPRITES INIMIGO
#Tamanho Inimigo
WH_INIMIGO = 75

ALIEN_1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "inimigo_1.png")), (WH_INIMIGO, WH_INIMIGO))
ALIEN_2 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "inimigo_2.png")), (WH_INIMIGO, WH_INIMIGO))
ALIEN_3 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "inimigo_3.png")), (WH_INIMIGO, WH_INIMIGO))

LASER_1 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_2 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_2.png"))
LASER_3 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_3.png"))

#SPRITES JOGADOR
# Largura e Altura do Jogador
WH_JOGADOR = 80

# Imagem Laser Jogador
LASER_JOGADOR = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_4.png"))

#carregando imagem do jogador
JOGADOR = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "jogador_se_movendo.png")), (WH_JOGADOR, WH_JOGADOR))
JOGADOR_PARADO = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "jogador_parado.png")), (WH_JOGADOR, WH_JOGADOR))
ESCUDO_NO_JOGADOR = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "escudo.png")), (WH_JOGADOR+20, WH_JOGADOR+20))
ESCUDO_NO_JOGADOR2 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "escudo2.png")), (WH_JOGADOR+20, WH_JOGADOR+20))


#LASER
#carregando imagem dos lasers
LASER_1 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_2 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_2.png"))
LASER_3 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_3.png"))
LASER_4 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))

#SPRITES BOOST
BOOST = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "boost_pontuacao.png")), (108, 90))

#SPRITES VIDA
VIDA = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "vida.png")), (30, 30))

#SPRITES METEORO
#carregando imagem dos meteoros
METEORO = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "meteoro_fogo.png")), (108, 90))

#SPRITES ESCUDO
ESCUDO = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "escudo.png")), (30, 30))
ESCUDO2 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "escudo2.png")), (30, 30))