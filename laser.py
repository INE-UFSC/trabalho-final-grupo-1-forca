import pygame
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#carregando imagem dos lasers
LASER_1 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_2 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_3 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_4 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))

def colidir(objeto1, objeto2):
    offset_x = objeto2.x - objeto1.x
    offset_y = objeto2.y - objeto1.y
    
    return objeto1.mascara.overlap(objeto2.mascara, (offset_x, offset_y)) != None
    
class Laser():
    def __init__(self, x: int, y: int, laser_img):
        self.__x = x
        self.__y = y
        self.__laser_img = laser_img
        self.__mascara = pygame.mask.from_surface(self.laser_img)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def laser_img(self):
        return self.__laser_img
    
    @property
    def mascara(self):
        return self.__mascara

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def desenhar(self, window):
        window.blit(self.laser_img, (self.x, self.y))

    def movimentar(self, velocidade):
        self.y += velocidade
    
    def fora_da_tela(self, height):
        return not(self.y <= height and self.y >= 0)
    
    def colisao(self, objeto):
        return colidir(self, objeto)
