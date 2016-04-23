import cocos
from cocos.director import director
import cocos.menu

class MouseDisplay(cocos.layer.Layer):
    """
    Test file for implementing mouse controls
    Unused in final project
    """
    is_event_handler = True

    def __init__(self):
        super(MouseDisplay, self).__init__()

    def is_inside_box( self, x, y ):
        (ax,ay,bx,by) = self.get_box()
        if( x >= ax and x <= bx and y >= ay and y <= by ):
            return True
        return False

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.posx, self.posy = director.get_virtual_coordinates(x,y)
        print(x,y)

        if self.selected_index[1].is_inside_box(x,y):
            self._activate_item()


if __name__ == "__main__":
    director.init(resizable=True)
    director.run(cocos.scene.Scene( MouseDisplay()))
