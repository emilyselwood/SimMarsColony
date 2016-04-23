import cocos
import GameData
import buildMenu
from cocos.director import director

class Map(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):

        super( Map, self ).__init__(0xCC, 0x86, 0x61, 0xFF)

        self.hexes = []
    
    def addBSS(self, buildSelectLayer, buildSelectScene):
        self.build_select_layer = buildSelectLayer
        self.build_select_scene = buildSelectScene


    def add_hex(self, hex):
        self.hexes.append(hex)
        self.add(hex.sprite(), z = 0)

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

# def on_mouse_press(self, x, y, buttons, modifiers):
        # self.posx, self.posy = director.get_virtual_coordinates(x,y)
        # print(x,y)

