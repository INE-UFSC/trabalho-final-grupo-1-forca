from abc import ABC, abstractmethod
import pygame
import os
import time
import random
pygame.font.init()

#definindo altura e largura da janela do meu jogo
WIDTH, HEIGHT = 750, 750
WH_JOGADOR = 80
WH_INIMIGO = 50

#definindo que minha janela tera a largura e altura especificada
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#nome que aparece na aba da janela
pygame.display.set_caption("Jogo Teste")

#carregando imagem do jogador
JOGADOR = pygame.transform.scale(pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "jogador.png")), (WH_JOGADOR, WH_JOGADOR))

#carregando imagem dos aliens inimigos
ALIEN_1 = pygame.transform.scale(pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "alien_1.png")), (WH_INIMIGO, WH_INIMIGO))
ALIEN_2 = pygame.transform.scale(pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "alien_2.png")), (WH_INIMIGO, WH_INIMIGO))
ALIEN_3 = pygame.transform.scale(pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "alien_3.png")), (WH_INIMIGO, WH_INIMIGO))

#carregando imagem dos lasers
LASER_1 = pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "laser_1.png"))
LASER_2 = pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "laser_2.png"))
LASER_3 = pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "laser_3.png"))
LASER_4 = pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "laser_4.png"))

#carregando imagem do plano de funo
PLANO_DE_FUNDO = pygame.transform.scale(pygame.image.load(os.path.join("D:/Users/josed/Desktop/jogo_teste/assets", "plano_de_fundo.png")), (WIDTH, HEIGHT))

def colidir(objeto1, objeto2):
    offset_x = objeto2.x - objeto1.x
    offset_y = objeto2.y - objeto1.y
    
    return objeto1.mascara.overlap(objeto2.mascara, (offset_x, offset_y)) != None


class Laser():
    def __init__(self, x: int, y: int, laser_img):
        self.__x = x
        self.__y = y
        self.__laser_img = laser_img
        self.__mascara = pygame.mask.from_surface(self.laser_img)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def laser_img(self):
        return self.__laser_img
    
    @property
    def mascara(self):
        return self.__mascara

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def desenhar(self, window):
        window.blit(self.laser_img, (self.x, self.y))

    def movimentar(self, velocidade):
        self.y += velocidade
    
    def fora_da_tela(self, height):
        return not(self.y <= height and self.y >= 0)
    
    def colisao(self, objeto):
        return colidir(self, objeto)


class Personagem(ABC):
    RESFRIAMENTO = 20

    @abstractmethod
    def __init__(self, x: int, y: int, saude = 100):
        self.__x = x
        self.__y = y
        self.__saude = saude
        self.__lasers = []
        self.__contador_resfriamento_laser = 0
        self.personagem_img = None
        self.laser_img = None
    
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

            if laser.fora_da_tela(HEIGHT):
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


class Inimigo(Personagem):
    ID_MAP =    {
                    "1": (ALIEN_1, LASER_1),
                    "2": (ALIEN_2, LASER_2),
                    "3": (ALIEN_3, LASER_3)
                }

    def __init__(self, x: int, y: int, id, saude = 100):
        super().__init__(x, y, saude)
        self.personagem_img, self.laser_img = self.ID_MAP[id]
        self.__mascara = pygame.mask.from_surface(self.personagem_img) #essa mascara pega o personagem_img e diz quais pixels ele está e nãoe stá ocupando, o que é necessário para a ser detectado a colisão

    @property
    def mascara(self):
        return self.__mascara

    @mascara.setter
    def mascara(self, mascara):
        self.__mascara = mascara

    def movimentar(self, velocidade):
        self.y += velocidade
            

