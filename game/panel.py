import pygame

from game.consts import WHITE, BLACK


class Panel(pygame.sprite.Sprite):
    def __init__(self, x=10, y=10, name="Player", filename='frog.gif'):
        super(Panel, self).__init__()
        self.surf = pygame.Surface([200, 200])
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.chosen = 0

        # load icon
        icon = pygame.image.load('./assets/' + filename).convert()
        self.surf.blit(icon, (x + 10, y + 10))

        # put text near icon
        font = pygame.font.SysFont('Sans', 25)
        text = font.render(name, True, WHITE)
        self.surf.blit(text, (x + 30, y + 14))

        # agents (enum starts at 1)
        agent_names = ['RANDOM', 'GREEDY', 'ROUND_ROBIN', 'EPSILON_GREEDY', 'UCB', 'THOMPSON_BETA']
        cur_y = y + 52
        for ind, ag in enumerate(agent_names):
            pygame.draw.circle(self.surf, WHITE, [x + 20, cur_y], 5)
            if self.chosen == ind:
                pygame.draw.circle(self.surf, BLACK, [x + 20, cur_y], 3)
            text = font.render(ag, True, WHITE)
            self.surf.blit(text, (x + 30, cur_y - 8))
            cur_y += 20




