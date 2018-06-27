from gym.envs.registration import register

register(
    id='grid-draw-v0',
    entry_point='grid_draw.envs:GridDrawEnv',
)