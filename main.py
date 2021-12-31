from ursina import *
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

from prefabs.controller import Controller
from prefabs.gun import Gun
from prefabs.player import Player

from scenes.arena import Map as ArenaScene

from ursinanetworking import *

from random import randint


class Handler(Entity):
    def __init__(self):
        super().__init__(
            eternal=True
        )

        self.id = None
        self.players = {}
        self.players_target_pos = {}
        self.map_objects = {}

        self.top_text = Text(position=window.top_left)
        self.skybox_texture = Texture('lightning/textures/skybox.jpg')
        scene = ArenaScene()
        texture.filtering = True
        self.sky = Sky(
            model='sphere',
            double_sided=True,
            texture=self.skybox_texture,
            rotation=Vec3(0, 270, 0)
        )
        self.sun = DirectionalLight(
            shadows=True
        )
        self.sun.look_at(Vec3(-2, -1, -2))
        shadow_res = 2**12
        self.sun.shadow_map_resolution = Vec2(shadow_res, shadow_res)
        self.controller = Controller(
            spawnpoints=scene.spawnpoints,
            spawn_rotations=scene.spawn_rotations,
        )
        spawn_pos = scene.spawnpoints[randint(0, len(scene.spawnpoints) - 1)]
        self.controller.position = spawn_pos
        self.controller.rotation = scene.spawn_rotations[spawn_pos]
        self.gun = Gun(
            parent=camera,
            position=Vec3(1.5, -.4, 1.5),
            scale=Vec3(.4, .5, 2),
            always_on_top=True,
            specularMap=None,
            normalMap=None,
            ambientStrength=.75,
            shader=lit_with_shadows_shader,
        )

    def update(self):
        self.top_text.text = f'X : {round(self.controller.x)}\nY : {round(self.controller.y)}\nZ : {round(self.controller.z)}'
        if 'player_count' in easy_client.replicated_variables:
            self.top_text.text += f'\n<red>Player Count : {easy_client.replicated_variables["player_count"].content["data"]}<red>'

        for var in easy_client.replicated_variables:
            if easy_client.replicated_variables[var].content['type'] == 'player' and easy_client.replicated_variables[var].content['id'] != handler.id:
                self.players[var].position = easy_client.replicated_variables[var].content['position']
                self.players[var].rotation = easy_client.replicated_variables[var].content['rotation']

        client.send_message('myPosition', tuple(self.controller.position))
        easy_client.process_net_events()

    def input(self, key):  # ignore
        if key == 'tab':
            self.controller.die()


if __name__ == '__main__':

    app = Ursina()
    window.borderless = False
    application.quit = lambda x: x

    handler = Handler()

    client = UrsinaNetworkingClient('localhost', 54321)
    easy_client = EasyUrsinaNetworkingClient(client)

    @client.event
    def onConnectionEstablished():
        print('Connected to server')


    @client.event
    def onConnectionError(reason):
        print(f'Error ! {reason}')


    @client.event
    def getId(id):
        handler.id = id
        print(f'Id : {handler.id}')


    @easy_client.event
    def onReplicatedVariableCreated(var):
        global client
        var_name = var.name
        var_type = var.content['type']
        if var_type == 'map_object':
            new_obj = Entity(
                parent=handler.controller,
                shader=lit_with_shadows_shader,
            )
            new_obj.name = var_name
            for i in var.content:
                setattr(new_obj, i, var.content[i])
            if var_name == 'cube1':
                new_obj.texture = 'brick'
            new_obj.scale *= Vec3(13, 13, 13)
            new_obj.position *= 13
            new_obj.client = client
            handler.map_objects[var_name] = new_obj
            new_obj.parent = scene
        elif var_type == 'player':
            print(f'new player {var_name}')
            handler.players[var_name] = Player(
                position=var.content['position'] + Vec3(0, 1, 0),
                rotation=var.content['rotation'],
            )
            print(handler.players)
            if handler.id == int(var.content['id']):
                handler.players[var_name].enabled = False
                handler.controller.position = var.content['position']


    @easy_client.event
    def onReplicatedVariableUpdated(var):
        if var.content['type'] == 'player':
            handler.players[var.name].position = var.content['position']
            handler.players[var.name].rotation = var.content['rotation']


    @easy_client.event
    def onReplicatedVariableRemoved(var):
        print(f'Removed var : {var}')
        global client
        var_name = var.name
        var_type = var.type
        if var_type == 'map_object':
            destroy(handler.map_objects[var_name])
            del handler.map_objects[var_name]
        elif var_type == 'player':
            destroy(handler.players[var_name])
            del handler.players[var_name]


    app.run()
