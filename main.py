# coding=utf-8
# must be imported first to prevent issues
from PIL import Image
from kivy.animation import Animation
from kivy.config import Config
from kivy.core.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image

from kivy.uix.widget import Widget

from utils import sizes
from utils.category import ElementScatter, AnimatedScatter, Category, Recover
from utils.gui import StaticImage, ButtonImage, ButtonImageChoices, LabelWrap

# Config.set('graphics', 'fullscreen', 'auto')  # set to 'auto' for production
Config.set('graphics', 'width', sizes.width)  # 1366
Config.set('graphics', 'height', sizes.height)  # 768

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
from utils.texts import *

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


# for speach
class SpeachLabel(Widget):
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


# float layout for draggable elements management
class FloatGameScreen(BackKeyScreen):
    currentObj = ObjectProperty(None)
    points = 0

    def __init__(self, **kwargs):
        super(FloatGameScreen, self).__init__(**kwargs)
        client_frame = FloatLayout(size_hint=(1, 1))
        # garden background
        left_bg = StaticImage(pos=(sizes.width_ref, sizes.height_ref),
                              size=(sizes.width_left_margin, sizes.height),
                              src='images/scenery/nav_fond_gauche_200x768px.png')
        client_frame.add_widget(left_bg)

        background = StaticImage(pos=(sizes.width_left_margin, sizes.height_ref),
                                 size=(sizes.width_game, sizes.height),
                                 src='images/fond/fond_jardin_v4.png')
        client_frame.add_widget(background)
        right_bg = StaticImage(pos=(sizes.width_right_game, sizes.height_ref),
                               size=(sizes.width_right_margin, sizes.height),
                               src='images/scenery/nav_fond_droite_142x768px.png')
        client_frame.add_widget(right_bg)

        # smiles and gscale (gauge)
        smile_pos = StaticImage(pos=(sizes.gauge_smiley_left, sizes.gauge_smiley_top),
                                size=(29, 29),
                                src='images/scenery/smile_positif_210x200px.png')
        client_frame.add_widget(smile_pos)

        smile_neg = StaticImage(pos=(sizes.gauge_smiley_left, sizes.gauge_smiley_bottom),
                                size=(29, 29),
                                src='images/scenery/smile_negatif_210x200px.png')
        client_frame.add_widget(smile_neg)

        scale = StaticImage(pos=(sizes.gauge_left_margin, sizes.gauge_bottom_margin),
                            size=(77, 459),
                            src='images/scenery/score_77x459px.png')
        client_frame.add_widget(scale)

        # colored score gauge
        self.gauge = StaticImage(pos=(sizes.gauge_left_start, sizes.gauge_bottom_start),
                            size=(sizes.gauge_width, sizes.gauge_height(sizes.gauge_number)),
                            src='images/scenery/score_vert.png')
        self.gauge.image.allow_stretch = True
        self.gauge.image.keep_ratio = False
        client_frame.add_widget(self.gauge)

        #cursor
        self.cursor = StaticImage(pos=(sizes.cursor_left, sizes.cursor_pos_y(sizes.gauge_number)),
                            size=(38, 20),
                            src='images/scenery/curseur_38x20px.png')
        client_frame.add_widget(self.cursor)

        #todo: add this to demo /tuto
        anim = Animation(y = sizes.cursor_pos_y(0), duration=1)
        anim += Animation(y=sizes.cursor_pos_y(2 * sizes.gauge_number), duration=2)
        anim += Animation(y=sizes.cursor_pos_y(sizes.gauge_number), duration=1)
        anim.start(self.cursor.image)

        cat_scale = StaticImage(pos=(sizes.border_small + 2, sizes.height_button_small + sizes.border_small),
                            size=(sizes.category_width, sizes.category_height),
                            src='images/scenery/niveau_avancement_186x23px.png')
        client_frame.add_widget(cat_scale)

        #todo: handle correctly category numbers
        self.categorynb = 1
        # colored score gauge
        self.category_scale = StaticImage(pos=(sizes.border_small, sizes.height_button_small + sizes.border_small),
                                 size=(sizes.category_width_progress(self.categorynb), sizes.category_height),
                                 src='images/scenery/niveau_avancement_curseur.png')
        self.category_scale.image.allow_stretch = True
        self.category_scale.image.keep_ratio = False
        client_frame.add_widget(self.category_scale)



        button_next = ButtonImage(on_press=self.category_forward,
                                  pos=(sizes.width_ref, sizes.border_small),
                                  size=(sizes.width_left_margin, sizes.height_button_small),
                                  size_img=(75, 44),
                                  src="images/scenery/fleche_suite_75x44px.png")
        client_frame.add_widget(button_next)

        button_stop = ButtonImage(on_press=self.stop_game,
                                  pos=(sizes.width_right_game, sizes.border_small),
                                  size=(sizes.width_right_margin, sizes.height_button_small),
                                  size_img=(57, 57),
                                  src="images/scenery/bouton_eteindre_200x200px.png")
        client_frame.add_widget(button_stop)

        positif = ElementScatter(name=Text("fr", "de", "en"), positive=True, first=True,
                                 img='images/non_animes/haie_diverses_especes.png')
        negatif = ElementScatter(name=Text("fr", "de", "en"), positive=False, first=False,
                                 img='images/non_animes/haie_de_thuya.png')

        target = StaticImage(pos=(sizes.width_left_margin, 0),
                             size=(175, 175),
                             src='images/zones_de_depot/blocdepot_haie_gauche.png')
        category = Category(name=Text("fr", "de", "en"), el1=positif, el2=negatif, target=target)

        # welcoming guy
        animated = StaticImage(pos=(790 + sizes.width_left_margin, 386), size=(75, 152),
                               src='images/animations/bonhomme/homme_positif_content_2.gif')
        animated.image.anim_delay = 0.1
        animated.image.anim_loop = 5
        client_frame.add_widget(animated)

        self.speach = speach = SpeachLabel()
        speach.label.text = txt_tutorial_welcome()
        speach.label.pos = (1366 - 364, 768 - 170)
        speach.label.size = (200, 150)
        client_frame.add_widget(speach)

        score_text = LabelWrap(size=(sizes.width_right_margin, sizes.height_button_small),
                               pos = (sizes.width_right_game, sizes.height_left_category_title),
                               text=Text(fr='Score', de = 'TODE', en='Score'),
                               font_size=28, bold=True)
        client_frame.add_widget(score_text)

        self.category_text = LabelWrap(size=(sizes.width_left_margin, sizes.height_left_category_element),
                                          pos=(sizes.width_ref, sizes.height_left_category_title),
                                          text=Text(fr='Catégorie', de='TODE', en='Category'),
                                          font_size=sizes.font_size_subtitle, bold=True)
        client_frame.add_widget(self.category_text)
        self.category_text.update_cat(1)

        self.category_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_left_category_element),
                                       pos=(sizes.border_text_min, sizes.height_left_category_desc),
                                       text=Text(fr="IiiiiiiiIiiiiiiiiIiiiiiiiiiiiiiiiiiiiIiiIIi (mock)", de='TODE', en='TOEN'),
                                       font_size=sizes.font_size_large)
        client_frame.add_widget(self.category_desc)

        #nice ui elements
        f1 = StaticImage(pos=(sizes.width_border_left, sizes.height_left_category_title - sizes.border_small),
                             size=(sizes.width_left_elements, sizes.border_small),
                             src='images/scenery/filet_souligne_144x6px.png')
        f2 = StaticImage(pos=(sizes.width_right_game + sizes.width_border_left, sizes.height_left_category_title - sizes.border_small),
                         size=(sizes.width_right_margin - 2 * sizes.width_border_left, sizes.border_small),
                         src='images/scenery/filet_souligne_144x6px.png')
        f2.image.allow_stretch = True
        f2.image.keep_ratio = False
        f3 = StaticImage(pos=(sizes.width_border_left, sizes.height_left_category_desc - sizes.border_small),
                         size=(sizes.width_left_elements, sizes.border_small),
                         src='images/scenery/filet_souligne_144x6px.png')
        client_frame.add_widget(f1)
        client_frame.add_widget(f2)
        client_frame.add_widget(f3)

        # textual description elements
        self.elem_first_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_title),
                               pos=(sizes.border_text_min, sizes.height_left_first_desc),
                               text=Text(fr="Haies d'espèces natives IiiiiiiIiiiiiIiiiiiiiiiiiiii 3rd and last line I", de='TODE', en='TOEN'),
                               vAlignTop=True)
        client_frame.add_widget(self.elem_first_desc)

        self.elem_second_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_title),
                                    pos=(sizes.border_text_min, sizes.height_left_second_desc),
                                    text=Text(fr="Haie homogène Iiiiiiiiiiii", de='TODE', en='TOEN'),
                                    vAlignTop=True)
        client_frame.add_widget(self.elem_second_desc)

        elem_first_frame = StaticImage(size=(sizes.width_left_elements, sizes.width_left_elements),
                                    pos=(sizes.width_border_left, sizes.height_left_first),
                                    src='images/scenery/fond_menu_gauche_144x144px.png')
        client_frame.add_widget(elem_first_frame)

        elem_second_frame = StaticImage(size=(sizes.width_left_elements, sizes.width_left_elements),
                                    pos=(sizes.width_border_left, sizes.height_left_second),
                                    src='images/scenery/fond_menu_gauche_144x144px.png')
        client_frame.add_widget(elem_second_frame)

        # add main layout to root
        self.add_widget(client_frame)

        self.frame = client_frame
        self.gameturn_setup(category)

    def category_forward(self, touch):
        if (self.categorynb < sizes.category_number):
            self.speach.label.text = txt_game_move_pass()
            self.anim_points(0, 0, 0, self.category_next)
        else:
            self.category_next(touch)

    def category_next(self, screen):
        if (self.categorynb >= sizes.category_number):
            print 'TODO: end of game, see results before leaving'
            self.back()
        category = self.current_category
        #todo: reactivate , just easier to test
        #self.frame.remove_widget(category.target)
        #self.frame.remove_widget(category.element1)
        #self.frame.remove_widget(category.element2)

        self.categorynb += 1

        self.category_scale.image.size = (sizes.category_width_progress(self.categorynb), sizes.category_height)
        self.category_text.update_cat(self.categorynb)
        self.category_desc.label.text = "blo"
        self.elem_first_desc.label.text = "bli"
        self.elem_second_desc.label.text = "bla"


        print 'TODO: add new category'

    # does nothing, used for no action after animation
    def none(self):
        pass

    # animates a smile/a points mark towards scale from the happening area
    # todo: choose if points or smiles
    def anim_points(self, points, x_start, y_start, fct_next=none):
        size = 50
        size_final = 200
        x_final = sizes.width - size_final
        y_final = (sizes.height - size_final) / 2
        y_shift = 300
        points_image = StaticImage(size=(size, size),
                                   pos=(x_start, y_start),
                                   src='images/scenery/points_neutre_500x500px.png')
        if (points > 0):
            points_image.image.source = 'images/scenery/smile_positif_210x200px.png'
            y_final += y_shift
        elif (points < 0):
            points_image.image.source = 'images/scenery/points_negatif_500x500px.png'
            y_final -= y_shift

        self.frame.add_widget(points_image)

        def remove(anim, widget):
            self.frame.remove_widget(points_image)
            fct_next(self)

        d = 3
        anim_points = Animation(size=(size_final, size_final), duration=d)
        anim_points &= Animation(x=x_final, y=y_final, duration=d, t='in_quad')
        anim_points.bind(on_complete=remove)
        anim_points.start(points_image.image)


    def stop_game(self, touch):
        print 'TODO: ask confirmation to reset/stop game'
        self.back()

    #update the cursor placement and gauge filling/color depending on points
    def update_cursor(self):
        anim = Animation(y=sizes.cursor_pos_y(self.points + sizes.gauge_number), duration=1)
        anim.start(self.cursor.image)
        self.gauge.image.size = (sizes.gauge_width, sizes.gauge_height(self.points + sizes.gauge_number))
        if (self.points >= 0):
            self.gauge.image.source= 'images/scenery/score_vert.png'
        else:
            self.gauge.image.source = 'images/scenery/score_rouge.png'

    # setup for category game turn
    # todo: tear down
    def gameturn_setup(self, category):
        self.current_category = category

        # target area to carry elements
        self.frame.add_widget(category.target)

        # positive and negative elements to drag & drop
        self.frame.add_widget(category.element1)
        self.frame.add_widget(category.element2)

    def on_touch_up(self, touch):
        element = self.currentObj
        print type(element)
        target = self.current_category.target
        # react only to element scatter moves ended to right target area
        if (isinstance(element, ElementScatter) and element.touch):
            # todo automatize placement for detection, static image & animation
            # check collision
            if (target.image.collide_widget(element)):
                # put the real object in place
                static = StaticImage(pos=(sizes.width_left_margin, 0), size=(175, 175), src=element.image.source)
                element.parent.add_widget(static)
                self.static = static

                # remove the target
                self.frame.remove_widget(self.current_category.target)

                # text speach update
                if (not element.positive):
                    self.speach.label.text = txt_game_move_negative()
                else:
                    self.speach.label.text = txt_game_move_positive()

                # animated guy: happy or not
                animated = StaticImage(pos=(790 + sizes.width_left_margin, 386), size=(75, 152),
                                       src='images/animations/bonhomme/homme_positif_content_2.gif')
                animated.image.anim_delay = 0.1
                animated.image.anim_loop = 5
                if (element.positive):
                    animated.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
                else:
                    # TODO: put the negative animation, remove the placement, remove the non-moving guy
                    animated.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
                    animated.image.pos = (890 + sizes.width_left_margin, 186)

                element.parent.add_widget(animated)


                # animation of animals
                # TODO: real animals!
                animal = AnimatedScatter()
                animal.image.anim_delay = 0.1
                animal.image.size = (75, 152)
                animal.pos = (0 + sizes.width_left_margin, 768)
                animal.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
                element.parent.add_widget(animal)
                anim = Animation(x=175 / 2 + sizes.width_left_margin, y=175 / 2, duration=1)
                if (element.positive):
                    anim += Animation(x=1024 + 200 + sizes.width_left_margin, y=212, duration=2)
                else:
                    anim += Animation(x=0 + sizes.width_left_margin, y=768, duration=1)
                anim.start(animal)
                # todo: remove the animal or make sure it disappear
                # element.parent.remove_widget(animal)

                anim_wid = Animation(x=element.x_orig, y=element.y_orig)
                anim_wid.start(element)

                # todo: always remove the widget
                # todo: why does selection doesn't work well ??
                #if (not element.positive):
                 #   element.parent.remove_widget(element)
                self.currentObj = ObjectProperty(None)

                if (element.positive):
                    self.points += 1
                else:
                    self.points -= 1


                # todo : disable all other widget!
                # todo: move to text info + other category, after a while

                def after(screen):
                    self.update_cursor()
                    self.frame.remove_widget(animal)
                    self.frame.remove_widget(animated)
                    if (element.positive):
                        self.category_next(None)
                    else:
                        self.after_negative()
                # points
                m = 1 if element.positive else -1
                self.anim_points(m, 175 / 2 + sizes.width_left_margin, 175 / 2, fct_next=after)

                print 'placed scatter'
            else:
                anim = Animation(x=element.x_orig, y=element.y_orig)
                anim.start(element)
                self.speach.label.text = txt_game_move_unreached()
                print 'not placed'
                self.currentObj = ObjectProperty(None)

    def after_negative(self):
        print 'negative'

        def x(_x):
            return _x + sizes.win_dx
        def y (_y):
            return _y + sizes.win_dy

        window_frame = FloatLayout(size_hint=(1, 1), pos=(0,0))

        window_frame.add_widget(StaticImage(
            pos=(x(-2), y(-22)),
            size=(923, 624),
            src='images/scenery/fenetre_infos_923x624px.png'))

        window_frame.add_widget(StaticImage(pos=(x(0), y(sizes.win_height - sizes.win_header)),
                            size=(sizes.win_width, sizes.win_header),
                            src='images/scenery/bandeau_gris_fenetre_choix_898x80px.png'))

        window_frame.add_widget(
            LabelWrap(pos=(x(0), y(sizes.win_height - sizes.win_header)),
                      size=(sizes.win_width - sizes.win_width_infos, sizes.win_header),
                      text=Text(fr="Ce n'est pas le bon choix...", de= "TODE", en="TOEN"),
                      font_size=sizes.font_size_title,
                      bold=True))

        # todo: separate the text for internationalizazion !
        window_frame.add_widget(ButtonImage(
            on_press=self.more_infos, pos=(x(sizes.win_width - sizes.win_width_infos), y(sizes.win_height - sizes.win_header)),
                            size=(sizes.win_width_infos, sizes.win_header),
                            size_img=(sizes.win_width_infos, sizes.win_header),
                            src='images/scenery/bouton_plus_d_infos_183x80px.png'))

        #todo: react to clicks
        def replace(screen):
            print 'replace'
            self.points += 2


            self.static.image.source = 'images/non_animes/haie_diverses_especes.png'


            #todo: better
            animal = AnimatedScatter()
            animal.image.anim_delay = 0.1
            animal.image.size = (75, 152)
            animal.pos = (0 + sizes.width_left_margin, 768)
            animal.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
            self.frame.add_widget(animal)
            anim = Animation(x=175 / 2 + sizes.width_left_margin, y=175 / 2, duration=1)
            anim += Animation(x=1024 + 200 + sizes.width_left_margin, y=212, duration=2)
            anim.start(animal)

            self.anim_points(1, 175 / 2 + sizes.width_left_margin, 175 / 2, fct_next=self.category_next)
            after_all_choices()

        def remove(screen):
            print 'TODO: remove the object'
            self.frame.remove_widget(self.static)
            self.points += 1
            after_all_choices()
            self.category_forward(None)

        def keep(screen):
            print 'keep'
            after_all_choices()
            self.category_next(None)

        def correct(screen):
            print 'correct'
            self.points += 2

            #todo: correction, instead, in right position
            self.static.image.source = 'images/non_animes/haie_diverses_especes.png'
            self.static.image.pos = (400,0)

            # todo: better
            animal = AnimatedScatter()
            animal.image.anim_delay = 0.1
            animal.image.size = (75, 152)
            animal.pos = (0 + sizes.width_left_margin, 768)
            animal.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
            self.frame.add_widget(animal)
            anim = Animation(x=175 / 2 + sizes.width_left_margin, y=175 / 2, duration=1)
            anim += Animation(x=1024 + 200 + sizes.width_left_margin, y=212, duration=2)
            anim.start(animal)

            self.anim_points(1, 175 / 2 + sizes.width_left_margin, 175 / 2, fct_next=self.category_next)
            after_all_choices()

        def after_all_choices():
            self.frame.remove_widget(window_frame)
            self.update_cursor()

        class ButtonImageChoicesKeep(ButtonImageChoices):
            def __init__(self, recover):
                pos = (x(sizes.win_choice_left), y(sizes.win_choice_down))
                text = Text("Garder", "TODE", "TOEN")
                super(ButtonImageChoicesKeep, self).__init__(keep, pos, text)

                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src=recover.negative))


        class ButtonImageChoicesRemove(ButtonImageChoices):
            def __init__(self, recover):
                pos = (x(sizes.win_choice_right), y(sizes.win_choice_up))
                text = Text(fr="Enlever", de="TODE", en="TOEN")
                super(ButtonImageChoicesRemove, self).__init__(remove, pos, text)

                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src=recover.negative))
                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src='images/scenery/picto_croix_112x112px.png'))


        class ButtonImageChoicesReplace(ButtonImageChoices):
            def __init__(self, recover):
                pos = (x(sizes.win_choice_left), y(sizes.win_choice_up))
                text = Text("Remplacer", "TODE", "TOEN")
                super(ButtonImageChoicesReplace, self).__init__(replace, pos, text)

                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src='images/scenery/fleche_seule_23x44px.png'))
                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src=recover.negative))
                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src='images/scenery/picto_croix_112x112px.png'))
                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_right, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src=recover.positive))

        class ButtonImageChoicesCorrect(ButtonImageChoices):
            def __init__(self, recover):
                pos = (x(sizes.win_choice_right), y(sizes.win_choice_down))
                text = Text("Corriger", "TODE", "TOEN")
                super(ButtonImageChoicesCorrect, self).__init__(correct, pos, text)

                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src='images/scenery/fleche_seule_23x44px.png'))
                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src=recover.negative))
                self.add_widget(
                    StaticImage(pos=(pos[0] + sizes.win_choice_inner_right, pos[1] + sizes.win_choice_inner_margin),
                                size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                                src=recover.correction))

        #initiate a correct recover
        recover = Recover('images/non_animes/haie_diverses_especes.png', 'images/non_animes/haie_de_thuya.png', True, 'images/non_animes/haie_de_thuya.png')
        window_frame.add_widget(ButtonImageChoicesReplace(recover))
        window_frame.add_widget(ButtonImageChoicesRemove(recover))
        window_frame.add_widget(ButtonImageChoicesKeep(recover))
        if (recover.solution):
            window_frame.add_widget(ButtonImageChoicesCorrect(recover))

        self.frame.add_widget(window_frame)
        pass

    def more_infos(self, screen):
        print 'know more'



# launch the app
if __name__ == '__main__':
    TouchGardenApp().run()
