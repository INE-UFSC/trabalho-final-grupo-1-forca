from personagem import Personagem
import pygame

#definindo altura e largura da janela do meu jogo
WIDTH, HEIGHT = 750, 750
WH_JOGADOR = 80
WH_INIMIGO = 50

#carregando imagem dos lasers
LASER_1 = pygame.image.load("../assets/laser_1.png")
LASER_2 = pygame.image.load("../assets/laser_2.png")
LASER_3 = pygame.image.load("../assets/laser_3.png")
LASER_4 = pygame.image.load("../assets/laser_4.png")

#carregando imagem do jogador
JOGADOR = pygame.transform.scale(pygame.image.load("../assets/jogador.png"), (WH_JOGADOR, WH_JOGADOR))

class Jogador(Personagem):
    def __init__(self, x: int, y: int, saude = 100):
        super().__init__(x, y, saude)
        self.personagem_img = JOGADOR
        self.laser_img = LASER_4
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
    
    def mover_lasers(self, velocidade, objetos):
        self.resfriamento_laser()
        for laser in self.lasers:
            laser.movimentar(velocidade)

            if laser.fora_da_tela(HEIGHT):
                self.lasers.remove(laser)
            else:
                for objeto in objetos:
                    if laser.colisao(objeto):
                        objetos.remove(objeto)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
    
    def desenhar(self, window, height_barra):
        super().desenhar(window)
        self.barra_de_saude(window, height_barra)

    def barra_de_saude(self, window, height_barra):
        pygame.draw.rect(window, (248, 12, 58), (self.x, self.y + self.personagem_img.get_height() + height_barra, self.personagem_img.get_width(), height_barra))
        pygame.draw.rect(window, (29, 189, 106), (self.x, self.y + self.personagem_img.get_height() + height_barra, self.personagem_img.get_width() * (self.saude/self.max_saude), height_barra))
