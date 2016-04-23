
tile_information = {
    'Farm': {
        'image': 'assets/hexagon-filled2.png',
        'build': {
            'energy': 1,
            'food': 1,
        },
        'consume': {
            'water': 1,
        },
        'produce': {
            'food': 3,
        }
    },
    'Habitat': {
        'image': 'assets/hexagon-filled2.png',
        'build': {
            'energy': 1,
            'food': 1,
        },
        'consume': {
            'food': 1,
        },
        'produce': {
            'energy': 2,
        }

    }
}



class GameData(object):

    def __init__(self):
        self.habitatmaterial = 4
        self.habitats = 0
        self.habitatcost = 2
        self.habitatproductivity = 2

    def setHabitatMaterial(self, n):
        self.habitatmaterial = n

    def addHabitatMaterial(self, n):
        self.habitatmaterial = self.habitatmaterial + int(n)

    def getHabitatMaterial(self):
        return self.habitatmaterial

    def getHabitats(self):
        return self.habitats

    def makeHabitats(self, number):
        n = int(number)
        self.habitatmaterial = self.habitatmaterial - n*self.habitatcost
        self.habitats = self.habitats + n

    def produce(self):
        self.habitatmaterial = self.habitatmaterial + self.habitats*self.habitatproductivity
