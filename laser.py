from Sprites import *
import pygame
import os


class Laser():   
    def __init__(self, x: int, y: int,  height: int, laser_img):
        self.__x = x
        self.__y = y
        self.__laser_img = laser_img
        self.__mascara = pygame.mask.from_surface(self.laser_img)
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
    def height(self):
        return self.__height

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def desenhar(self, window):
        window.blit(self.laser_img, (self.x, self.y))
    
    def fora_da_tela(self):
        return not(self.y <= self.height and self.y + WH_INIMIGO >= 0)
    
    def mover_lasers(self, velocidade, lasers):
        self.movimentar(velocidade)
        if self.fora_da_tela():
            lasers.remove(self)

    def movimentar(self, velocidade):
        self.y += velocidade

    def colisao(self, objeto):
        offset_x = int(objeto.x - self.x)
        offset_y = int(objeto.y - self.y)
       
        return self.mascara.overlap(objeto.mascara, (offset_x, offset_y)) != None