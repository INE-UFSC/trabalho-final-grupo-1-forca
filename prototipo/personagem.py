import pygame
from abc import ABC, abstractmethod
from laser import Laser

class Personagem(ABC):
    RESFRIAMENTO = 20

    @abstractmethod
    def __init__(self, x: int, y: int, height: int, saude=100):
        self.__x = x
        self.__y = y
        self.__saude = saude
        self.__lasers = []
        self.__contador_resfriamento_laser = 0
        self.personagem_img = None
        self.laser_img = None
        self.height = height
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def saude(self):
        return self.__saude
    
    @property
    def lasers(self):
        return self.__lasers
    
    @property
    def contador_resfriamento_laser(self):
        return self.__contador_resfriamento_laser

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    @saude.setter
    def saude(self, saude: int):
        self.__saude = saude
    
    @contador_resfriamento_laser.setter
    def contador_resfriamento_laser(self, contador_resfriamento_laser):
        self.__contador_resfriamento_laser = contador_resfriamento_laser
    
    def desenhar(self, window):
        window.blit(self.personagem_img, (self.x, self.y))

        for laser in self.lasers:
            laser.desenhar(window)

    def mover_lasers(self, velocidade, objeto):
        self.resfriamento_laser()
        for laser in self.lasers:
            laser.movimentar(velocidade)

            if laser.fora_da_tela(self.height):
                self.lasers.remove(laser)
            elif laser.colisao(objeto):
                objeto.saude -= 10
                self.lasers.remove(laser)

    def resfriamento_laser(self):
        if self.contador_resfriamento_laser >= self.RESFRIAMENTO:
            self.contador_resfriamento_laser = 0
        elif self.contador_resfriamento_laser > 0:
            self.contador_resfriamento_laser += 1

    def atirar(self):
        if self.contador_resfriamento_laser == 0:
            laser = Laser(int(self.x + (self.personagem_img.get_width()/2) - (self.laser_img.get_width()/2)), int(self.y-10), self.laser_img)
            self.lasers.append(laser)
            self.contador_resfriamento_laser = 1

    def get_width(self):
        return self.personagem_img.get_width()
    
    def get_height(self):
        return self.personagem_img.get_height()