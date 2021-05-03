import pygame
import random
from persistencia.rankingDAO import RankingDAO

#importar 
from jogador import Jogador
from inimigo import Inimigo
from meteoro import Meteoro

pygame.init()

#conexao com rankingDAO
ranking = RankingDAO()

#definindo altura e largura da janela do meu jogo
WIDTH, HEIGHT = 750, 750
WH_JOGADOR = 80
WH_INIMIGO = 50

#carregando imagem do jogador
JOGADOR = pygame.transform.scale(pygame.image.load("../assets/jogador.png"), (WH_JOGADOR, WH_JOGADOR))

#definindo que minha janela tera a largura e altura especificada
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#nome que aparece na aba da janela
pygame.display.set_caption("Jogo Teste")

#carregando imagem do plano de funo
PLANO_DE_FUNDO = pygame.transform.scale(pygame.image.load("../assets/plano_de_fundo.png"), (WIDTH, HEIGHT))

# Novo evento criado para aumentar a pontuação conforme passa o tempo
tempo = pygame.USEREVENT + 1
pygame.time.set_timer(tempo, 5000)

def colidir(objeto1, objeto2):
    offset_x = objeto2.x - objeto1.x
    offset_y = objeto2.y - objeto1.y
    
    return objeto1.mascara.overlap(objeto2.mascara, (offset_x, offset_y)) != None

def main(nome: str):
    run = True
    FPS = 60
    nivel = 0
    vidas = 1
    fonte = pygame.font.SysFont("comicsans", 50)
    fonte_fim_de_jogo = pygame.font.SysFont("comicsans", 60)
    clock = pygame.time.Clock()

    #variáveis pro inimigo
    inimigos = []
    onda_de_inimigos = 5
    velocidade_inimigo = 2

    #variáveis pro meteoro
    meteoros = []
    onda_de_meteoros = 2
    velocidade_meteoro = 1

    velocidade_laser = 7
    height_barra = 10
    saude = 30
    
    movimento_jogador = 8
    jogador = Jogador(int(WIDTH/2 - JOGADOR.get_width()/2), int(HEIGHT-125), HEIGHT, saude)

    
    fim_de_jogo = False
    contador_fim_de_jogo = 0

    def salvar_pontuacao():
        ranking.add(nome, jogador.pontuacao)
        print(ranking.get_all())

    def desenhar_janela():
        WIN.blit(PLANO_DE_FUNDO, (0, 0))

        #mostrando textos na tela
        label_vidas = fonte.render(f"Vidas: {vidas}", 1, (255, 255, 255)) #1 - suavização de serrilhado
        label_nivel = fonte.render(f"Nível: {nivel}", 1, (255, 255, 255))
        label_pontuacao = fonte.render(f"{jogador.pontuacao}", 1, (255, 255, 255))

        WIN.blit(label_vidas, (10, 10))
        WIN.blit(label_nivel, (WIDTH - label_nivel.get_width() - 10, 10))
        WIN.blit(label_pontuacao, ((WIDTH + label_pontuacao.get_width())/2, 10))

        for inimigo in inimigos:
            inimigo.desenhar(WIN)

        for meteoro in meteoros:
            meteoro.desenhar(WIN)
            
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
            if vidas >= 1:
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


        #lógica do inimigo
        if len(inimigos) == 0:
            nivel += 1
            onda_de_inimigos += 5

            for i in range(onda_de_inimigos):
                inimigo = Inimigo(random.randrange(50, WIDTH-128), random.randrange(-10000*(nivel/5), -128), str(random.randrange(1, 4)), HEIGHT, saude) #ver depois sobre o -1500
                inimigos.append(inimigo)

        for inimigo in inimigos[:]:
            inimigo.movimentar(velocidade_inimigo)
            inimigo.mover_lasers(velocidade_laser, jogador)

            if random.randrange(0, 4*FPS) == 1:
                inimigo.atirar()

            if colidir(inimigo, jogador):
                jogador.saude -= 10
                inimigos.remove(inimigo)

            elif inimigo.y + inimigo.get_height() > HEIGHT:
                inimigos.remove(inimigo)
        
        #lógica do meteoro
        if len(meteoros) == 0:
            onda_de_meteoros += 2
            onde = random.randrange(1,3)

            for i in range(onda_de_meteoros):
                if onde == 2:
                    meteoro = Meteoro(random.randrange(50, WIDTH-128), random.randrange(-10000*(nivel/5), -128), HEIGHT, WIDTH)
                else:
                    meteoro = Meteoro(random.randrange(-10000*(nivel/5), -128), random.randrange(0, WIDTH-128), HEIGHT, WIDTH)

                meteoros.append(meteoro)

        for meteoro in meteoros[:]:
            meteoro.movimentar(velocidade_meteoro)

            if colidir(meteoro, jogador):
                jogador.saude -= 15
                meteoros.remove(meteoro)
            
            elif meteoro.y + meteoro.get_height() > HEIGHT or meteoro.x + meteoro.get_width() > WIDTH:
                meteoros.remove(meteoro)

        # EVENTOS
        #vai passar por todos os eventos que ocorreram, 60 vezes por segundo
        for event in pygame.event.get():
            #se clicar no botão de fechar, o while se encerra, ou seja, o jogo fecha
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                jogador.atirar()
            if event.type == tempo:
                jogador.inc_pontuacao(10)

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
        
        # Laser Jogador
        jogador.mover_lasers(-velocidade_laser, inimigos, meteoros)

    salvar_pontuacao()

def main_menu():
    nome = input("Informe seu nome: ")
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
                main(nome)
    pygame.quit()



main_menu()
