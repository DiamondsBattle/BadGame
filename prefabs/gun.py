from ursina import *


class Gun(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            model='cube',
            color=color.gray,
            texture='white_cube',
            **kwargs
        )
        self.dmg = 1

    def input(self, key):
        if key == 'left mouse down':
            self.shoot()

    def shoot(self):
        ray = raycast(
            direction=self.forward,
            origin=self,
        )
        if ray:
            try:
                ray.entity.hit(self.dmg)
            except AttributeError:
                pass
            except Exception as e:
                print(e)


class Bullet(Entity):
    def __init__(self):
        super().__init__(
            parent=self,
            model='cube',
            color=color.red,
            scale=.1,
            collider='box',
        )

    def update(self):
        if self.intersects():
            print('yeah')
            self.enabled = False
