# must be imported first to prevent issues
from kivy.animation import Animation
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image

Config.set('graphics', 'fullscreen', 'auto')  # set to 'auto' for production
Config.set('graphics', 'width', 1366)  # 1366
Config.set('graphics', 'height', 768)  # 768

Config.set('graphics', 'position', 'custom')  # 'auto'
Config.set('graphics', 'top', 0)
Config.set('graphics', 'left', 0)

Config.set('graphics', 'show_cursor', 0)
Config.set('graphics', 'borderless', 1)
Config.set('graphics', 'resizable', 0)

from kivy.app import App
from kivy.uix.button import Button

from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.core.text import LabelBase
from kivy.uix.behaviors import DragBehavior
import settings

# loading widget instructions
Builder.load_file('screens.kv')
Builder.load_file('widgets.kv')

# ease-of-access for the only screenmanager in use
MANAGER = None

# pre-load game music
music = SoundLoader.load("audio/garden_base.wav")

# Creating a backgroundable label (by default a blank background)
# http://robertour.com/2015/07/15/kivy-label-or-widget-with-background-color-property/
Builder.load_string("""
<LabelB>:
  background_color: 1,1,1,1
  canvas.before:
    Color:
      rgba: self.background_color
    Rectangle:
      pos: self.pos
      size: self.size
""")


class LabelB(Label):
    background_color = ListProperty([1, 1, 1, 1])


Factory.register('KivyB', module='LabelB')


# thanks  @Mathieu Virbel
# https://andnovar.wordpress.com/2011/08/03/kivy-label-with-background/
class LabelC(Label):
    pass


# for registering custom fonts
for font in settings.KIVY_FONTS:
    LabelBase.register(**font)


# for drag & drop texts (no image yet)
class DragLabel(DragBehavior, LabelB):
    pass


# for star-like buttons
class ButtonStar(Button):
    pass


# for category-like buttons
class ButtonCategory(Button):
    pass


# specialized version of screen that handles keyboard presses and has a cursor system,
# used for all the screens outside the loading screen
class KeyScreen(Screen):
    pass


class BackKeyScreen(KeyScreen):
    def __init__(self, previous, **kwargs):
        super(BackKeyScreen, self).__init__(**kwargs)

        # set previous screen for back button
        self.previous = previous

    # returns to previous screen
    def back(self):
        self.manager.switch_to(self.previous, direction='right')


class LoadingScreen(Screen):
    pass


# screen corresponding to the main menu
class MainMenuScreen(KeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_array = self.layout.children[:-1]
        self.cursor_reverse = True
        self.cursor_wrap = True

    # switches to the how to screen
    def test(self):
        self.manager.switch_to(TestScreen(name="Test", previous=self), direction='left')

    # switches to the training mode menu
    def game(self):
        self.manager.switch_to(GameScreen(name="Game", previous=self), direction='left')

    # switches to the training mode menu
    def floatgame(self):
        self.manager.switch_to(FloatGameScreen(name="Game", previous=self), direction='left')

    # switches to the training mode menu
    def animations(self):
        self.manager.switch_to(TestAnimationsScreen(name="TestAnimations", previous=self), direction='left')

    # switches to the training mode menu
    def graphics(self):
        self.manager.switch_to(TestGraphicsScreen(name="TestGraphics", previous=self), direction='left')

    # switches to the training mode menu
    def allgraphics(self):
        self.manager.switch_to(TestAllGraphicsScreen(name="TestGraphics", previous=self), direction='left')

    def stats(self):
        self.manager.switch_to(StatsScreen(name="Stats", previous=self), direction='left')


# "test" screen
class TestScreen(BackKeyScreen):
    # reference to back button for cursor use
    bback = ObjectProperty()
    # text contained on the screen, stored here for ease of reading
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)

        # cursor can only select back button
        self.cursor_array = [self.bback]
        self.cursor_wrap = True

        # main text for the screen
        self.text = "[i]italic [b]and[/i] bold[/b][b][color=ffffff]white[/color] [color=ff3333]red[/color] [/b][font=CorporativeSansRd]CorpSsRd[/font]"


# screen for picking training mode difficulty
class GameScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_array = self.layout.children[:-1]
        self.cursor_reverse = True
        self.cursor_wrap = True


