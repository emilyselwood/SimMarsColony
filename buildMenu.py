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


class BuildSelectScene(cocos.layer.Layer):

    def __init__(self):
        super(BuildSelectScene, self).__init__() #constructor

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a cocosnode
        label = cocos.text.Label('Hello, World!',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        
        label.position = 320, 240
        self.add(label)

        label2 = cocos.text.Label('A new kind of label',
                                  font_name='Times New Roman',
                                  font_size=40,
                                  anchor_x='left', anchor_y='center')
        label2.position = 280, 170
        self.add(label2)
        
if __name__ == "__main__":
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # We create a new layer, an instance of HelloWorld
    hello_layer = HelloWorld()

    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene(hello_layer)

    # And now, start the application, starting with main_scene
    cocos.director.director.run(main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )
