import Map
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

    def __init__(self, energy, water, food, people, map):
        self.resources = {
            'energy': energy,
            'water': water,
            'food': food
        }
        self.people = people
        self.map = map

    def build(self, type, x, y):
        hex = Map.Hex(x, y, tile_information[type])
        # check we have the right materials available to build
        if not self.have_enough_stuff(hex.build):
            return False
        # TODO: check the grid is alowed to be built on.
        # reduce amout of resources
        self.subtract_stuff(hex.build)

        # add tile to map
        self.map.add_hex(hex)
        return True

    def consume(self):
        result = {}
        # buildings
        for key, value in self.map.cost_of_hexes().iteritems():
            v = result.get(key, 0)
            result[key] = v + value

        # consue for people as well

        # check we have enough stuff to survive if not ???
        if not self.have_enough_stuff(result):
            return False
        # remove stuff from store.
        self.subtract_stuff(result)
        return True

    def buildCost(self, type):
        build_details = type['build']
        build_energy = build_details['energy']
        build_water = build_details['water']
        build_food = build_details['food']
        string = "Build cost is " + str(build_energy) + " energy and " + str(build_water) + " water and " + str(build_food) + "food"
        return string

    def produce(self):
        for key, value in self.map.gained_from_hexes().iteritems():
            self.resources[key] = self.resources[key] + value

    def have_enough_stuff(self, to_remove):
        for key, value in to_remove.iteritems():
            if self.resources[key] - value < 0:
                return False
        return True

    def subtract_stuff(self, to_remove):
        for key, value in to_remove.iteritems():
            self.resources[key] = self.resources[key] - value


    def print_resources(self):
        for key, value in self.resources.iteritems():
            print('{key}:{value}'.format(key=key, value=value))

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
