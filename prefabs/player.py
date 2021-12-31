from ursina import *
from lightning import *
from shaders.dissolve_shader import dissolve_shader


class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            model='cube',
            scale=Vec3(1, 2.3, 1),
            visible=True,
            shader=None,
            **kwargs
        )
        self.dead = False
        self.hp = 1
        self.max_hp = 1
        self.threshold = 1

    def hit(self, dmg):
        if self.dead:
            return
        self.hp -= dmg
        self.blink(
            color.red,
            duration=.3
        )
        if self.hp <= 0:
            self.hp = 0
            invoke(setattr, self, 'dead', True, delay=.3)
            self.collider = None
            destroy(self, delay=10)

    def update(self):
        if self.dead and self.shader != dissolve_shader:
            self.shader = dissolve_shader
            self.set_shader_input(
                'noiseTex',
                load_texture('../textures/dissolve.png'),
            )
            self.set_shader_input('threshold', self.threshold)
        if self.threshold > 0 and self.dead and self.shader == dissolve_shader:
            self.set_shader_input('threshold', self.threshold)
            self.threshold -= time.dt
