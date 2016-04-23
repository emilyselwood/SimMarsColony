import cocos
import GameData

class Map(cocos.layer.ColorLayer):

    def __init__(self):

        super( Map, self ).__init__(0xCC, 0x86, 0x61, 0xFF)

        self.hexes = []


    def add_hex(self, hex):
        self.hexes.append(hex)
        self.add(hex.sprite(), z = 0)

    def produce(self):


    def build(self, hexType, x, y):
        GameData.tile_information['Farm'])


class Hex():

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
    map.add_hex(Hex(1, 0, GameData.tile_information['Habitat']))
    map.add_hex(Hex(0, 1, GameData.tile_information['Habitat']))
    map.add_hex(Hex(1, 1, GameData.tile_information['Farm']))


    cocos.director.director.run (cocos.scene.Scene (map ) )
