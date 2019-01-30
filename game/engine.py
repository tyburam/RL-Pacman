import pygame
from pygame.locals import *

from game.ball import Ball
from game.consts import BLACK, WHITE
from game.panel import Panel
from game.player import AgentPlayer
from game.stats import Stats
from game.wall import get_walls


def main_menu(screen):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    player_panel = Panel()
    ghost1_panel = Panel(200, 10, 'Ghost 1', 'ghost.gif')
    ghost2_panel = Panel(400, 10, 'Ghost 2', 'skeleton.gif')
    all_panels = pygame.sprite.Group()
    all_panels.add(player_panel)
    all_panels.add(ghost1_panel)
    all_panels.add(ghost2_panel)

    font = pygame.font.SysFont('Sans', 25)
    text = font.render('START', True, WHITE)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            # works until windows is closed or ESC is pressed
            running = not ((event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT)

        player_panel.check_click()
        ghost1_panel.check_click()
        ghost2_panel.check_click()

        clicked = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if clicked[0] == 1 and 400 >= mouse[1] >= 320:
            return player_panel.chosen, ghost1_panel.chosen, ghost2_panel.chosen

        screen.blit(background, (0, 0))
        for entity in all_panels:
            screen.blit(entity.surf, entity.rect)

        screen.blit(text, (250, 350))
        pygame.draw.rect(background, WHITE, [0, 320, 600, 80], 3)
        pygame.display.flip()
        clock.tick(10)

    return None


def main_loop(screen, chosen):
    if chosen is None:
        return

    font = pygame.font.SysFont('Sans', 60)
    text = font.render('GAME OVER', True, WHITE)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    main_player = AgentPlayer()
    ghost1 = AgentPlayer(160, 140, 'ghost.gif')
    ghost2 = AgentPlayer(200, 140, 'skeleton.gif')
    ghosts = pygame.sprite.Group()
    ghosts.add(ghost1)
    ghosts.add(ghost2)
    all_walls = get_walls()
    all_balls = Ball.get_balls()
    stats = Stats(agents=chosen)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(all_balls)
    all_sprites.add(all_walls)
    all_sprites.add(main_player)
    all_sprites.add(ghosts)
    all_sprites.add(stats)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            # works until windows is closed or ESC is pressed
            running = not ((event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT)
            if event.type == KEYDOWN and (event.key == K_RETURN or event.key == K_KP_ENTER):
                main_loop(screen, chosen)
                return

        main_player.update(all_walls, [])
        ghost1.update(all_walls, [])
        ghosts.update(all_walls, [])
        stats.update()

        screen.blit(background, (0, 0))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(main_player, ghosts):
            main_player.kill()
            screen.blit(text, (250, 350))

        pygame.display.flip()
        clock.tick(10)
