import Map
tile_information = {
    'Farm': {
        'image': 'assets/tile_farm.png',
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
    'LaunchPad' : {
        'image' : 'assets/hexagon-filled2.png',
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
        map.addGameData(self)
        self.current_x = 1
        self.current_y = 0

    def build(self, type):
        hex = Map.Hex(self.current_x, self.current_y, tile_information[type])
        self.advance_coordinates()
        # check we have the right materials available to build
        if not self.have_enough_stuff(hex.build):
            return False
        # TODO: check the grid is alowed to be built on.
        # reduce amout of resources
        self.subtract_stuff(hex.build)

        # add tile to map
        self.map.add_hex(hex)
        return True

    def advance_coordinates(self):
        if (self.current_x == 1):
            if (self.current_y == 0):
                self.current_y = 1
                return True
            if (self.current_y == 1):
                self.current_x = 0
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
        building_type = tile_information[type]
        build_details = building_type['build']
        build_energy = build_details.get('energy', 0)
        build_food = build_details.get('food', 0)
        
        build_water = build_details.get('water', 0)
        string = "Build cost is %s energy \n and %s water \n and %s food" % (build_energy, build_water, build_food)
        return string

    def getMap(self):
        return self.map

    def produce(self):
        for key, value in self.map.gained_from_hexes().iteritems():
            self.resources[key] = self.resources[key] + value
        self.print_resources()
 
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

    def get_resources(self):
        string = ""
        for key, value in self.resources.iteritems():
            string = string + key + ":" + str(value) + " "
        return string
