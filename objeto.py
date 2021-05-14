from abc import ABC, abstractmethod
import pygame


class Objeto(ABC):
    @abstractmethod
    def __init__(self, x: int, y: int, height: int, width: int):
        self.__x = x
        self.__y = y
        self.objeto_img = None
        self.height = height
        self.width = width
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def desenhar(self, window):
        window.blit(self.objeto_img, (self.x, self.y))

    def get_width(self):
        return self.objeto_img.get_width()
    
    def get_height(self):
        return self.objeto_img.get_height()
    
    def colisao(self, objeto, lista = None):
        offset_x = int(objeto.x - self.x)
        offset_y = int(objeto.y - self.y)
        
        return self.mascara.overlap(objeto.mascara, (offset_x, offset_y)) != None