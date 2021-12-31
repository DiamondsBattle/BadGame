from ursina import Vec3
from lightning import *


class Map:
    def __init__(self):
        self.scale = Vec3(10, 15, 10)
        self.spawnpoints = [
            Vec3(17, 3.9, -11),
            Vec3(30, 3.9, 43)
        ]
        self.players_spawnpoints = {}
        self.spawn_rotations = {
            self.spawnpoints[0]: Vec3(0, 0, 0),
            self.spawnpoints[1]: Vec3(0, 180, 0),
        }
        self.map_objects = [
            {'name': 'ground0', 'position': Vec3(0.717209, 0.0650005, 1.47876), 'scale': Vec3(7.63412, 0.377096, 6.83478), 'model': 'cube', 'texture': 'grass', 'collider': 'box'},
            {'name': 'cube0', 'position': Vec3(1.77414, 0.0352307, -0.1615), 'rotation': Vec3(-30.3932, 0, 0), 'scale': Vec3(1, 1, 1.00228), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
            {'name': 'cube1', 'position': Vec3(0.163978, 0.132117, 0.0842512), 'rotation': Vec3(0, 0, 0), 'scale': Vec3(2.25593, 0.733819, 0.686022), 'texture': 'brick', 'model': 'cube', 'collider': 'box'},
            {'name': 'cube2', 'position': Vec3(2.57359, 0.341133, 2.90831), 'rotation': Vec3(-33.2264, 160.004, -1.07129e-06), 'scale': Vec3(3.61582, 0.193036, 0.741865), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
            {'name': 'cube3', 'position': Vec3(-0.511491, 0.0660003, 3.57692), 'rotation': Vec3(0, 0, 0), 'scale': Vec3(1.59711, 1, 1), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
            {'name': 'cube4', 'position': Vec3(3.3732, 0.0650005, 0.804685), 'rotation': Vec3(0, 0, 0), 'scale': Vec3(0, 0, 0), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
            {'name': 'sphere0', 'position': Vec3(-2.03666, 0.247244, 1.92628), 'rotation': Vec3(0, 0, 0), 'scale': Vec3(1.78112, 0.878218, 1.50543), 'model': 'sphere', 'texture': 'grass', 'collider': 'mesh'},
            {'name': 'cube5', 'position': Vec3(-1.17393, 0.0690011, 1.60021), 'rotation': Vec3(0, 20.8228, 0), 'scale': Vec3(1.84036, 1, 1), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
            {'name': 'cube6', 'position': Vec3(-1.86625, 0.0640001, -0.595428), 'rotation': Vec3(-42.092, 0, -135.657), 'scale': Vec3(1, 1, 1), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
            {'name': 'cube7', 'position': Vec3(1.38342, 0.067902, 1.1319), 'rotation': Vec3(8.68138, 20.8959, 0), 'scale': Vec3(1.21458, 0.72776, 0.72776), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
            {'name': 'cube8', 'position': Vec3(3.47625, 0.0649996, -1.0903), 'rotation': Vec3(7.55913, 52.4755, 0), 'scale': Vec3(1, 1, 1), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
            {'name': 'cube9', 'position': Vec3(1.51486, 0.0711185, 3.85773), 'rotation': Vec3(-32.2104, 0, -45.5435), 'scale': Vec3(1.61453, 1.61453, 1.61453), 'model': 'cube', 'texture': 'brick', 'collider': 'box'},
        ]
