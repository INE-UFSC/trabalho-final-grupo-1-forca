from personagem import Personagem
from Sprites import *
from Som import *
import pygame
import random
import os


pygame.mixer.init()


class Jogador(Personagem):
    def __init__(self, x: int, y: int, height: int, saude = 100):
        super().__init__(x, y, height, saude)
        self.personagem_img = JOGADOR
        self.personagem_parado_img = JOGADOR_PARADO
        self.laser_img = LASER_JOGADOR
        self.escudo_img = escudo_no_jogador
        self.escudo_img2 = escudo_no_jogador2
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

    def desenhar_escudo(self, window):
        r = random.randrange(0, 10)
        if r > 5:
            window.blit(self.escudo_img, (self.x - 10, self.y - 10))
        else:
            window.blit(self.escudo_img2, (self.x - 10, self.y - 10))

    def dano(self, pontos):
        self.saude -= pontos

    def barra_de_saude(self, window, height_barra):
        pygame.draw.rect(window, (248, 12, 58), (self.x, self.y + self.personagem_img.get_height() + height_barra, self.personagem_img.get_width(), height_barra))
        pygame.draw.rect(window, (29, 189, 106), (self.x, self.y + self.personagem_img.get_height() + height_barra, self.personagem_img.get_width() * (self.saude/self.max_saude), height_barra))