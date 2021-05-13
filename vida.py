import pygame
import os
from objeto import Objeto

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

vida = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "vida.png")), (30, 30))

class Vida(Objeto):
    def __init__(self, x: int, y: int, height: int, width: int):
        super().__init__(x, y, height, width)
        self.objeto_img = vida
        self.__mascara = pygame.mask.from_surface(self.objeto_img) #essa mascara pega o personagem_img e diz quais pixels ele está e nãoe stá ocupando, o que é necessário para a ser detectado a colisão

    @property
    def mascara(self):
        return self.__mascara

    @mascara.setter
    def mascara(self, mascara):
        self.__mascara = mascara

    def movimentar(self, velocidade):
        self.y += velocidade
