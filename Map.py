import cocos
import GameData
import buildMenu
from cocos.director import director
from cocos.scene import Scene
from cocos import tiles

import pyglet

class MainMap(cocos.layer.ScrollingManager):

    is_event_handler = True

    def __init__(self, buildSelectScene):

        super( MainMap, self ).__init__()
        self.build_select_scene = buildSelectScene

        self.map_loaded = tiles.load('background_map.tmx')['tile_layer_1']

        self.add(self.map_loaded, z = 0)
        center = self.map_loaded.cells[10][7].center
        self.map_loaded.set_view(5, 5, 15, 15, 0, 0)
        self.set_focus(center[0], center[1])
        self.hexes = []



    def addBSS(self, buildSelectLayer, buildSelectScene):
        self.build_select_layer = buildSelectLayer
        self.build_select_scene = buildSelectScene

    def add_hex(self, hex):
        self.hexes.append(hex)
        cell = self.map_loaded.cells[hex.x][hex.y]
        cell.tile = tiles.Tile(cell.tile.id+len(self.hexes), cell.tile.properties, pyglet.image.load(hex.image), None)
        self.map_loaded.set_dirty()


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
        self.game_data.consume()
        self.game_data.produce()
        buildingInfo_scene = cocos.scene.Scene(buildMenu.BuildInfoScene(self.game_data))
        building_select_layer = buildMenu.BuildSelectScene(self.game_data)
        buildingSelect_scene = cocos.scene.Scene(building_select_layer)
        cocos.director.director.run(buildingSelect_scene)

    def addGameData(self, gamedata):
        self.game_data = gamedata



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
