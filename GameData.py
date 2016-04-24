import Map
tile_information = {
    'Farm': {
        'image': 'assets/tile_farm.png',
        'build': {
            'materials': 1,
            'food': 1,
        },
        'consume': {
            'water': 1,
            'energy': 1,
        },
        'produce': {
            'food': 1,
            'oxygen': 1,
        }
    },
    'LaunchPad' : {
        'image' : 'assets/tile_landingdeck.png',
        'build': {
            'energy': 0,
            'food': 0,
        },
        'consume': {
            'water': 0,
        },
        'produce': {
            'water': 0,
    }
    },
    'Habitat': {
        'image': 'assets/tile_habitat.png',
        'build': {
            'materials': 1,
        },
        'consume': {
            'food': 0,
        },
        'produce': {
            'energy': 0,
        }

    },
    'CommsTower': {
        'image': 'assets/tile_comms.png',
        'build': {
            'materials': 1,
        },
        'consume': {
            'energy': 1,
        },
        'produce': {
            'energy': 0,
        }

    },
    'MiningDome' : {
        'image': 'assets/tile_rover.png',
        'build': {
            'materials': 1,
         },
        'consume': {
            'energy': 1,
        },
        'produce': {
            'materials': 1,
            'water': 1,
        }
    },
    'SolarFarm' : {
        'image': 'assets/tile_solar.png',
        'build': {
            'materials': 1,
        },
        'consume': {
            'energy': 0,
        },
        'produce': {
            'energy': 1,
        }
    },
    'OxygenPlant' : {
        'image': 'assets/tile_oxygen.png',
        'build': {
            'materials': 1,
        },
        'consume': {
            'water': 2,
            'energy': 1,
        },
        'produce': {
            'oxygen': 2,
        }
    }

}

class GameData(object):

    def __init__(self, energy, water, food, oxygen, materials, people, map):
        self.resources = {
            'energy': energy,
            'water': water,
            'food': food,
            'oxygen' : oxygen,
            'materials' : materials
        }
        self.rocket_payload = {
            'food' : 2,
            'materials' : 2,
            'energy': 1,
            'oxygen' : 2,
            'water' : 2,
        }
        self.people = people
        self.map = map
        self.map.addGameData(self)

        self.position_index = 0
        self.cell_list = self.map.get_neighbors(10, 7)
        self.current_x = self.cell_list[self.position_index][0]
        self.current_y = self.cell_list[self.position_index][1]

    def get_build_information(self):
        v = {}
        for k, value in tile_information.iteritems():
            v[k] = value
        return v

    def build(self, type, x, y):
        print("GameData.build({type},{x}:{y})".format(type = type, x = x, y = x))
        hex = Map.Hex(x, y, tile_information[type])
        #self.advance_coordinates()
        # check we have the right materials available to build
        if not self.have_enough_stuff(hex.build):
            return False

        # reduce amount of resources
        self.subtract_stuff(hex.build)

        # add tile to map
        self.map.add_hex(hex)
        return True

    def advance_coordinates(self):

        self.position_index = self.position_index + 1
        if self.position_index >= len(self.cell_list):
            self.cell_list = self.map.get_neighbors(self.current_x, self.current_y)
            self.position_index = 0

        self.current_x = self.cell_list[self.position_index][0]
        self.current_y = self.cell_list[self.position_index][1]

        print("current(xy){x}:{y}".format(x = self.current_x, y = self.current_y))


    def consume(self):
        result = {}
        # buildings
        for key, value in self.map.cost_of_hexes().iteritems():
            v = result.get(key, 0)
            result[key] = v + value

        # consume for people as well

        # check we have enough stuff to survive if not ???
        if not self.have_enough_stuff(result):
            return False
        # remove stuff from store.
        self.subtract_stuff(result)
        return True

    def buildCost(self, type):
        building_type = tile_information[type]
        string = ""
        for key, value in building_type['build'].iteritems():
            string = string + key + " : " + str(value) + " "
        return string

    def getMap(self):
        return self.map

    def produce(self):
        for key, value in self.map.gained_from_hexes().iteritems():
            self.resources[key] = self.resources[key] + value

    def rocket_arrives(self):
        for key, value in self.rocket_payload.iteritems():
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


    def get_resources(self):
        string = ""
        for key, value in self.resources.iteritems():
            string = string + key + ":" + str(value) + " "
        return string
