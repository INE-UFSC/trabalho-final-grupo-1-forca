import pygame
from personagem import Personagem

WH_JOGADOR = 80
WH_INIMIGO = 50

LASER_JOGADOR = pygame.image.load("../assets/laser_4.png")

#carregando imagem do jogador
JOGADOR = pygame.transform.scale(pygame.image.load("../assets/jogador.png"), (WH_JOGADOR, WH_JOGADOR))

class Jogador(Personagem):
    def __init__(self, x: int, y: int, height: int, saude = 100):
        super().__init__(x, y, height, saude)
        self.personagem_img = JOGADOR
        self.laser_img = LASER_JOGADOR
        self.__mascara = pygame.mask.from_surface(self.personagem_img) #essa mascara pega o personagem_img e diz quais pixels ele está e nãoe stá ocupando, o que é necessário para a ser detectado a colisão
        self.__max_saude = saude

    @property
    def mascara(self):
        return self.__mascara

    @property
    def max_saude(self):
        return self.__max_saude

    @mascara.setter
    def mascara(self, mascara):
        self.__mascara = mascara

    @max_saude.setter
    def max_saude(self, max_saude: int):
        self.__max_saude = max_saude
    
    def mover_lasers(self, velocidade, objetos, meteoros):
        self.resfriamento_laser()
        for laser in self.lasers:
            laser.movimentar(velocidade)

            if laser.fora_da_tela(self.height):
                self.lasers.remove(laser)
            else:
                for objeto in objetos:
                    if laser.colisao(objeto):
                        objetos.remove(objeto)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

                for meteoro in meteoros:
                    if laser.colisao(meteoro) and laser in self.lasers:
                        self.lasers.remove(laser)
                        
    
    def desenhar(self, window, height_barra):
        super().desenhar(window)
        self.barra_de_saude(window, height_barra)

    def barra_de_saude(self, window, height_barra):
        pygame.draw.rect(window, (248, 12, 58), (self.x, self.y + self.personagem_img.get_height() + height_barra, self.personagem_img.get_width(), height_barra))
        pygame.draw.rect(window, (29, 189, 106), (self.x, self.y + self.personagem_img.get_height() + height_barra, self.personagem_img.get_width() * (self.saude/self.max_saude), height_barra))
