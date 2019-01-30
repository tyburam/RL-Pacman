import numpy as np
from agents.agent import Agent


class SarsaAgent(Agent):
    def __init__(self, actions, epsilon=0.01, alpha=0.5, gamma=1):
        super(SarsaAgent, self).__init__(actions)
        self.Q = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def get_q(self, state, action):
        return self.Q.get((state, action), 0.0)

    def act(self, obs):
        if np.random.random() < self.epsilon:
            return np.random.randint(0, self.num_actions)

        q = [self.get_q(obs, a) for a in self.actions]
        return self.actions[q.index(max(q))]

    def feedback(self, state_before, state_after, action, reward):
        qnext = self.get_q(state_after, action)
        oldv = self.Q.get((state_before, action), 0.0)
        self.Q[(state_before, action)] = oldv + self.alpha * (reward + self.gamma * qnext - oldv)

