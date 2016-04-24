import cocos
import GameData
import Map
import buildMenu

cocos.director.director.init()

# Create the scenes

map = Map.MainMap(None)

game_data = GameData.GameData(10, 10, 10, 10, map)


building_select_layer = buildMenu.BuildSelectScene(game_data)
buildingSelect_scene = cocos.scene.Scene(building_select_layer)

map.add_hex(Map.Hex(10, 7, GameData.tile_information['LaunchPad']))
map.addBSS(building_select_layer, buildingSelect_scene)




# And now, start the application, starting with main_scene
cocos.director.director.run(buildingSelect_scene)

# or you could have written, without so many comments:
#      director.run( cocos.scene.Scene( HelloWorld() ) )
