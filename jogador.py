import pygame
import os
from personagem import Personagem
from arquivos.Som import *

pygame.mixer.init()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Largura e Altura do Jogador
WH_JOGADOR = 80

# Imagem Laser Jogador
LASER_JOGADOR = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_4.png"))

#carregando imagem do jogador
JOGADOR = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "jogador_se_movendo.png")), (WH_JOGADOR, WH_JOGADOR))
JOGADOR_PARADO = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "jogador_parado.png")), (WH_JOGADOR, WH_JOGADOR))


class Jogador(Personagem):
    def __init__(self, x: int, y: int, height: int, saude = 100):
        super().__init__(x, y, height, saude)
        self.personagem_img = JOGADOR
        self.personagem_parado_img = JOGADOR_PARADO
        self.laser_img = LASER_JOGADOR
        self.__mascara = pygame.mask.from_surface(self.personagem_img) #essa mascara pega o personagem_img e diz quais pixels ele está e nãoe stá ocupando, o que é necessário para a ser detectado a colisão
        self.__max_saude = saude
        self.__pontuacao = 0

    @property
    def mascara(self):
        return self.__mascara

    @property
    def max_saude(self):
        return self.__max_saude

    @property
    def pontuacao(self):
        return self.__pontuacao

    @mascara.setter
    def mascara(self, mascara):
        self.__mascara = mascara

    @max_saude.setter
    def max_saude(self, max_saude: int):
        self.__max_saude = max_saude

    def inc_pontuacao(self, inc_pontuacao):  #Incrementa a pontuação
        self.__pontuacao += inc_pontuacao                        
    
    def desenhar(self, window, height_barra, parado):
        if not parado:
            super().desenhar(window)
        else:
            window.blit(self.personagem_parado_img, (self.x, self.y))

        self.barra_de_saude(window, height_barra)

    def dano(self, pontos):
        self.saude -= pontos


    def barra_de_saude(self, window, height_barra):
        pygame.draw.rect(window, (248, 12, 58), (self.x, self.y + self.personagem_img.get_height() + height_barra, self.personagem_img.get_width(), height_barra))
        pygame.draw.rect(window, (29, 189, 106), (self.x, self.y + self.personagem_img.get_height() + height_barra, self.personagem_img.get_width() * (self.saude/self.max_saude), height_barra))
