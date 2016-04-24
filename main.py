import cocos
import GameData
import Map
import buildMenu

cocos.director.director.init(width=800, height=600, autoscale=True, resizable=True)

# Create the scenes

map = Map.MainMap(None)

game_data = GameData.GameData(10, map)


map.add_hex(Map.Hex(10, 7, GameData.tile_information['LaunchPad']))
#map.addBSS(building_select_layer, buildingSelect_scene)
map_scene = cocos.scene.Scene(map)

# And now, start the application, starting with main_scene
cocos.director.director.run(map_scene)

# or you could have written, without so many comments:
#      director.run( cocos.scene.Scene( HelloWorld() ) )
