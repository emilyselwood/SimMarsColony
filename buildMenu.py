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
        label = cocos.text.Label('Select Building you would like:',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='top')

        label.position = 300, 600

        self.add(label)

        self.update_resource_info()
        self.add(self.resource_label)
        self.add(BuildMenu(self.gamedata))


    def update_resource_info(self):
        self.resource_label = cocos.text.Label(self.gamedata.get_resources(),
                                          font_name='Times New Roman',
                                          font_size=22,
                                          anchor_x='center', anchor_y='center')
        self.resource_label.position = 320, 20


class BuildMenu(cocos.menu.Menu):
    def __init__(self, gamedata):
        super(BuildMenu, self).__init__()
        self.gamedata = gamedata
        #for each building from gamedata create buttons and store in an array
        allMenuItems = []

        #
        for k, i in GameData.GameData.get_build_information(gamedata).iteritems():
            allMenuItems.append(cocos.menu.ImageMenuItem(i['image'], self.onButtonClick,k))

        self.create_menu(allMenuItems)


    def onButtonClick(self,buildingType):

        print (buildingType)
        self.buildingInfo_scene = BuildInfoScene(self.gamedata, buildingType)
        cocos.director.director.run(cocos.scene.Scene(self.buildingInfo_scene))


class BuildThisMenu(cocos.menu.Menu):
    def __init__(self, gamedata, buildingType):
        super(BuildThisMenu, self).__init__()
        self.gamedata = gamedata
        self.map = self.gamedata.map
        self.building_type = buildingType

        buildButton = cocos.menu.MenuItem('Build', self.onButtonClick)
        self.create_menu([buildButton])

    def onButtonClick(self):
        self.gamedata.build(self.building_type)
        cocos.director.director.run(cocos.scene.Scene(self.map))

class BuildInfoScene(cocos.layer.ColorLayer):

    def __init__(self, gamedata, buildingType):
        super(BuildInfoScene, self).__init__(64,64,224,255) #constructor
        self.gamedata = gamedata
        self.building_type = buildingType
        gs_string = self.gamedata.buildCost(buildingType)
        self.add(BuildThisMenu(self.gamedata, buildingType))

        label = cocos.text.Label(gs_string,
                                 font_name='Times New Roman',
                                 font_size=12,
                                 anchor_x='center', anchor_y='center')

        label.position = 320, 140
        self.add(label)
