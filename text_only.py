import GameData

gamedata = GameData.GameData()

while 1:
    hs = gamedata.getHabitats()
    print("You have " + str(gamedata.getHabitats()) + " habitats")
    print("You have " + str(gamedata.getHabitatMaterial()) + " Habitat Materal")
    hconsume = raw_input("How Much Habitat Material do you want to order?")
    gamedata.addHabitatMaterial(hconsume)
    tiles = raw_input("How many habitats do you want to create?")
    gamedata.makeHabitats(tiles);
    gamedata.produce()
