import numpy as np
from agents.agent import Agent


class QLearningAgent(Agent):
    def __init__(self, actions, epsilon=0.01, alpha=0.5, gamma=1):
        super(QLearningAgent, self).__init__(actions)
        self.Q = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def get_q(self, state, action):
        return self.Q.get((state, action), 0.0)

    def get_q_max(self, state):
        q = [self.get_q(state, a) for a in self.actions]
        max_q = max(q)
        return max_q, q.index(max_q)

    def act(self, obs):
        if np.random.random() < self.epsilon:
            return np.random.randint(0, self.num_actions)

        q_max = self.get_q_max(obs)
        return self.actions[q_max[1]]

    def feedback(self, state_before, state_after, action, reward):
        qnext = self.get_q_max(state_after)
        oldv = self.Q.get((state_before, action), 0.0)
        self.Q[(state_before, action)] = oldv + self.alpha * (reward + self.gamma * qnext - oldv)

