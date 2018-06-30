import gym
import numpy as np
from gym import spaces


class GridDrawBwEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.grid_size = 14
        self.action_space = spaces.Discrete(6)
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(2, self.grid_size, self.grid_size), dtype=np.float32)
        self.current_state = None
        self.done = None
        self.position = None

    def step(self, action):
        if self.done:
            raise RuntimeError("Episode has finished. Call env.reset() to start a new episode.")

        if action == 5:
            self.done = True
            return self.current_state, 0, True, None

        if action == 4:
            self.current_state[0][tuple(self.position)] += 15 * int(self.current_state[0][tuple(self.position)] < 255)
            self.current_state[0][tuple(self.position)] = min(self.current_state[0][tuple(self.position)], 255)
            return self.current_state, 0, False, None

        if action == 0:  # move up
            move = np.array([-1, 0])
        elif action == 1:  # move right
            move = np.array([0, 1])
        elif action == 2:  # move down
            move = np.array([1, 0])
        elif action == 3:  # move left
            move = np.array([0, -1])
        else:
            raise ValueError("Action not contained in Action Space. The action space is: " + self.action_space)

        self.current_state[1][tuple(self.position)] = 0

        self.position += move
        self.position = np.clip(self.position, 0, self.grid_size-1)

        self.current_state[1][tuple(self.position)] = 1

        return self.current_state, 0, False, None

    def reset(self):
        canvas = np.zeros((self.grid_size, self.grid_size))
        position_matrix = np.zeros((self.grid_size, self.grid_size))

        self.position = np.array([0, 0])

        position_matrix[tuple(self.position)] = 1

        self.current_state = np.stack([canvas, position_matrix])

        self.done = False
        return self.current_state

    def render(self, mode='human', close=False):
        return
