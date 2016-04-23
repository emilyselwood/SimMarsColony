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
import GameData


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
    def __init__(self, buildingInfo_scene):
        super(BuildMenu, self).__init__("Click the apple")
        self.buildingInfo_scene = buildingInfo_scene

        CCMenuItem = cocos.menu.ImageMenuItem("ico-res-fd.png", self.onButtonClick)
        self.create_menu([CCMenuItem])

    def onButtonClick(self):
        cocos.director.director.run(self.buildingInfo_scene)

class BuildThisMenu(cocos.menu.Menu):
    def __init__(self, map):
        super(BuildThisMenu, self).__init__("Build")
        self.map = map
        
        build_button = cocos.menu.MenuItem('Build', self.onButtonClick)
        self.create_menu([build_button])
    
    def onButtonClick(self):
        cocos.director.director.run(cocos.scene.Scene(self.map))

class BuildInfoScene(cocos.layer.ColorLayer):

    def __init__(self, gamedata):
        super(BuildInfoScene, self).__init__(64,64,224,255) #constructor
        self.gamedata = gamedata
        gs_string = gamedata.buildCost('Farm')
        self.add(BuildThisMenu(self.gamedata.getMap()))

        label = cocos.text.Label(gs_string,
                                 font_name='Times New Roman',
                                 font_size=12,
                                 anchor_x='center', anchor_y='center')
        
        label.position = 320, 240
        self.add(label)
