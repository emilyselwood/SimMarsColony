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
import Map

class BuildSelectScene(cocos.layer.ColorLayer):

    def __init__(self, gamedata):
        super(BuildSelectScene, self).__init__(230,149,18,255) #constructor
        self.gamedata = gamedata
        

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a cocosnode
        label = cocos.text.Label('Scene 1',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        
        label.position = 320, 140
        self.add(label)

        self.update_resource_info()
        self.add(self.resource_label)
        self.add(BuildMenu(cocos.scene.Scene(BuildInfoScene(self.gamedata)), self.gamedata))


    def update_resource_info(self):
        self.resource_label = cocos.text.Label(self.gamedata.get_resources(),
                                          font_name='Times New Roman',
                                          font_size=32,
                                          anchor_x='center', anchor_y='center')
        self.resource_label.position = 320, 120


class BuildMenu(cocos.menu.Menu):
    def __init__(self, buildingInfo_scene,gamedata):
        super(BuildMenu, self).__init__("Click the apple")
        self.buildingInfo_scene = buildingInfo_scene
        self.gamedata = gamedata

        #for each building from gamedata create buttons and store in an array
        allMenuItems = []
        for i in GameData.GameData.get_build_information(gamedata):
            allMenuItems.append(cocos.menu.ImageMenuItem("assets/ico-res-fd.png", self.onButtonClick))
        theMenu = self.create_menu(allMenuItems)

    def onButtonClick(self):
        # self.building_info_scene.set_building_type('Farm')
        cocos.director.director.run(self.buildingInfo_scene)


class BuildThisMenu(cocos.menu.Menu):
    def __init__(self, gamedata):
        super(BuildThisMenu, self).__init__()
        self.gamedata = gamedata
        self.map = self.gamedata.map
        
        build_button = cocos.menu.MenuItem('Build', self.onButtonClick)
        self.create_menu([build_button])
    
    def onButtonClick(self):
        self.gamedata.build('Farm')
        cocos.director.director.run(cocos.scene.Scene(self.map))

class BuildInfoScene(cocos.layer.ColorLayer):

    def __init__(self, gamedata):
        super(BuildInfoScene, self).__init__(64,64,224,255) #constructor
        self.gamedata = gamedata
        gs_string = self.gamedata.buildCost('Farm')
        self.add(BuildThisMenu(self.gamedata))

        label = cocos.text.Label(gs_string,
                                 font_name='Times New Roman',
                                 font_size=12,
                                 anchor_x='center', anchor_y='center')
        
        label.position = 320, 240
        self.add(label)
