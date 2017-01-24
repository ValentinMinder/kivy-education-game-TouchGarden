from kivy.uix.label import Label
from kivy.uix.scatter import Scatter

import texts
import sizes


class Category(object):
    def __init__(self, name, el1, el2, target):
        self.name = name
        self.element1 = el1
        self.element2 = el2
        self.target = target


# animated scatter element
#  todo: check disabling all touch
class AnimatedScatter(Scatter):
    def __init__(self):
        super(AnimatedScatter, self).__init__()


# draggable element scatter (touchable by children)
# todo: check if disabling other touch than dragging
class ElementScatter(Scatter):
    def __init__(self, name, positive, first, img):
        super(ElementScatter, self).__init__()
        self.name = name
        # to know wether positive or negative scenario should be activated
        self.positive = positive
        self.image.source = img
        # _orig to replace object at their correct original placement
        self.x_orig = sizes.border_margin
        if (first):
            self.y_orig = sizes.height - sizes.height_left_margin
        else:
            print sizes.height - sizes.height_left_margin - sizes.height_left_elements
            self.y_orig = sizes.height - sizes.height_left_margin - sizes.height_left_elements
        self.pos = (self.x_orig, self.y_orig)
        self.touch = True

    # detect the touch
    def on_bring_to_front(self, touch):
        print 'brought to front: '
        print self.positive
