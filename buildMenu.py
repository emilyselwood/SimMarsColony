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

    def __init__(self, gamedata, buildingInfo_scene):
        super(BuildSelectScene, self).__init__(230,149,18,255) #constructor
        self.gamedata = gamedata

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a cocosnode
        label = cocos.text.Label('Scene 1',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        
        label.position = 320, 240
        self.add(label)

        self.update_resource_info()
        self.add(self.resource_label)
        self.add(BuildMenu(buildingInfo_scene))


    def update_resource_info(self):
        self.resource_label = cocos.text.Label(self.gamedata.get_resources(),
                                          font_name='Times New Roman',
                                          font_size=32,
                                          anchor_x='center', anchor_y='center')
        self.resource_label.position = 320, 120



class BuildMenu(cocos.menu.Menu):
    def __init__(self, buildingInfo_scene):
        super(BuildMenu, self).__init__("Click the apple")
        self.buildingInfo_scene = buildingInfo_scene

        menuItem1 = cocos.menu.ImageMenuItem("assets/ico-res-fd.png", self.onButtonClick)
        menuItem2 = cocos.menu.ImageMenuItem("assets/ico-res-fd.png", self.onButtonClick)
        menuItem3 = cocos.menu.ImageMenuItem("assets/ico-res-fd.png", self.onButtonClick)
        menuItem4 = cocos.menu.ImageMenuItem("assets/ico-res-fd.png", self.onButtonClick)
        menuItem5 = cocos.menu.ImageMenuItem("assets/ico-res-fd.png", self.onButtonClick)
        menuItem6 = cocos.menu.ImageMenuItem("assets/ico-res-fd.png", self.onButtonClick)
        
        #for each (building in the buildings from gamedata)
        #
        # create a menu item and add to $allMenuItems
        #
        # self.create_menu([$allMenuItems])
        #

        self.create_menu([menuItem1,menuItem2,menuItem3,menuItem4,menuItem5,menuItem6])

    def onButtonClick(self):
        cocos.director.director.run(self.buildingInfo_scene)






class BuildThisMenu(cocos.menu.Menu):
    def __init__(self, gamedata):
        super(BuildThisMenu, self).__init__()
        self.gamedata = gamedata
        self.map = self.gamedata.map
        
        build_button = cocos.menu.MenuItem('Build', self.onButtonClick)
        self.create_menu([build_button])
    
    def onButtonClick(self):
        self.gamedata.build('Farm', 1, 0)
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
