import cocos
import GameData
import Map
import buildMenu

cocos.director.director.init()
    
# Create the scenes
buildingSelect_scene = cocos.scene.Scene(buildMenu.BuildSelectScene())

map = Map.Map(buildingSelect_scene)

game_data = GameData.GameData(10, 10, 10, 10, map)

buildingInfo_scene = cocos.scene.Scene(buildMenu.BuildInfoScene(game_data))
buildingSelect_scene.add(buildMenu.BuildMenu(buildingInfo_scene))



# And now, start the application, starting with main_scene
cocos.director.director.run(buildingSelect_scene)

# or you could have written, without so many comments:
#      director.run( cocos.scene.Scene( HelloWorld() ) )
