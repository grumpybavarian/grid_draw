from gym.envs.registration import register

register(
    id='grid-draw-bw-v0',
    entry_point='grid_draw.envs:GridDrawBwEnv',
)

register(
    id='grid-draw-rgb-v0',
    entry_point='grid_draw.envs:GridDrawRgbEnv',
)