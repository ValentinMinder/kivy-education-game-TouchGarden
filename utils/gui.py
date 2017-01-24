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