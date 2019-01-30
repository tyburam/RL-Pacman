import pygame

from agents.sarsa_agent import SarsaAgent
from game.consts import *
from agents.agent import AgentType
from agents.random_agent import RandomAgent
from agents.greedy_agent import GreedyAgent
from agents.round_robin_agent import RoundRobinAgent
from agents.epsilon_greedy_agent import EpsilonGreedyAgent
from agents.ucb_agent import UcbAgent
from agents.thompson_beta_agent import ThompsonBetaAgent


class AgentPlayer(pygame.sprite.Sprite):
    def __init__(self, x=10, y=10, filename='frog.gif', agent_type=AgentType.RANDOM):
        super(AgentPlayer, self).__init__()
        self.surf = pygame.image.load('./assets/'+filename).convert()
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.agent_type = agent_type
        self.action = -1

        if agent_type == AgentType.RANDOM:
            self.agent = RandomAgent(ALL_ACTIONS)
        elif agent_type == AgentType.GREEDY:
            self.agent = GreedyAgent(ALL_ACTIONS)
        elif agent_type == AgentType.ROUND_ROBIN:
            self.agent = RoundRobinAgent(ALL_ACTIONS)
        elif agent_type == AgentType.EPSILON_GREEDY:
            self.agent = EpsilonGreedyAgent(ALL_ACTIONS, 0.5)
        elif agent_type == AgentType.UCB:
            self.agent = UcbAgent(ALL_ACTIONS, 0.5)
        elif agent_type == AgentType.THOMPSON_BETA:
            self.agent = ThompsonBetaAgent(ALL_ACTIONS)
        elif agent_type == AgentType.SARSA:
            self.agent = SarsaAgent(ALL_ACTIONS)

    def update(self, walls, observation):
        self.action = self.agent.act(observation)

        old_x = self.rect.left
        old_y = self.rect.top

        if self.action == ACTION_LEFT:
            self.rect.move_ip(-5, 0)
        if self.action == ACTION_UP:
            self.rect.move_ip(0, -5)
        if self.action == ACTION_RIGHT:
            self.rect.move_ip(5, 0)
        if self.action == ACTION_DOWN:
            self.rect.move_ip(0, 5)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.left >= 380:
            self.rect.right = 370
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.top >= 380:
            self.rect.top = 370

        if pygame.sprite.spritecollideany(self, walls):
            self.rect.left = old_x
            self.rect.top = old_y

    def feedback(self, before, after, reward):
        self.agent.feedback(before, after, self.action, reward)
