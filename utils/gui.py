# coding=utf-8
from kivy.uix.button import Button

from kivy.uix.widget import Widget

# non-draggable image widget
class StaticImage(Widget):
    def __init__(self, pos, size, src):
        super(StaticImage, self).__init__()
        self.image.pos = pos
        self.image.size = size
        self.image.source = src


# transparent button with centered unstreched image wrapper
class ButtonImage(Button):
    def __init__(self, on_press, pos, size, size_img, src):
        super(ButtonImage, self).__init__(on_press=on_press, pos=pos, size=size, size_hint=(None, None),
                                          background_normal='images/scenery/transparency.png')
        self.add_widget(
            StaticImage(pos=(pos[0] + (size[0] - size_img[0]) / 2.0, pos[1] + (size[1] - size_img[1]) / 2.0),
                        size=size_img,
                        src=src))
