import pygame
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
pygame.mixer.init()

#carregando musica de fundo
MUSICA = pygame.mixer.music.load(os.path.join(BASE_DIR, "assets", "musica_de_fundo.ogg"))

#carregando musica fim de jogo
MUSICA_FIM = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets", "musica_fim_de_jogo.ogg"))

#carregando som de morte do jogador
MORTE = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets", "explosao_fim_de_jogo.ogg"))

#som colisao nave
COLIDIU = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets", "som_colisao.ogg"))
EXPLODIU = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets", "explodiu.ogg"))

#som da colisao laser
EXPLODIU = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets", "explodiu.ogg"))

