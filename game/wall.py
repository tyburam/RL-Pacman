import pygame

from game.consts import WALLS, BLUE


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)

        self.surf = pygame.Surface([width, height])
        self.surf.fill(color)

        self.rect = self.surf.get_rect()
        self.rect.top = y
        self.rect.left = x


def get_walls():
    all_walls = pygame.sprite.RenderPlain()
    for item in WALLS:
        wall = Wall(item[0], item[1], item[2], item[3], BLUE)
        all_walls.add(wall)
    return all_walls