# screen for testing graphics
class TestAnimationsScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(TestAnimationsScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_reverse = True
        self.cursor_wrap = True


# screen for testing graphics
class TestAllGraphicsScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(TestAllGraphicsScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_reverse = True
        self.cursor_wrap = True

    # switches to the training mode menu
    def moregraphics(self):
        self.manager.switch_to(TestMoreGraphicsScreen(name="TestGraphics", previous=self.previous), direction='left')


# screen for testing graphics
class TestMoreGraphicsScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(TestMoreGraphicsScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_reverse = True
        self.cursor_wrap = True


# screen for testing graphics
class TestGraphicsScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(TestGraphicsScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_reverse = True
        self.cursor_wrap = True


# screen for picking training mode difficulty
class StatsScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(StatsScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_array = self.layoutd.children[:-1]
        self.cursor_reverse = True
        self.cursor_wrap = True

    # switches to the how to screen
    def confirm(self):
        self.manager.switch_to(ConfirmStatsScreen(name="Test", previous=self.previous), direction='left')


# screen for picking training mode difficulty
class ConfirmStatsScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(ConfirmStatsScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_reverse = True
        self.cursor_wrap = True


# main application class
class TouchGardenApp(App):
    # changes window title
    title = "Interactive Touch Garden"

    def __init__(self, **kwargs):
        super(TouchGardenApp, self).__init__(**kwargs)

        # initialize new ScreenManager for handling screens, and set it as global for ease of use
        self.manager = ScreenManager()
        global MANAGER
        MANAGER = self.manager

    def build(self):
        # load and start playing game audio
        if music:
            music.loop = True
            music.play()

        # set starting screen
        self.manager.switch_to(MainMenuScreen(name="MainMenu"))
        return self.manager


# draggable element scatter
class ElementScatter(Scatter):
    def __init__(self, **kwargs):
        super(ElementScatter, self).__init__()

    # detect the touch
    def on_bring_to_front(self, touch):
        print 'brought to front: '
        print self.positive


# non-draggable image widget
class StaticImage(Label):
    def __init__(self, **kwargs):
        super(StaticImage, self).__init__()


margin_right = 242
height = 768


# float layout for draggable elements management
class FloatGameScreen(Screen):
    currentObj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(FloatGameScreen, self).__init__()
        client_frame = FloatLayout(size_hint=(1, 1))

        # garden background
        background = StaticImage()
        background.image.source = 'images/fond/fond_jardin_v4.png'
        background.image.pos = (margin_right, 0)
        background.image.size = (1024, 768)
        client_frame.add_widget(background)

        # todo: make target area + positive/negative elements selection dependant on category
        # target area to carry elements
        area = StaticImage()
        area.image.source = 'images/zones_de_depot/blocdepot_haie_gauche.png'
        area.image.pos = (margin_right, 0)
        area.image.size = (175, 175)
        client_frame.add_widget(area)

        # positive and negative elements to drag & drop
        # todo: check if disabling other touch than dragging
        # todo: automatize placement & original position
        positif = ElementScatter()
        positif.image.source = 'images/non_animes/haie_diverses_especes.png'
        positif.pos = (20, height - 1 * margin_right)
        positif.x_orig = 20
        positif.y_orig = height - 1 * margin_right
        positif.touch = True
        client_frame.add_widget(positif)

        negatif = ElementScatter()
        negatif.image.source = 'images/non_animes/haie_de_thuya.png'
        negatif.pos = (20, height - 2.5 * margin_right)
        negatif.x_orig = 20
        negatif.y_orig = height - 2.5 * margin_right
        negatif.positive = False
        negatif.touch = True
        client_frame.add_widget(negatif)

        # welcoming guy
        animated = StaticImage()
        animated.image.anim_delay = 0.1
        animated.image.anim_loop = 5
        animated.image.size = (75, 152)
        animated.image.pos = (790 + margin_right, 386)
        animated.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
        client_frame.add_widget(animated)

        # add main layout to root
        self.add_widget(client_frame)

    def on_touch_up(self, touch):
        element = self.currentObj
        print type(element)
        # react only to element scatter moves ended to right target area
        if (isinstance(element, ElementScatter) and element.touch):
            # todo automatize placement for detection, static image & animation
            if ((element.x >= margin_right - 175) & (element.x <= margin_right + 175)  # x placement with tolerance
                    & (element.y >= -175) & (element.y <= 175)):  # y placement with tolerance
                # put the real object in place
                static = StaticImage()
                static.image.source = element.image.source
                static.image.pos = (margin_right, 0)
                static.image.size = (175, 175)
                element.parent.add_widget(static)

                # animated guy: happy or not
                animated = StaticImage()
                animated.image.anim_delay = 0.1
                animated.image.anim_loop = 5
                animated.image.size = (75, 152)
                animated.image.pos = (790 + margin_right, 386)
                if (element.positive):
                    animated.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
                else:
                    # TODO: put the negative animation, remove the placement, remove the non-moving guy
                    animated.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
                    animated.image.pos = (890 + margin_right, 186)

                element.parent.add_widget(animated)

                # points

                points = ElementScatter()
                if (element.positive):
                    points.image.source = 'images/plus_green.png'
                else:
                    points.image.source = 'images/minus_red.png'
                points.pos = (175 / 2 + margin_right, 175 / 2)
                element.parent.add_widget(points)
                anim_points = Animation(x=1500, y=500, duration=2)
                if (element.positive):
                    points.image.size = (100, 100)
                    anim_points &= Animation(size=(700, 700))
                else:
                    points.image.size = (600, 600)
                    anim_points &= Animation(size=(100, 100))
                anim_points.start(points.image)

                # animation of animals
                # TODO: real animals!
                animal = ElementScatter()
                animal.image.anim_delay = 0.1
                animal.image.size = (75, 152)
                animal.pos = (0 + margin_right, 768)
                animal.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
                element.parent.add_widget(animal)
                anim = Animation(x=175 / 2 + margin_right, y=175 / 2, duration=1)
                if (element.positive):
                    anim += Animation(x=1024 + 200 + margin_right, y=212, duration=2)
                else:
                    anim += Animation(x=0 + margin_right, y=768, duration=1)
                anim.start(animal)
                # todo: remove the animal or make sure it disappear
                # element.parent.remove_widget(animal)

                anim_wid = Animation(x=element.x_orig, y=element.y_orig - 200)
                anim_wid.start(element)

                # todo: always remove the widget
                # todo: why does selection doesn't work well ??
                if (not element.positive):
                    element.parent.remove_widget(element)
                self.currentObj = ObjectProperty(None)

                # todo : disable all other widget!
                # todo: move to text info + other category, after a while

                print 'placed scatter'
            else:
                anim = Animation(x=element.x_orig, y=element.y_orig)
                anim.start(element)
                print 'not placed'
                self.currentObj = ObjectProperty(None)


# launch the app
if __name__ == '__main__':
    TouchGardenApp().run()
