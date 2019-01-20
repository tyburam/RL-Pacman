import pygame
from pygame.locals import *
from game.consts import BLACK
from game.panel import Panel
from game.player import AgentPlayer
from game.wall import get_walls

main_menu_closing = False


def main_menu(screen):
    global main_menu_closing
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    player_panel = Panel()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            # works until windows is closed or ESC is pressed
            running = not ((event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT)

        player_panel.check_click()

        screen.blit(background, (0, 0))
        screen.blit(player_panel.surf, player_panel.rect)
        pygame.display.flip()
        clock.tick(10)

    main_menu_closing = True


def main_loop(screen):
    global main_menu_closing
    if main_menu_closing:
        return
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
