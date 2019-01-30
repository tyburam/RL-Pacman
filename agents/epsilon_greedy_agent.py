import numpy as np
from .agent import Agent


class EpsilonGreedyAgent(Agent):

    def __init__(self, actions, epsilon):
        self.total_rewards = np.zeros(len(actions), dtype=np.longdouble)
        self.total_counts = np.zeros(len(actions), dtype=np.longdouble)

        if epsilon is None or epsilon < 0 or epsilon > 1:
            raise ValueError("EpsilonGreedy: Invalid value of epsilon")
        self.epsilon = epsilon
        self.bound_eps = (self.epsilon == 0 or self.epsilon == 1)

        super(EpsilonGreedyAgent, self).__init__(actions)

    def act(self, obs):
        choice = self.epsilon if self.bound_eps else np.random.binomial(1, self.epsilon)

        if choice == 1:
            return np.random.choice(self.num_actions)

        current_averages = np.divide(self.total_rewards, self.total_counts,
                                     where=self.total_counts > 0)
        # Correctly handles Bernoulli rewards; over-estimates otherwise
        current_averages[self.total_counts <= 0] = 0.5
        return np.argmax(current_averages)

    def feedback(self, state_before, state_after, action, reward):
        self.total_rewards[action] += reward
        self.total_counts[action] += 1
