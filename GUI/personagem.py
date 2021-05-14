from abc import ABC, abstractmethod
import pygame


class Personagem(ABC):
    @abstractmethod
    def __init__(self, x: int, y: int, height: int, width: int, saude = 100):
        self.__x = x
        self.__y = y
        self.__height = height
        self.__width = width
        self.__saude = saude
        self.__personagem_img = None
        self.__laser_img = None
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

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
    
    def colisao(self, objeto, lista = None):
        offset_x = int(objeto.x - self.x)
        offset_y = int(objeto.y - self.y)    
        colisao = self.mascara.overlap(objeto.mascara, (offset_x, offset_y)) != None

        if colisao:
            lista.remove(self)
        return colisao
    
    def atirar(self, laser):
        if self.contador_resfriamento_laser == 0:
            self.lasers.append(laser)
            self.contador_resfriamento_laser = 1
            
    def get_width(self):
        return self.personagem_img.get_width()
    
    def get_height(self):
        return self.personagem_img.get_height()
    
    @property
    @abstractmethod
    def personagem_img(self):
        pass
    
    @property
    @abstractmethod
    def laser_img(self):
        pass

    @abstractmethod
    def movimentar(self):
        pass