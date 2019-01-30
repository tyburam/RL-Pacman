import numpy as np
from agents.agent import Agent


class LinearFunctionApproximationQLearningAgent(Agent):
    def __init__(self, actions, epsilon=0.01, alpha=0.5, gamma=1):
        super(LinearFunctionApproximationQLearningAgent, self).__init__(actions)
        self.theta = np.zeros(64, dtype=np.float)
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def feature_extractor(self, state, action):
        action_index = np.zeros(self.num_actions, dtype=np.int)
        action_index[action] = 1
        return np.concatenate([action_index[i] * state for i in self.actions])

    def act(self, obs):
        if np.random.random() < self.epsilon:
            return np.random.randint(0, self.num_actions)

        q = [np.sum(self.theta.transpose() * self.feature_extractor(obs, a)) for a in self.actions]
        if q.count(max(q)) > 1:
            best = [i for i in range(len(self.actions)) if q[i] == max(q)]
            return self.actions[np.random.choice(best)]
        return self.actions[q.index(max(q))]


def feedback(self, state_before, state_after, action, reward):
    q = [np.sum(self.theta.transpose() * self.featureExtractor(state_after, a)) for a in self.actions]
    max_q_new = max(q)
    old_v = np.sum(self.theta.transpose() * self.featureExtractor(state_before, action))
    td_target = reward + self.gamma * max_q_new
    td_delta = td_target - old_v
    self.theta += self.alpha * td_delta * self.featureExtractor(state_before, action)
