from .agent import Agent


class RoundRobinAgent(Agent):

    def __init__(self, actions):
        self.previous_action = None
        super(RoundRobinAgent, self).__init__(actions)

    def act(self, obs):
        if self.previous_action is None:
            self.previous_action = 0
            return 0

        current_action = self.previous_action + 1
        if current_action >= self.num_actions:
            current_action = 0
        self.previous_action = current_action
        return current_action
