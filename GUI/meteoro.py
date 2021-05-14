from objeto import Objeto
import pygame
import os


class Meteoro(Objeto):
    def __init__(self, x: int, y: int, height: int, width: int, objeto_img):
        super().__init__(x, y, height, width)
        self.__objeto_img = objeto_img
        self.__mascara = pygame.mask.from_surface(self.__objeto_img) #essa mascara pega o personagem_img e diz quais pixels ele está e nãoe stá ocupando, o que é necessário para a ser detectado a colisão

    @property
    def objeto_img(self):
        return self.__objeto_img

    @property
    def mascara(self):
        return self.__mascara

    def movimentar(self, velocidade, meteoros):
        self.y += velocidade 
        self.x += velocidade + 3
        if self.fora_da_tela():
            meteoros.remove(self)
