import pygame
import random
from prototipo_teste.objeto_teste import Objeto


class Enemy(pygame.sprite.Sprite, Objeto):
    def __init__(self, displaySurf):
        super().__init__()
        self.__largura_tela = displaySurf.get_width()
        self.__altura_tela = displaySurf.get_height()
        self.__tamanho_x = 50
        self.__tamanho_y = 90
        self.__posicao_x = random.randint(30, self.__largura_tela - 50)
        self.__posicao_y = 0
        #self.image = pygame.image.load("Materials/Enemy.png")
        self.surf = pygame.Surface((self.__tamanho_x, self.__tamanho_y))
        self.surf.fill("red")
        self.rect = self.surf.get_rect(center=(self.__tamanho_x, self.__posicao_y))
        self.__velocidade = 2
        self.__vida = 3

    @property
    def velocidade(self):
        return self.__velocidade

    def incremento_velocidade(self, incremento):
        self.__velocidade += incremento

    def shooted(self):
        self.__vida -= 1
        if self.__vida == 0:
            self.__vida = 3
            self.rect.top = 0
            self.rect.center = (random.randint(30, 350), 0)
            print("kill")

    def mover(self):
        self.rect.move_ip(0, self.__velocidade)
        if self.rect.bottom > self.__altura_tela:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def desenhar(self, surface):
        surface.blit(self.surf, self.rect)
    #   surface.blit(self.image, self.rect)

    def colisao(self):
        pass
