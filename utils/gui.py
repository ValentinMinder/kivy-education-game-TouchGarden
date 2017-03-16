# coding=utf-8
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from utils import sizes

# wrapping widget containing a single image
# used for exact x/y image positioning (image is NOT centered)
# widget can be added to a FloatLayout and wrapped Image will be correctly placed
# to change image properties, access it with widget.image
class ImageWrap(Widget):
    def __init__(self, source = 'images/scenery/transparency.png', pos = (100, 100), size = (200,200), allow_stretch = False, keep_ratio=True, anim_delay=0.5, anim_loop=0):
        super(ImageWrap, self).__init__()
        self.image = ImageFlip()
        self.add_widget(self.image)
        self.image.source = source
        self.image.pos = pos
        self.image.size = size
        self.image.allow_stretch = allow_stretch
        self.image.keep_ratio = keep_ratio
        self.image.anim_delay = anim_delay
        self.image.anim_loop = anim_loop

    def flip(self):
        self.image.flip()


# a flippable image, including animated ones (flip once all the textures, until they are all flipped)
class ImageFlip(Image):
    def __init__(self):
        super(ImageFlip, self).__init__()
        self.should_flip = False
        self.tex_ref = [0,0,0,0,0,0,0,0]

    def flip(self):
        # flip the current texture and memorize
        self.should_flip = True
        self.tex_ref = self.texture.tex_coords
        self.texture.flip_horizontal()

    #react to texture changes, eg. to flip the image (only when needed
    def on_texture(self, *any):
        if (self.should_flip):
            if (self.texture.tex_coords == self.tex_ref):
                self.texture.flip_horizontal()
            else:
                self.should_flip = False
                self.tex_ref = [0,0,0,0,0,0,0,0]


# transparent button with centered unstreched image wrapper
class ButtonImage(Button):
    def __init__(self, on_press, pos, size, size_img, source, allow_strech=False):
        super(ButtonImage, self).__init__(on_press=on_press, pos=pos, size=size, size_hint=(None, None),
                                          background_normal='images/scenery/transparency.png')
        self.add_widget(
            ImageWrap(pos=(pos[0] + (size[0] - size_img[0]) / 2.0, pos[1] + (size[1] - size_img[1]) / 2.0),
                      size=size_img,
                      source=source,
                      allow_stretch=allow_strech))

# transparent button with centered unstreched image wrapper
class ButtonImageText(Button):
    def __init__(self, on_press, pos, size, source_back, size_img, source, text, left, vAlignTop = False, font_size = sizes.font_size_large):
        super(ButtonImageText, self).__init__(on_press=on_press, pos=pos, size=size, size_hint=(None, None),
                                          background_normal='images/scenery/transparency.png')

        self.add_widget(
            ImageWrap(pos=pos,
                      size=size,
                      source=source_back))

        label = LabelWrap(pos=(pos[0], pos[1]),
                          size=(left, size[1]),
                          text=text,
                          hAlignLeft=True,
                          font_size=font_size,
                          vAlignTop = vAlignTop)
        self.add_widget(label)
        label.label.padding = (10, 0)

        self.add_widget(
            ImageWrap(pos=(pos[0] + left, pos[1] + (size[1] - size_img[1]) / 2.0),
                      size=size_img,
                      source=source))

class ButtonImageChoices(ButtonImage):
    def __init__(self, on_press, pos, text):
        size = (sizes.win_choice_width, sizes.win_choice_height)
        super(ButtonImageChoices, self).__init__(on_press=on_press, pos=pos, size=size, size_img=size,
                                                 source='images/scenery/fond_menu_choix_400x193px.png')

        self.add_widget(
            LabelWrap(pos=(pos[0], pos[1] + sizes.win_choice_height - sizes.win_choice_header),
                      size=(sizes.win_choice_width, sizes.win_choice_header),
                      text=text,
                      font_size=sizes.font_size_subtitle,
                      bold=True))

# for speach
class LabelWrap(Widget):
    def __init__(self, pos, size, text, font_size = sizes.font_size_default, bold=False, vAlignTop=False, hAlignLeft = False, padding = (0,0)):
        super(LabelWrap, self).__init__()
        self.label.pos = pos
        self.label.size = size
        self.label.padding = padding
        self.label.text = text.get()
        self.text = text
        self.bold = bold
        self.bolden()
        self.label.font_size = font_size
        if (vAlignTop):
            self.label.valign = 'top'
        if (hAlignLeft):
            self.label.halign = 'left'

    def bolden(self):
        if (self.bold):
            self.label.text = "[b]" + self.label.text + "[/b]"

    # update the text for category x/y (warning: categories start at 0)
    def update_cat(self, nb_current_category):
        self.label.text = self.text.get() + " " + str(nb_current_category + 1) + "/" + str(sizes.gauge_number + 1)
        self.bolden()
