#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('RL-Pacman')
screen = pygame.display.set_mode((600, 600))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))  # black
screen.blit(background, (0, 0))

running = True

while running:
    for event in pygame.event.get():
        # works until windows is closed or ESC is pressed
        running = not ((event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT)

    pygame.display.flip()
