from ursinanetworking import *
from scenes.arena import Map as Arena
from random import randint

server = UrsinaNetworkingServer('localhost', 54321)
easy_server = EasyUrsinaNetworkingServer(server)

map_objects = {}


@server.event
def onClientConnected(client):
    global player_count
    player_count += 1
    easy_server.update_replicated_variable_by_name(
        'player_count',
        'data',
        player_count,
    )
    spawnpoint = map.spawnpoints[randint(0, len(map.spawnpoints) - 1)]
    easy_server.create_replicated_variable(
        f'player_{client.id}',
        {
            'type': 'player',
            'id': client.id,
            'position': spawnpoint,
            'rotation': map.spawn_rotations[spawnpoint],
        }
    )
    print(f'{client} connected')
    client.send_message('getId', client.id)


@server.event
def onClientDisconnected(client):
    global player_count
    player_count -= 1
    easy_server.update_replicated_variable_by_name(
        'player_count',
        'data',
        player_count
    )
    easy_server.remove_replicated_variable_by_name(f'player_{client.id}')
    print(f'Client {client.id} disconnected')


@server.event
def myPosition(client, new_pos):
    print(f'{client.id}\t{new_pos}')
    easy_server.update_replicated_variable_by_name(f'player_{client.id}', 'position', new_pos)


def loadMap():
    global map
    map = Arena()
    for obj in map.map_objects:
        obj['type'] = 'map_object'
        easy_server.create_replicated_variable(
            obj['name'],
            obj,
        )
        map_objects[obj['name']] = obj


loadMap()

player_count = 0
easy_server.create_replicated_variable(
    'player_count',
    {
        'type': 'info',
        'data': player_count,
    }
)

while True:
    easy_server.process_net_events()
