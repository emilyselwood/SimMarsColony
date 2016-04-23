import cocos

class Map(cocos.layer.ColorLayer):

    def __init__(self):

        super( Map, self ).__init__(0xCC, 0x86, 0x61, 0xFF)

        self.hexes = []


    def add_hex(self, hex):
        self.hexes.append(hex)
        self.add(hex.sprite(), z = 0)


class Hex():

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def sprite(self):
        sprite = cocos.sprite.Sprite(self.image)
        x = 320 + self.x * 160
        y = 200 + self.y * 185
        if self.y % 2 == 0:
            x = x + 80
            y = y + 47
        sprite.position = x, y
        return sprite

class LaunchPad(Hex):
    def __init__(self, x, y):
        Hex.__init__(self, x, y, 'hexagon-filled2.png')

class Farm(Hex):
    def __init__(self, x, y):
        Hex.__init__(self, x, y, 'hexagon-filled2.png')

class PowerStation(Hex):
    def __init(self, x, y):
        Hex.__init__(self, x, y, 'hexagon-filled2.png')


if __name__ == "__main__":
    cocos.director.director.init()

    map = Map()

    #startingHex = UnusedHex(0, 0)
    map.add_hex(LaunchPad(0, 0))
    map.add_hex(Farm(1, 0))
    map.add_hex(Farm(0, 1))
    map.add_hex(PowerStation(1, 1))


    cocos.director.director.run (cocos.scene.Scene (map ) )
