import os

import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

YELLOW = (255,165,0)
PURPLE = (128,0,128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

CROWN = pygame.image.load("../images/crown.png")
CROWN = pygame.transform.scale(CROWN, (55, 55))

LAVA = pygame.image.load("../images/lava.png")
LAVA = pygame.transform.scale(LAVA, (800, 800))

ROCK = pygame.image.load("../images/rock2.jpg")
ROCK = pygame.transform.scale(ROCK, (100, 100))

PURPLE_PIC = pygame.image.load("../images/blue.png")
PURPLE_PIC = pygame.transform.scale(PURPLE_PIC, (85, 85))

YELLOW_PIC = pygame.image.load("../images/orange.png")
YELLOW_PIC = pygame.transform.scale(YELLOW_PIC, (85, 85))

