#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from game.engine import main_menu, main_loop

pygame.init()
pygame.display.set_caption('RL-Pacman')
screen = pygame.display.set_mode((600, 406))

pygame.mouse.set_visible(True)
chosen = main_menu(screen)
pygame.mouse.set_visible(False)
main_loop(screen, chosen)
