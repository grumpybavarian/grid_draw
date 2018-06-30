from gym.envs.registration import register

register(
    id='GridDrawBw-v0',
    entry_point='grid_draw.envs:GridDrawBwEnv',
)

register(
    id='GridDrawRgb-v0',
    entry_point='grid_draw.envs:GridDrawRgbEnv',
)
