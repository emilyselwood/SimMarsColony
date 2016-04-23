import cocos
import GameData

class Map(cocos.layer.ColorLayer):

    def __init__(self):

        super( Map, self ).__init__(0xCC, 0x86, 0x61, 0xFF)

        self.hexes = []


    def add_hex(self, hex):
        self.hexes.append(hex)
        self.add(hex.sprite(), z = 0)

    def cost_of_hexes(self) :
        result = {}
        for hex in self.hexes:
            for key, value in hex.consume.iteritems():
                v = result.get(key, 0)
                result[key] = v + value
        return result


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


    cocos.director.director.run (cocos.scene.Scene (map ) )
