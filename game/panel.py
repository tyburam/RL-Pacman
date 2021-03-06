import pygame

from game.consts import WHITE, BLACK, AGENT_NAMES


class Panel(pygame.sprite.Sprite):
    def __init__(self, x=10, y=10, name='Player', filename='frog.gif'):
        super(Panel, self).__init__()
        self.surf = pygame.Surface((200, 250))
        self.rect = self.surf.get_rect(left=x, top=y, width=200, height=250)
        self.chosen = 0
        self.btn1_abs_x = x + 10

        # load icon
        icon = pygame.image.load('./assets/' + filename).convert()
        x = y = 0
        self.surf.blit(icon, (x + 10, y + 10))

        # put text near icon
        font = pygame.font.SysFont('Sans', 25)
        text = font.render(name, True, WHITE)
        self.surf.blit(text, (x + 30, y + 14))

        cur_y = y + 52
        self.btn1_abs_y = self.btn1_rel_y = cur_y
        self.btn1_rel_x = x + 20
        for ind, ag in enumerate(AGENT_NAMES):
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
        cur_y = self.btn1_rel_y
        new_chosen = -1
        for ind, ag in enumerate(AGENT_NAMES):
            if self.btn1_abs_x + 150 >= mouse[0] >= self.btn1_abs_x and cur_y + 15 >= mouse[1] >= cur_y:
                new_chosen = ind
                break
            cur_y += 20

        if new_chosen >= 0 and new_chosen != self.chosen:
            pygame.draw.circle(self.surf, WHITE, [self.btn1_rel_x, self.btn1_rel_y + self.chosen * 20], 5)
            self.chosen = new_chosen
            pygame.draw.circle(self.surf, BLACK, [self.btn1_rel_x, self.btn1_rel_y + self.chosen * 20], 3)





