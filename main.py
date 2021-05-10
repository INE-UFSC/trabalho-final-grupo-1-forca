import pygame
import random
import os

#importar
from jogador import Jogador
from inimigo import Inimigo
from meteoro import Meteoro

pygame.init()

#definindo altura e largura da janela do meu jogo
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WIDTH, HEIGHT = 650, 650
WH_JOGADOR = 80
WH_INIMIGO = 50

#carregando imagem do jogador
JOGADOR = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "jogador_se_movendo.png")), (WH_JOGADOR, WH_JOGADOR))

#definindo que minha janela tera a largura e altura especificada
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#nome que aparece na aba da janela
pygame.display.set_caption("Jogo Teste")

#carregando imagem do plano de funo
PLANO_DE_FUNDO = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "tela_jogo_princial.png")), (WIDTH, HEIGHT))

# Novo evento criado para aumentar a pontuação conforme passa o tempo
tempo = pygame.USEREVENT + 1
pygame.time.set_timer(tempo, 5000)

#cores
branco = (255,255,255)
preto = (0,0,0)


def colidir(objeto1, objeto2):
    offset_x = int(objeto2.x - objeto1.x)
    offset_y = int(objeto2.y - objeto1.y)

    return objeto1.mascara.overlap(objeto2.mascara, (offset_x, offset_y)) != None

