from personagem import Personagem
from Sprites import *
import pygame
import os


class Inimigo(Personagem):
    ID_MAP =    {
                    "1": (ALIEN_1, LASER_1),
                    "2": (ALIEN_2, LASER_2),
                    "3": (ALIEN_3, LASER_3)
                }

    def __init__(self, x: int, y: int, id, height: int, saude = 100):
        super().__init__(x, y, height, saude)
        self.personagem_img, self.laser_img = self.ID_MAP[id]
        self.__mascara = pygame.mask.from_surface(self.personagem_img) #essa mascara pega o personagem_img e diz quais pixels ele está e nãoe stá ocupando, o que é necessário para a ser detectado a colisão

    @property
    def mascara(self):
        return self.__mascara

    @mascara.setter
    def mascara(self, mascara):
        self.__mascara = mascara

    def movimentar(self, velocidade):
        self.y += velocidade