import cocos
import GameData
import Map
import buildMenu

cocos.director.director.init()

# Create the scenes


game_data = GameData.GameData(10, 10, 10, 10, None)

buildingInfo_scene = cocos.scene.Scene(buildMenu.BuildInfoScene(game_data))
building_select_layer = buildMenu.BuildSelectScene(game_data, buildingInfo_scene)
buildingSelect_scene = cocos.scene.Scene(building_select_layer)
map = Map.MainMap(buildingInfo_scene)
game_data.map = map
map.addBSS(building_select_layer, buildingSelect_scene)

map.add_hex(Map.Hex(0, 0, GameData.tile_information['LaunchPad']))




# And now, start the application, starting with main_scene
cocos.director.director.run(buildingSelect_scene)

# or you could have written, without so many comments:
#      director.run( cocos.scene.Scene( HelloWorld() ) )
