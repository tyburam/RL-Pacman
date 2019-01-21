import pygame

from game.consts import WHITE, BLACK, AGENT_NAMES


class Stats(pygame.sprite.Sprite):
    def __init__(self, x=410, y=10, agents=(0, 0, 0)):
        super(Stats, self).__init__()
        self.surf = pygame.Surface((200, 400))
        self.rect = self.surf.get_rect(left=x, top=y, width=200, height=200)

        # icons, names and agent types
        names = {'Player': 'frog.gif', 'Ghost 1': 'ghost.gif', 'Ghost 2': 'skeleton.gif'}
        chosen = {'Player': agents[0], 'Ghost 1': agents[1], 'Ghost 2': agents[2]}
        x = y = 0
        self.font = pygame.font.SysFont('Sans', 25)
        for name, filename in names.items():
            icon = pygame.image.load('./assets/' + filename).convert()
            self.surf.blit(icon, (x + 10, y + 10))

            # name text
            text = self.font.render(name, True, WHITE)
            self.surf.blit(text, (x + 30, y + 14))

            # agent type text
            text = self.font.render(AGENT_NAMES[chosen[name]], True, WHITE)
            self.surf.blit(text, (x + 30, y + 34))

            y += 50

    def update(self, points=0):
        text = self.font.render('Points: ' + str(points), True, WHITE)
        self.surf.blit(text, (30, 160))
