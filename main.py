import cocos
import GameData
import Map
import buildMenu

cocos.director.director.init()
    
# Create the scenes
map = Map.Map()
game_data = GameData.GameData(10, 10, 10, 10, map)

buildingSelect_scene = cocos.scene.Scene(buildMenu.BuildSelectScene(game_data))
map.addBSS(buildingSelect_scene)

map.add_hex(Map.Hex(0, 0, GameData.tile_information['LaunchPad']))

buildingInfo_scene = cocos.scene.Scene(buildMenu.BuildInfoScene(game_data))
buildingSelect_scene.add(buildMenu.BuildMenu(buildingInfo_scene))



# And now, start the application, starting with main_scene
cocos.director.director.run(buildingSelect_scene)

# or you could have written, without so many comments:
#      director.run( cocos.scene.Scene( HelloWorld() ) )
