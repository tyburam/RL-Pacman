import numpy as np
import math
from .epsilon_greedy_agent import EpsilonGreedyAgent


class UcbAgent(EpsilonGreedyAgent):

    def __init__(self, actions, epsilon):
        self.round = 0
        self.times_played = np.zeros(len(actions), dtype=np.int)
        super(UcbAgent, self).__init__(actions, epsilon)

    def act(self, obs):
        self.round += 1
        current_action = self.round - 1

        # first try to explore all actions
        # than play using maximum average and exploration bonus
        if self.round > self.num_actions:
            current_averages = np.divide(self.total_rewards, self.total_counts,
                                         where=self.total_counts > 0)
            current_averages[self.total_counts <= 0] = 0.5

            log_val = 2 * math.log(self.round)
            bonus = np.sqrt(log_val / self.times_played)

            rewards = current_averages + bonus
            current_action = np.argmax(rewards)

        self.times_played[current_action] += 1
        return current_action
