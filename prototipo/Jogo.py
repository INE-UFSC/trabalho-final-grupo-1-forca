import pygame
import time
import random

#iniciar pygame
pygame.init()

#tela
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()