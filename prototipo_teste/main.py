import pygame
from pygame.locals import *
import sys
from prototipo_teste.enemy import Enemy
from prototipo_teste.player import Player
from prototipo_teste.bullet import Bullet
import time

# Initialize pyGame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Other variables for use in the program
screen_width = 400
screen_height = 600

# Setting display
displaySurf = pygame.display.set_mode((screen_width, screen_height))
displaySurf.fill("black")
pygame.display.set_caption("Game")

# Setting up sprites
E1 = Enemy(displaySurf)
P1 = Player(displaySurf)

# Creating Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 10000)

# Main loop
cont = 0
running = True
while running:
    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == inc_speed:
            E1.incremento_velocidade(2)

        if event.type == QUIT:
            running = False
            break

        if event.type == KEYDOWN:
            if event.key == pygame.K_z:
                B1 = Bullet(P1.rect.centerx, P1.rect.top)
                bullets.add(B1)
                all_sprites.add(B1)

    # Moves and redraw all sprites
    # Usando polimorfismo com os metodos desenhar() e mover()
    for entity in all_sprites:
        entity.desenhar(displaySurf)
        entity.mover()

    # Collision between enemies and bullets
    hits = pygame.sprite.spritecollide(E1, bullets, True)
    if hits:
        B1.kill()
        E1.shooted()

    # To be Run if collision occurs between Player and Enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        displaySurf.fill("red")
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        running = False
        break

    # Update
    pygame.display.update()

    # Draw/Render
    displaySurf.fill("black")

    # Keep loop running at the right speed
    FramePerSec.tick(FPS)

    # Contagem de quantos loops aconteceram
    cont += 1

print("Quantos loops aconteceram: ", cont)
pygame.quit()
sys.exit()
