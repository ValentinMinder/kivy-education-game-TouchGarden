from kivy.uix.label import Label
from kivy.uix.scatter import Scatter

import texts
import sizes
from gui import ImageWrap


class Category(object):
    def __init__(self, name, el1, el2, target):
        self.name = name
        self.element1 = el1
        self.element2 = el2
        self.target = target

class Recover(object):
    def __init__(self, positive, negative, solution=False, correction='images/scenery/transparency.png'):
        self.positive = positive
        self.negative = negative
        self.solution = solution
        self.correction = correction


# draggable element scatter (touchable by children)
class ElementScatter(Scatter):
    def __init__(self, name, positive, first, img):
        super(ElementScatter, self).__init__()
        self.name = name
        # disable other moves than translation (drag & drop)
        self.do_rotation = self.do_scale = False
        # to know wether positive or negative scenario should be activated
        self.positive = positive
        self.size_hint = (None, None)
        self.size = (sizes.width_left_elements, sizes.width_left_elements)
        self.image.source = img
        self.image.size = (sizes.width_left_images, sizes.width_left_images)
        self.image.pos = (sizes.border_small, sizes.border_small)
        # _orig to replace object at their correct original placement
        self.x_orig = sizes.width_border_left
        if (first):
            self.y_orig = sizes.height_left_first
        else:
            self.y_orig = sizes.height_left_second
        self.pos = (self.x_orig, self.y_orig)
        self.touch = True

    # detect the touch
    def on_bring_to_front(self, touch):
        print 'brought to front: '
        print self.positive
