from objeto import Objeto
import pygame


class Laser(Objeto):   
    def __init__(self, x: int, y: int, height: int, width: int, objeto_img):
        super().__init__(x, y, height, width)
        self.__objeto_img = objeto_img
        self.__mascara = pygame.mask.from_surface(self.__objeto_img)
    
    @property
    def objeto_img(self):
        return self.__objeto_img
    
    @property
    def mascara(self):
        return self.__mascara
    
    def fora_da_tela(self):
        return not(self.y <= self.height and self.y + self.get_height() >= 0)