import unittest
import gym
import grid_draw

class Environment(unittest.TestCase):

    def test_bw_env_make(self):
        gym.make("GridDrawBw-v0")

    def test_bw_env_reset(self):
        env = gym.make("GridDrawBw-v0")
        env.reset()

    def test_bw_env_step(self):
        env = gym.make("GridDrawBw-v0")
        env.reset()
        env.step(0)

    def test_rgb_env_make(self):
        gym.make("GridDrawBw-v0")

    def test_rgb_env_reset(self):
        env = gym.make("GridDrawBw-v0")
        env.reset()

    def test_rgb_env_step(self):
        env = gym.make("GridDrawBw-v0")
        env.reset()
        env.step(0)
