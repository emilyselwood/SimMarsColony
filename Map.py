import cocos
import GameData
from cocos.director import director

class Map(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self, buildSelectScene):

        super( Map, self ).__init__(0xCC, 0x86, 0x61, 0xFF)
        self.build_select_scene = buildSelectScene

        self.hexes = []


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

# def on_mouse_press(self, x, y, buttons, modifiers):
        # self.posx, self.posy = director.get_virtual_coordinates(x,y)
        # print(x,y)

if __name__ == "__main__":
    cocos.director.director.init()

    map = Map()

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


    cocos.director.director.run (cocos.scene.Scene (map ) )
