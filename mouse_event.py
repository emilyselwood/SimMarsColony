import cocos
from cocos.director import director

class MouseDisplay(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(MouseDisplay, self).__init__()

    def on_mouse_press(self, x, y, buttons, modifiers):

        self.posx, self.posy = director.get_virtual_coordinates(x, y)
        print(x,y)


if __name__ == "__main__":
    director.init(resizable=True)
    director.run(cocos.scene.Scene( MouseDisplay()))