def main():
    run = True
    FPS = 60
    nivel = 0
    vidas = 5
    fonte = pygame.font.SysFont("comicsans", 50)
    fonte_fim_de_jogo = pygame.font.SysFont("comicsans", 60)
    clock = pygame.time.Clock()
    movimento_jogador = 8
    inimigos = []
    onda_de_inimigos = 5
    velocidade_inimigo = 2
    velocidade_laser = 7
    height_barra = 10
    saude = 100

    jogador = Jogador(int(WIDTH/2 - JOGADOR.get_width()/2), int(HEIGHT-125), saude)
    fim_de_jogo = False
    contador_fim_de_jogo = 0

    def desenhar_janela():
        WIN.blit(PLANO_DE_FUNDO, (0, 0))

        #mostrando textos na tela
        label_vidas = fonte.render(f"Vidas: {vidas}", 1, (255, 255, 255)) #1 - suavização de serrilhado
        label_nivel = fonte.render(f"Nível: {nivel}", 1, (255, 255, 255))

        WIN.blit(label_vidas, (10, 10))
        WIN.blit(label_nivel, (WIDTH - label_nivel.get_width() - 10, 10))

        for inimigo in inimigos:
            inimigo.desenhar(WIN)

        jogador.desenhar(WIN, height_barra)

        if fim_de_jogo:
            fim_de_jogo_label = fonte_fim_de_jogo.render("VOCÊ PERDEU!!!", 1, (255, 255, 255))
            WIN.blit(fim_de_jogo_label, (WIDTH/2 - fim_de_jogo_label.get_width()/2, HEIGHT/2 - fim_de_jogo_label.get_height()/2))

        pygame.display.update() #sempre que for desenhar, devemos atualizar a tela colocando a "nova imagem" por cima das outras que estavam desenhadas

    #quer dizer que o jogo vai executar a no máximo 60 quadros por segundo em qualquer máquina
    while run:
        clock.tick(FPS)
        desenhar_janela()
        
        if jogador.saude <= 0:
            if vidas >= 2:
                jogador.saude = saude
                vidas -= 1
            else:
                fim_de_jogo = True
                contador_fim_de_jogo += 1

        if vidas <= 0:
            fim_de_jogo = True
            contador_fim_de_jogo += 1
        
        if fim_de_jogo:
            if contador_fim_de_jogo > FPS * 3:
                run = False
            else:
                continue

        if len(inimigos) == 0:
            nivel += 1
            onda_de_inimigos += 5

            for i in range(onda_de_inimigos):
                inimigo = Inimigo(random.randrange(50, WIDTH-128), random.randrange(-10000*(nivel/5), -128), str(random.randrange(1, 4)), saude) #ver depois sobre o -1500
                inimigos.append(inimigo)
        

        #vai passar por todos os eventos que ocorreram, 60 vezes por segundo
        for event in pygame.event.get():
            #se clicar no botão de fechar, o while se encerra, ou seja, o jogo fecha
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                jogador.atirar()

        teclas = pygame.key.get_pressed() #retorna um dicioonário de todas as teclas e diz se estão pressionadas ou não

        #movimentos do jogador de acordo com a tecla pressionada
        if teclas[pygame.K_a] and jogador.x - movimento_jogador > 0: #esquerda
            jogador.x -= movimento_jogador
        if teclas[pygame.K_d] and jogador.x + movimento_jogador + jogador.get_width() < WIDTH: #direita
            jogador.x += movimento_jogador
        if teclas[pygame.K_w] and jogador.y - movimento_jogador > 0: #cima
            jogador.y -= movimento_jogador
        if teclas[pygame.K_s] and jogador.y + movimento_jogador + jogador.get_height() + 2*height_barra < HEIGHT: #baixo
            jogador.y += movimento_jogador
        

        for inimigo in inimigos[:]:
            inimigo.movimentar(velocidade_inimigo)
            inimigo.mover_lasers(velocidade_laser, jogador)

            if random.randrange(0, 4*FPS) == 1:
                inimigo.atirar()

            if colidir(inimigo, jogador):
                jogador.saude -= 10
                inimigos.remove(inimigo)

            elif inimigo.y + inimigo.get_height()  > HEIGHT:
                vidas -= 1
                inimigos.remove(inimigo)

        jogador.mover_lasers(-velocidade_laser, inimigos)

def main_menu():
    fonte_titulo = pygame.font.SysFont("comicsans", 60)
    run = True

    while run:
        WIN.blit(PLANO_DE_FUNDO, (0, 0))
        
        label_titulo = fonte_titulo.render("Pressione o mouse para começar...", 1, (255, 255, 255))
        WIN.blit(label_titulo, (WIDTH/2 - label_titulo.get_width()/2, HEIGHT/2 - label_titulo.get_height()/2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()