class Main():

    def main(self):
        run = True
        FPS = 60
        nivel = 1
        vidas = 5
        fonte = pygame.font.Font(os.path.join(BASE_DIR, "assets", "levycrayola.TTF"), 50)
        fonte_fim_de_jogo = pygame.font.Font(os.path.join(BASE_DIR, "assets", "levycrayola.TTF"), 60)
        clock = pygame.time.Clock()
        parado = True

        # Pontuação para o próximo nível
        pontuacao_limite = 800

        # variáveis pro inimigo
        inimigos = []
        onda_de_inimigos = 5
        velocidade_inimigo = 2

        # variáveis pro meteoro
        meteoros = []
        #onda_de_meteoros = 2
        velocidade_meteoro = 1

        velocidade_laser = 7
        height_barra = 10
        saude = 100

        movimento_jogador = 8
        jogador = Jogador(int(WIDTH / 2 - JOGADOR.get_width() / 2), int(HEIGHT - 125), HEIGHT, saude)

        fim_de_jogo = False
        contador_fim_de_jogo = 0

        def desenhar_janela():
            WIN.blit(PLANO_DE_FUNDO, (0, 0))

            # mostrando textos na tela
            label_vidas = fonte.render(f"Vidas: {vidas}", True, preto)  # 1 - suavização de serrilhado
            label_nivel = fonte.render(f"Nivel: {nivel}", True, preto)
            label_pontuacao = fonte.render(f"{jogador.pontuacao}", True, preto)

            WIN.blit(label_vidas, (10, 10))
            WIN.blit(label_nivel, (WIDTH - label_nivel.get_width() - 10, 10))
            WIN.blit(label_pontuacao, (10, 595))

            for inimigo in inimigos:
                inimigo.desenhar(WIN)

            for meteoro in meteoros:
                meteoro.desenhar(WIN)

            jogador.desenhar(WIN, height_barra, parado)

            if fim_de_jogo:
                fim_de_jogo_label = fonte_fim_de_jogo.render("Aguarde", True, preto)
                WIN.blit(fim_de_jogo_label, (
                    WIDTH / 2 - fim_de_jogo_label.get_width() / 2, HEIGHT / 2 - fim_de_jogo_label.get_height() / 2))

            pygame.display.update()  # sempre que for desenhar, devemos atualizar a tela colocando a "nova imagem" por cima das outras que estavam desenhadas

        # quer dizer que o jogo vai executar a no máximo 60 quadros por segundo em qualquer máquina
        while run:
            clock.tick(FPS)
            desenhar_janela()

            if jogador.saude <= 0:
                if vidas >= 1:
                    jogador.saude = saude
                    vidas -= 1
                else:
                    fim_de_jogo = True
                    contador_fim_de_jogo += 1

            if vidas <= 0:
                fim_de_jogo = True
                contador_fim_de_jogo += 1

            # A pontuacao é retornada quando o jogador perde
            if fim_de_jogo:
                if contador_fim_de_jogo > FPS * 3:
                    return jogador.pontuacao
                else:
                    continue

            # Subida de nivel, Velocidade do Inimigo, do Laser e do Meteoro
            if jogador.pontuacao >= pontuacao_limite:
                if nivel < 3:
                    if nivel == 1:
                        velocidade_meteoro += 1
                        pontuacao_limite = 1800
                    if nivel == 2:
                        pontuacao_limite = 3000
                    velocidade_inimigo += 0.5
                    velocidade_laser += 0.5
                elif nivel == 3:
                    pontuacao_limite = 4000
                    velocidade_inimigo += 0.5
                    velocidade_laser += 0.5
                    velocidade_meteoro += 1
                elif nivel == 4:
                    pontuacao_limite = 5000
                    velocidade_inimigo += 0.5
                    velocidade_laser += 0.5
                elif nivel > 4:
                    pontuacao_limite += pontuacao_limite * 0.3
                    velocidade_inimigo += 1
                    velocidade_laser += 1
                    velocidade_meteoro += 1
                nivel += 1
                #print("vel inimigo:", velocidade_inimigo)

            # lógica do inimigo
            if len(inimigos) == 0:
                onda_de_inimigos += 5

                for i in range(onda_de_inimigos):
                    inimigo = Inimigo(random.randrange(50, WIDTH - 128), random.randrange(-8000 * (nivel / 5), -128),
                                      str(random.randrange(1, 4)), HEIGHT, saude)  # ver depois sobre o -1500
                    inimigos.append(inimigo)

            for inimigo in inimigos[:]:
                inimigo.movimentar(velocidade_inimigo)
                inimigo.mover_lasers(velocidade_laser, jogador)

                if random.randrange(0, 4 * FPS) == 1:
                    inimigo.atirar()

                if colidir(inimigo, jogador):
                    jogador.saude -= 10
                    inimigos.remove(inimigo)

                elif inimigo.y + inimigo.get_height() > HEIGHT:
                    inimigos.remove(inimigo)

            # lógica de criação, remoção e movimento dos meteoros
            if len(meteoros) == 0:
                meteoro = Meteoro(-110, random.randrange(0, 400), HEIGHT, WIDTH)
                meteoros.append(meteoro)
                if nivel > 1:
                    meteoro2 = Meteoro(-510, random.randrange(-300, 250), HEIGHT, WIDTH)
                    meteoros.append(meteoro2)
                if nivel > 2:
                    meteoro3 = Meteoro(-910, random.randrange(-600, -50), HEIGHT, WIDTH)
                    meteoros.append(meteoro3)
                if nivel > 3:
                    meteoro4 = Meteoro(-1310, random.randrange(-1100, -400), HEIGHT, WIDTH)
                    meteoros.append(meteoro4)
                if nivel > 4:
                    meteoro6 = Meteoro(-1710, random.randrange(-1150, -550), HEIGHT, WIDTH)
                    meteoros.append(meteoro6)
                if nivel > 5:
                    meteoro5 = Meteoro(-1110, random.randrange(-700, -150), HEIGHT, WIDTH)
                    meteoros.append(meteoro5)
                if nivel > 6:
                    meteoro7 = Meteoro(-710, random.randrange(-600, 0), HEIGHT, WIDTH)
                    meteoros.append(meteoro7)
                #print("m", len(meteoros))
                # print("nivel", nivel,"vel", velocidade_meteoro)

            for meteoro in meteoros[:]:
                meteoro.movimentar(velocidade_meteoro)

                if colidir(meteoro, jogador):
                    jogador.saude -= 15
                    meteoros.remove(meteoro)

                elif meteoro.y > HEIGHT or meteoro.x > WIDTH:
                    meteoros.remove(meteoro)

            # EVENTOS
            # vai passar por todos os eventos que ocorreram, 60 vezes por segundo
            for event in pygame.event.get():
                # se clicar no botão de fechar, o while se encerra, ou seja, o jogo fecha
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jogador.atirar()
                if event.type == tempo:
                    jogador.inc_pontuacao(10)

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if 624 > mouse[0] > 562 and 648 > mouse[1] > 543:
                    if click[0] == 1:
                        return jogador.pontuacao

            teclas = pygame.key.get_pressed()  # retorna um dicioonário de todas as teclas e diz se estão pressionadas ou não

            # movimentos do jogador de acordo com a tecla pressionada
            if teclas[pygame.K_a] and jogador.x - movimento_jogador > 0:  # esquerda
                jogador.x -= movimento_jogador
                parado = False
            elif teclas[pygame.K_d] and jogador.x + movimento_jogador + jogador.get_width() < WIDTH:  # direita
                jogador.x += movimento_jogador
                parado = False
            elif teclas[pygame.K_w] and jogador.y - movimento_jogador > 0:  # cima
                jogador.y -= movimento_jogador
                parado = False
            elif teclas[
                pygame.K_s] and jogador.y + movimento_jogador + jogador.get_height() + 2 * height_barra < HEIGHT:  # baixo
                jogador.y += movimento_jogador
                parado = False
            else:
                parado = True

            # Laser Jogador
            jogador.mover_lasers(-velocidade_laser, inimigos, meteoros)
