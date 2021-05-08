import pygame
import os
from main import Main

pygame.init()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
largura = 650
altura = 650

pygame.display.set_caption('Caderno Invaders')
gameDisplay = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

black = (0, 0, 0)

tela_menu_principal = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_menu_principal.jpg")), (largura, altura))
tela_nome = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_nome.png")), (largura, altura))
tela_tutorial = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_tutorial.png")), (largura, altura))
tela_volume = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_volume.png")), (largura, altura))
tela_ranking = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_ranking.png")), (largura, altura))
tela_jogo_principal = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_jogo_princial.png")), (largura, altura))
tela_fim = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_fim.png")), (largura, altura))


def botao(x, x2, y, y2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    acabou = None

    if x2 > mouse[0] > x and y2 > mouse[1] > y:
        if click[0] == 1 and action != None:
            acabou = action()

    return acabou

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class Menu():
    def __init__(self):
        self.__largura = largura
        self.__altura = altura
        self.__crashou = False

    def menu_principal(self):
        while not self.__crashou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__crashou = False

            gameDisplay.blit(tela_menu_principal, (0, 0))

            botao(236, 417, 326, 363, self.menu_nome)
            botao(140, 419, 406, 444, self.menu_ranking)
            botao(243, 398, 489, 526, self.menu_volume)
            botao(267, 359, 566, 609, self.menu_sair)

            pygame.display.update()
            clock.tick(60)

    def menu_nome(self):
        text = ''
        while not self.__crashou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__crashou = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif len(text) <= 10:
                        text += event.unicode
                        

            gameDisplay.blit(tela_nome, (0, 0))
            
            font = pygame.font.Font(os.path.join(BASE_DIR, "assets", "levycrayola.ttf"), 75)
            textSurf, textRect = text_objects(text, font)
            textRect.center = (338, 388)
            gameDisplay.blit(textSurf, textRect)

            botao(256, 405, 580, 608, self.menu_tutorial)

            pygame.display.update()
            clock.tick(60)

    def menu_tutorial(self):

        while not self.__crashou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__crashou = False

            gameDisplay.blit(tela_tutorial, (0, 0))

            acabou = botao(230, 436, 572, 606, self.comecar_jogo)

            if acabou:
                self.tela_fim()

            pygame.display.update()
            clock.tick(60)

    def menu_ranking(self):

        while not self.__crashou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__crashou = False

            gameDisplay.blit(tela_ranking, (0, 0))

            botao(258, 381, 571, 607, self.menu_principal)

            pygame.display.update()
            clock.tick(60)

    def menu_volume(self):

        while not self.__crashou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__crashou = False

            gameDisplay.blit(tela_volume, (0, 0))

            #botões volume
            botao(137, 267, 410, 511, self.diminuir_volume)
            botao(403, 522, 410, 514, self.aumentar_volume)

            #botão voltar
            botao(265, 386, 568, 608, self.menu_principal)

            pygame.display.flip()
            clock.tick(60)

    def tela_fim(self):
        while not self.__crashou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__crashou = False

                print(event)

            gameDisplay.blit(tela_fim, (0, 0))

            botao(465, 634, 485, 642, self.menu_principal)

            pygame.display.flip()
            clock.tick(60)

        pass

    def diminuir_volume(self):
        pass

    def aumentar_volume(self):
        pass

    def comecar_jogo(self):
        jogo_comecado = Main()
        acabou = jogo_comecado.main()

        if acabou:
            self.tela_fim()

    def menu_sair(self):
        pygame.quit()
        quit()

#menu = Menu()
#menu.menu_principal()