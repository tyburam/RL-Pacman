#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from game.consts import *
from game.player import AgentPlayer
from game.wall import get_walls

pygame.init()
pygame.display.set_caption('RL-Pacman')
screen = pygame.display.set_mode((406, 406))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)

main_player = AgentPlayer()
ghost1 = AgentPlayer(160, 140)
ghost2 = AgentPlayer(200, 140)
ghosts = pygame.sprite.Group()
ghosts.add(ghost1)
ghosts.add(ghost2)
all_walls = get_walls()

all_sprites = pygame.sprite.Group()
all_sprites.add(all_walls)
all_sprites.add(main_player)
all_sprites.add(ghosts)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        # works until windows is closed or ESC is pressed
        running = not ((event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT)

    main_player.update(all_walls, [])
    ghost1.update(all_walls, [])
    ghosts.update(all_walls, [])

    screen.blit(background, (0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(main_player, ghosts):
        main_player.kill()

    pygame.display.flip()
    clock.tick(10)
