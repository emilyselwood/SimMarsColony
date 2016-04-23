import cocos
import GameData
from cocos.director import director
from cocos.scene import Scene
from cocos import tiles

import pyglet

class MainMap(cocos.layer.ScrollingManager):

    is_event_handler = True


    def __init__(self, buildSelectScene):


        super( MainMap, self ).__init__()
        self.map_loaded = tiles.load('background_map.tmx')

        layer = self.map_loaded['tile_layer_1']
        #layer.cells[1][1].tile.image = pyglet.image.load('assets/tile_oxygen.png')

        self.build_select_scene = buildSelectScene

        self.add(self.map_loaded['tile_layer_1'], z = 0)
        self.hexes = []


    def add_hex(self, hex):
        self.hexes.append(hex)
        oldTile = self.map_loaded['tile_layer_1'].cells[hex.x][hex.y].tile
        newTile = tiles.Tile(oldTile.id+1, oldTile.properties, pyglet.image.load(hex.image), None)
        self.map_loaded['tile_layer_1'].cells[hex.x][hex.y].tile = newTile

    def cost_of_hexes(self) :
        return self.for_each_hex('consume')

    def gained_from_hexes(self):
        return self.for_each_hex('produce')

    def for_each_hex(self, value_map):
        result = {}
        for hex in self.hexes:
            for key, value in getattr(hex, value_map).iteritems():
                v = result.get(key, 0)
                result[key] = v + value
        return result

    def on_mouse_press(self, x, y, buttons, modifiers):
        cocos.director.director.run(self.build_select_scene)


class Hex(object):

    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.image = map['image']
        self.build = map['build']
        self.consume = map['consume']
        self.produce = map['produce']

    def sprite(self):
        sprite = cocos.sprite.Sprite(self.image)
        x = 320 + self.x * 160
        y = 200 + self.y * 185
        if self.y % 2 == 0:
            x = x + 80
            y = y + 47
        sprite.position = x, y
        return sprite

class MouseDisplay(cocos.layer.Layer):
    is_event_handler = True
    def on_mouse_press(self, x, y, buttons, modifiers):
        self.posx, self.posy = director.get_virtual_coordinates(x,y)
        print(x,y)


if __name__ == "__main__":
    director.init(width=800, height=600, autoscale=False, resizable=True)

    map = MainMap()

    #startingHex = UnusedHex(0, 0)
    map.add_hex(Hex(0, 0, GameData.tile_information['Farm']))

    game_data = GameData.GameData(10, 10, 10, 10, map)
    game_data.print_resources()
    print("building farm")
    game_data.build('Farm', 1, 0)
    game_data.print_resources()
    print("Consuming resources")
    game_data.consume()
    game_data.print_resources()

    print("Produce resources")
    game_data.produce()
    game_data.print_resources()


    director.run (Scene (map ) )
