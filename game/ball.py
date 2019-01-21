import pygame

from game.consts import WHITE


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, width=20, height=20):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(left=x, top=y, width=width, height=height)
        pygame.draw.circle(self.surf, WHITE, [5, 5], 3)

    @staticmethod
    def get_balls():
        all_balls = pygame.sprite.Group()
        for x in range(10, 390, 15):
            for y in range(10, 390, 15):
                # [50, 250, 100, 6],
                # [100, 250, 6, 50],
                # [250, 250, 100, 6],
                # [300, 250, 6, 50],
                if 55 <= y <= 60 or (145 <= x <= 250 and 100 <= y <= 190) or (50 <= x <= 150 and 250 <= y <= 255)\
                        or (250 <= x <= 350 and 250 <= y <= 255) or (x == 100 and 250 <= y <= 300)\
                        or (x == 295 and 250 <= y <= 300):
                    continue
                ball = Ball(x, y)
                all_balls.add(ball)
        return all_balls
