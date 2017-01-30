# coding=utf-8
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from utils import sizes

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

class ButtonImageChoices(ButtonImage):
    def __init__(self, on_press, pos, text):
        size = (sizes.win_choice_width, sizes.win_choice_height)
        super(ButtonImageChoices, self).__init__(on_press=on_press, pos=pos, size=size, size_img=size,
                                          src = 'images/scenery/fond_menu_choix_400x193px.png')

        self.add_widget(
            LabelWrap(pos=(pos[0], pos[1] + sizes.win_choice_height - sizes.win_choice_header),
                      size=(sizes.win_choice_width, sizes.win_choice_header),
                      text=text,
                      font_size=sizes.font_size_subtitle,
                      bold=True))

# for speach
class LabelWrap(Widget):
    def __init__(self, pos, size, text, font_size = sizes.font_size_default, bold=False, vAlignTop=False):
        super(LabelWrap, self).__init__()
        self.label.pos = pos
        self.label.size = size
        self.label.text = text.get()
        self.text = text
        self.bold = bold
        self.bolden()
        self.label.font_size = font_size
        if (vAlignTop):
            self.label.valign = 'top'

    def bolden(self):
        if (self.bold):
            self.label.text = "[b]" + self.label.text + "[/b]"

    def update_cat(self, current_cat):
        self.label.text = self.text.get() + " " + str(current_cat) + "/" + str(sizes.gauge_number)
        self.bolden()
