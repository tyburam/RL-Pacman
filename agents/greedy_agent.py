import numpy as np
from .agent import Agent


class GreedyAgent(Agent):

    def __init__(self, actions):
        self.total_rewards = np.zeros(len(actions), dtype=np.longdouble)
        self.total_counts = np.zeros(len(actions), dtype=np.longdouble)
        super(GreedyAgent, self).__init__(actions)

    def act(self, obs):
        current_averages = np.divide(self.total_rewards, self.total_counts,
                                     where=self.total_counts > 0)
        # Correctly handles Bernoulli rewards; over-estimates otherwise
        current_averages[self.total_counts <= 0] = 0.5
        return np.argmax(current_averages)

    def feedback(self, state_before, state_after, action, reward):
        self.total_rewards[action] += reward
        self.total_counts[action] += 1
