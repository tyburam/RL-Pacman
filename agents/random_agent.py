import numpy as np
from .agent import Agent


class RandomAgent(Agent):

    def __init__(self, actions):
        super(RandomAgent, self).__init__(actions)

    def act(self, obs):
        return np.random.randint(0, self.num_actions)
