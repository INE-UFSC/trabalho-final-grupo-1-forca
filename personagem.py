from abc import ABC, abstractmethod
import pygame


class Personagem(ABC):
    RESFRIAMENTO = 20
    @abstractmethod
    def __init__(self, x: int, y: int, height: int, saude=100):
        self.__x = x
        self.__y = y
        self.__saude = saude
        self.personagem_img = None
        self.laser_img = None
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def saude(self):
        return self.__saude

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    @saude.setter
    def saude(self, saude: int):
        self.__saude = saude
    
    def desenhar(self, window):
        window.blit(self.personagem_img, (self.x, self.y))

    def atirar(self, laser):
        if self.contador_resfriamento_laser == 0:
            self.lasers.append(laser)
            self.contador_resfriamento_laser = 1
    
    def colisao(self, objeto):
        offset_x = int(objeto.x - self.x)
        offset_y = int(objeto.y - self.y)    
        return self.mascara.overlap(objeto.mascara, (offset_x, offset_y)) != None

    def get_width(self):
        return self.personagem_img.get_width()
    
    def get_height(self):
        return self.personagem_img.get_height()