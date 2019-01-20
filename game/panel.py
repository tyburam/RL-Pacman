import pygame

from game.consts import WHITE, BLACK


class Panel(pygame.sprite.Sprite):
    def __init__(self, x=10, y=10, name='Player', filename='frog.gif'):
        super(Panel, self).__init__()
        self.surf = pygame.Surface((200, 200))
        self.rect = self.surf.get_rect(left=x, top=y, width=200, height=200)
        self.chosen = 0

        # load icon
        icon = pygame.image.load('./assets/' + filename).convert()
        x = y = 0
        self.surf.blit(icon, (x + 10, y + 10))

        # put text near icon
        font = pygame.font.SysFont('Sans', 25)
        text = font.render(name, True, WHITE)
        self.surf.blit(text, (x + 30, y + 14))

        # agents (enum starts at 1)
        self.agent_names = ['RANDOM', 'GREEDY', 'ROUND_ROBIN', 'EPSILON_GREEDY', 'UCB', 'THOMPSON_BETA']
        cur_y = y + 52
        self.button1_x = x + 20
        self.button1_y = cur_y
        for ind, ag in enumerate(self.agent_names):
            pygame.draw.circle(self.surf, WHITE, [x + 20, cur_y], 5)
            if self.chosen == ind:
                pygame.draw.circle(self.surf, BLACK, [x + 20, cur_y], 3)
            text = font.render(ag, True, WHITE)
            self.surf.blit(text, (x + 30, cur_y - 8))
            cur_y += 20

    def check_click(self):
        clicked = pygame.mouse.get_pressed()
        if clicked[0] != 1:
            return

        mouse = pygame.mouse.get_pos()
        cur_y = self.button1_y
        new_chosen = -1
        for ind, ag in enumerate(self.agent_names):
            if self.button1_x + 150 > mouse[0] > self.button1_x and cur_y + 15 > mouse[1] > cur_y:
                new_chosen = ind
                break
            cur_y += 20

        if new_chosen >= 0 and new_chosen != self.chosen:
            pygame.draw.circle(self.surf, WHITE, [self.button1_x, self.button1_y + self.chosen * 20], 5)
            self.chosen = new_chosen
            pygame.draw.circle(self.surf, BLACK, [self.button1_x, self.button1_y + self.chosen * 20], 3)





