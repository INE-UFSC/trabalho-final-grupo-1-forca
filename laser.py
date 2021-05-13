import pygame
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#carregando imagem dos lasers
LASER_1 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_2 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_3 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))
LASER_4 = pygame.image.load(os.path.join(BASE_DIR, "assets", "laser_1.png"))

class Laser():
    RESFRIAMENTO = 20
    
    def __init__(self, x: int, y: int,  height: int, laser_img):
        self.__x = x
        self.__y = y
        self.__laser_img = laser_img
        self.__mascara = pygame.mask.from_surface(self.laser_img)
        self.__contador_resfriamento_laser = 0
        self.__height = height

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
    
    @property
    def contador_resfriamento_laser(self):
        return self.__contador_resfriamento_laser
    
    @property
    def height(self):
        return self.__height

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y
    
    @contador_resfriamento_laser.setter
    def contador_resfriamento_laser(self, contador_resfriamento_laser):
        self.__contador_resfriamento_laser = contador_resfriamento_laser    

    def desenhar(self, window):
        window.blit(self.laser_img, (self.x, self.y))

    def movimentar(self, velocidade):
        self.y += velocidade
    
    def fora_da_tela(self, height):
        return not(self.y <= height and self.y >= 0)
    
    def mover_lasers(self, velocidade, lasers):
        self.resfriamento_laser()
        self.movimentar(velocidade)
        if self.fora_da_tela(self.height):
            lasers.remove(self)
    
    def resfriamento_laser(self):
        if self.contador_resfriamento_laser >= self.RESFRIAMENTO:
            self.contador_resfriamento_laser = 0
        elif self.contador_resfriamento_laser > 0:
            self.contador_resfriamento_laser += 1

    def movimentar(self, velocidade):
        self.y += velocidade

    def colisao(self, objeto):
        offset_x = int(objeto.x - self.x)
        offset_y = int(objeto.y - self.y)
        
        return self.mascara.overlap(objeto.mascara, (offset_x, offset_y)) != None