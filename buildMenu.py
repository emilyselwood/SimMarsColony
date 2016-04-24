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

    def __init__(self, gamedata, x, y):
        super(BuildSelectScene, self).__init__(230, 149, 18, 255) #constructor
        self.gamedata = gamedata
        self.x = x
        self.y = y

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a cocosnode
        label = cocos.text.Label('Select Building you would like:',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')

        label.position = 320, 560

        self.add(label)

        self.update_resource_info()
        self.add(self.resource_label)
        self.add(BuildMenu(self.gamedata, self.x, self.y))

    def update_resource_info(self):
        resource_dict = self.gamedata.get_resources()
        string = ""
        for key, v in resource_dict.iteritems():
            string = string + key + " : " + str(v) + "\n"
        
        self.resource_label = cocos.text.Label(string,
                                          font_name='Times New Roman',
                                          font_size=22,
                                          multiline = True,
                                          width = 300,
                                          anchor_x='center', anchor_y='center')
        self.resource_label.position = 500, 300


class BuildMenu(cocos.menu.Menu):
    def __init__(self, gamedata, x, y):
        super(BuildMenu, self).__init__()
        self.gamedata = gamedata
        self.x = x
        self.y = y
        #for each building from gamedata create buttons and store in an array
        allMenuItems = []
        self.font_item["font_size"]=20
        self.font_item_selected["font_size"] = 22
        #
        for k, i in GameData.GameData.get_build_information(gamedata).iteritems():
            allMenuItems.append(cocos.menu.ImageMenuItem(i['image'], self.onButtonClick, k))
            allMenuItems.append(cocos.menu.MenuItem(k, self.onButtonClick,k))

        self.create_menu(allMenuItems)
        self.position = -200, 0


    def onButtonClick(self,buildingType):

        print (buildingType)
        self.buildingInfo_scene = BuildInfoScene(self.gamedata, buildingType, self.x, self.y)
        cocos.director.director.run(cocos.scene.Scene(self.buildingInfo_scene))


class BuildThisMenu(cocos.menu.Menu):
    def __init__(self, gamedata, buildingType, x, y):
        super(BuildThisMenu, self).__init__()
        self.gamedata = gamedata
        self.map = self.gamedata.map
        self.building_type = buildingType
        self.x = x
        self.y = y

        build_button = cocos.menu.MenuItem('Build', self.onButtonClick)
        self.create_menu([build_button])
        self.position = 200, -200

    def onButtonClick(self):
        self.gamedata.build(self.building_type, self.x, self.y)
        cocos.director.director.run(cocos.scene.Scene(self.map))

class BuildInfoScene(cocos.layer.ColorLayer):

    def __init__(self, gamedata, buildingType,x, y):

        super(BuildInfoScene, self).__init__(64,64,224,255) #constructor
        self.gamedata = gamedata
        self.x = x
        self.y = y
        self.building_type = buildingType
        gs_string = self.gamedata.buildCost(buildingType)
        self.add(BuildThisMenu(self.gamedata, buildingType, self.x, self.y))

        label = cocos.text.Label(gs_string,
                                 font_name='Times New Roman',
                                 font_size=12,
                                 anchor_x='center', anchor_y='center')

        label.position = 320, 240
        self.add(name_label)
        self.add(label)
