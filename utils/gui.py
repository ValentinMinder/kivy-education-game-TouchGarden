# coding=utf-8
from kivy.uix.image import Image
from kivy.uix.label import Label


from kivy.uix.widget import Widget

# non-draggable image widget
class StaticImage(Widget):
    def __init__(self, pos, size, src):
        super(StaticImage, self).__init__()
        self.image.pos = pos
        self.image.size = size
        self.image.source = src


# transparent button with centered unstreched image wrapper
class ButtonWrap(Widget):
    def __init__(self, fct, pos, size, size_img, src):
        super(ButtonWrap, self).__init__()
        self.button.on_touch_down = fct
        self.button.pos = pos
        self.button.size = size
        self.button.background_normal = 'images/scenery/transparency.png'
        self.button.add_widget(
            StaticImage(pos=(pos[0] + (size[0] - size_img[0]) / 2.0, pos[1] + (size[1] - size_img[1]) / 2.0),
                        size=size_img, src=src))
