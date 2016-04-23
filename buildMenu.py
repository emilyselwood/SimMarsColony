#
# cocos2d
# http://python.cocos2d.org
#

from __future__ import division, print_function, unicode_literals

# Import assemblies
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

import cocos


class BuildSelectScene(cocos.layer.ColorLayer):

    def __init__(self):
        super(BuildSelectScene, self).__init__(230,149,18,255) #constructor

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a cocosnode
        label = cocos.text.Label('Scene 1',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        
        label.position = 320, 240
        self.add(label)

class BuildMenu(cocos.menu.Menu):
    def __init__(self):
        super(BuildMenu, self).__init__("Click the apple")

        CCMenuItem = cocos.menu.ImageMenuItem("ico-res-fd.png", self.onButtonClick)
        self.create_menu([CCMenuItem])

    def onButtonClick(self):
        cocos.director.director.run(buildingInfo_scene)

class BuildInfoScene(cocos.layer.ColorLayer):

    def __init__(self):
        super(BuildInfoScene, self).__init__(64,64,224,255) #constructor

        label = cocos.text.Label('Scene 2',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        
        label.position = 320, 240
        self.add(label)
        
if __name__ == "__main__":
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # Create the scenes
    buildingSelect_scene = cocos.scene.Scene(BuildSelectScene())
    buildingSelect_scene.add(BuildMenu())
    buildingInfo_scene = cocos.scene.Scene(BuildInfoScene())

    # And now, start the application, starting with main_scene
    cocos.director.director.run(buildingSelect_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )
