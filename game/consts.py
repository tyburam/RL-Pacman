ACTION_LEFT = 0
ACTION_UP = 1
ACTION_RIGHT = 2
ACTION_DOWN = 3
ALL_ACTIONS = [ACTION_LEFT, ACTION_UP, ACTION_RIGHT, ACTION_DOWN]

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# [x, y, width, height]
WALLS = [[0, 0, 6, 400],  # borders begin
         [0, 0, 400, 6],
         [0, 400, 406, 6],
         [400, 0, 6, 406],  # borders end
         [150, 100, 6, 90],  # ghost cage begin
         [150, 190, 106, 6],
         [250, 100, 6, 90],  # ghost cage end
         [50, 50, 80, 6],
         [250, 50, 80, 6],
         [50, 250, 100, 6],
         [100, 250, 6, 50],
         [250, 250, 100, 6],
         [300, 250, 6, 50],
         [200, 320, 6, 80]
         ]

# agents (enum starts at 1)
AGENT_NAMES = ['RANDOM', 'GREEDY', 'ROUND_ROBIN', 'EPSILON_GREEDY', 'UCB', 'THOMPSON_BETA']
