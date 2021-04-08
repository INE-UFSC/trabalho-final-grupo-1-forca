import pygame
from pygame.locals import *
from prototipo_teste.objeto_teste import Objeto


class Player(pygame.sprite.Sprite, Objeto):
    def __init__(self, displaySurf):
        super().__init__()
        self.__largura_tela = displaySurf.get_width()
        self.__altura_tela = displaySurf.get_height()
        self.__tamanho_x = 50
        self.__tamanho_y = 90
        self.__posicao_x = self.__largura_tela / 2
        self.__posicao_y = self.__altura_tela / 1.2
        #self.image = pygame.image.load("Materials/Player.png")
        self.surf = pygame.Surface((50, 90))
        self.surf.fill("blueviolet")
        self.rect = self.surf.get_rect(center=(self.__posicao_x, self.__posicao_y))
        self.__velocidade = 5
        self.__vida = 0

    def mover(self):
        #print("right:", self.rect.right)
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -self.__velocidade)
        if self.rect.bottom < self.__altura_tela:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.__velocidade)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-self.__velocidade, 0)
        if self.rect.right < self.__largura_tela:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(self.__velocidade, 0)

    def desenhar(self, surface):
        surface.blit(self.surf, self.rect)
        #surface.blit(self.image, self.rect)

    def colisao(self):
        pass
