import pygame
import os
from personagem import Personagem

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

WH_INIMIGO = 75

#carregando imagem dos aliens inimigos
ALIEN_1 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "inimigo_1.png")), (WH_INIMIGO, WH_INIMIGO))
ALIEN_2 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "inimigo_2.png")), (WH_INIMIGO, WH_INIMIGO))
ALIEN_3 = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "inimigo_3.png")), (WH_INIMIGO, WH_INIMIGO))

LASER_1 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_2 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_2.png"))
LASER_3 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_3.png"))


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