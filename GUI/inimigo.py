from personagem import Personagem
from Sprites import *
import pygame
import os


class Inimigo(Personagem):
    #lasers de cada inimigos
    ID_MAP ={
                "1": (ALIEN_1, LASER_1),
                "2": (ALIEN_2, LASER_2),
                "3": (ALIEN_3, LASER_3)
            }
            
    def __init__(self, x: int, y: int, id, height: int, width: int, saude: int):
        super().__init__(x, y, height, width, saude)
        self.__personagem_img, self.__laser_img = self.ID_MAP[id]
        self.__mascara = pygame.mask.from_surface(self.__personagem_img) #essa mascara pega o personagem_img e diz quais pixels ele está e nãoe stá ocupando, o que é necessário para a ser detectado a colisão

    @property
    def personagem_img(self):
        return self.__personagem_img

    @property
    def laser_img(self):
        return self.__laser_img

    @property
    def mascara(self):
        return self.__mascara

    def fora_da_tela(self):
        return ((self.y > self.height) or (self.x > self.width))

    def movimentar(self, velocidade, inimigos):
        self.y += velocidade
        if self.fora_da_tela():
            inimigos.remove(self)