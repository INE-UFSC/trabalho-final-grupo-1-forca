import pygame
from prototipo_teste.objeto_teste import Objeto


class Bullet(pygame.sprite.Sprite, Objeto):
    def __init__(self, x, y):
        super().__init__()
        self.__tamanho_x = 5
        self.__tamanho_y = 10
        self.__posicao_x = x
        self.__posicao_y = y - self.__tamanho_y
        self.surf = pygame.Surface((self.__tamanho_x, self.__tamanho_y))
        self.surf.fill("white")
        self.rect = self.surf.get_rect(center=(self.__posicao_x, self.__posicao_y))
        #self.rect.bottom = y
        #self.rect.centerx = x
        self.__velocidade = -10
        self.__vida = 0

    def mover(self):
        self.rect.y += self.__velocidade
        if self.rect.bottom < 0:
            self.kill()

    def desenhar(self, surface):
        surface.blit(self.surf, self.rect)

    def colisao(self):
        pass

