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
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget

from utils import sizes
from utils.quiz import Quiz
from utils.category import ElementScatter, AnimatedScatter, Category, Recover
from utils.gui import ImageWrap, ButtonImage, ButtonImageChoices, LabelWrap

#Config.set('graphics', 'fullscreen', 'auto')  # set to 'auto' for production
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


# for star-like buttons
class ButtonStar(ToggleButton):
    # on press, toogle all previous stars and untoggle following
    def on_press(self):
        self.parent.parent.parent.check(self)


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

    def start(self):
        self.manager.switch_to(StartScreen(name="Start", previous=self), direction='left')


# start screen to choose language and see credits
class StartScreen(BackKeyScreen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        self.cursor_array = self.layout.children[:-1]
        self.cursor_reverse = True
        self.cursor_wrap = True

    def french(self):
        lang.current = lang.fr
        self.forward()

    def german(self):
        lang.current = lang.de
        self.forward()

    def english(self):
        lang.current = lang.en
        self.forward()

    def forward(self):
        self.manager.switch_to(FloatGameScreen(name="Game", previous=self), direction='left')


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
    max = 5

    def __init__(self, **kwargs):
        super(StatsScreen, self).__init__(**kwargs)

        def add_star(widget):
            widget.add_widget(Label())
            for i in range(1, self.max + 1):
                bs = ButtonStar()
                bs.text = bs.id = str(i)
                widget.add_widget(bs)
                widget.add_widget(Label())

        add_star(self.star_fr)
        add_star(self.star_de)

    def check(self, btn):
        print btn
        print btn.id
        nb = int(btn.id)
        self.rate = nb

        def check_star(widget):
            for i in widget.children:
                if (i.id):
                    if int(i.id) <= nb:
                        i.state = 'down'
                    else:
                        i.state = 'normal'
                        anim = Animation(x=2000, duration=1)
                        anim.start(i)


                    # todo: choos if anim should forward
                    if (int(i.id) == self.max):
                        anim = Animation(duration=3)
                        anim.bind(on_complete=self.forward_)
                        anim.start(i)

        check_star(self.star_fr)
        check_star(self.star_de)
        self.vde.disabled = False
        self.vfr.disabled = False

    def validate_fr(self):
        lang.current = lang.fr
        self.forward()

    def validate_de(self):
        lang.current = lang.de
        self.forward()

    def forward_(self, a, b):
        print a
        print b
        self.forward()

    def forward(self):
        self.manager.switch_to(ContestIntroScreen(name="Game", previous=self), direction='left')


class QuestionWidget(BoxLayout):
    def __init__(self, q, image=False):
        super(QuestionWidget, self).__init__()
        self.question = q
        self.q.text = q.question.get()
        self.selected = -1
        i = q.replies.__len__() - 1
        while (i >= 0):
            t = ToggleButton(on_press=self.reply, id=str(i), group="question",
                         background_color=color.back_grey)
            self.r.add_widget(t)
            if image:
                self.q.size_hint = 1, 0.2
                self.size_hint = 1, 4
                im = Image(source=q.replies[i].text)
                t.add_widget(im)

                def upos(b, c):
                    b.children[0].pos = c

                def usize(b, c):
                    b.children[0].size = c

                t.bind(pos=upos)
                t.bind(size=usize)
            else:
                t.text=q.replies[i].text.get()
            i -= 1

    def done(self):
        return (self.selected != -1)

    def reply(self, btn):
        nb = int(btn.id)
        if (self.done()):
            self.r.children[self.selected].background_color = color.back_grey
        self.selected = nb
        btn.background_color = color.back_selected
        self.parent.parent.parent.check()

    def correct(self):
        nb = self.selected
        if (nb != -1):
            if (self.question.replies[nb].is_correct):
                self.r.children[nb].background_color = color.back_green
                return True
            else:
                self.r.children[nb].background_color = color.back_magenta
        return False

    def block(self):
        for child in self.r.children:
            child.disabled = True


# screen for picking training mode difficulty
class ContestIntroScreen(BackKeyScreen):
    def __init__(self, **kwargs):
        super(ContestIntroScreen, self).__init__(**kwargs)

        quiz = Quiz()
        q = quiz.question_public_img
        im = QuestionWidget(q, image=True)
        self.l.add_widget(im)

    def check(self):
        self.forward()

    def forward(self):
        self.manager.switch_to(ContestScreen(name="Contest", previous=self.previous), direction='left')


# screen for picking training mode difficulty
class ContestScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(ContestScreen, self).__init__(**kwargs)

        # cursor options
        self.cursor_reverse = True
        self.cursor_wrap = True

        layout = BoxLayout(orientation='vertical', size_hint=(1, 1), padding=10, spacing=10)
        self.add_widget(layout)

        layout.add_widget(
            Label(text='Tu peux maintenant participer au concours en répondant correctement à quelques sur l\'exposition',
                  size_hint=(1, 0.2)))

        self.qlayout = qlayout = BoxLayout(orientation='vertical', size_hint=(1, 1), spacing=10)

        self.quiz = Quiz()
        qlayout.add_widget(QuestionWidget(self.quiz.question_public))
        for qi in self.quiz.question_images:
            im = QuestionWidget(qi, image=True)
            qlayout.add_widget(im)
        for qq in self.quiz.questions:
            qw = QuestionWidget(qq)
            qlayout.add_widget(qw)

        layout.add_widget(qlayout)

        self.btn_submit = btn = Button(text="répondre d'abord à toutes les questions", size_hint=(1, 0.1),
                                       background_normal='', background_down='')
        btn.disabled = True
        btn.background_color = color.back_grey

        def erase():
            self.back()

        def submit():
            all_correct = True
            for qq in self.qlayout.children:
                all_correct &= qq.correct()
                qq.block()
            if all_correct:
                btn.background_color = color.back_green
                btn.text = "Bravo, vous avez répondu correctement, vous allez participer au tirage au sort."
            else:
                btn.background_color = color.back_magenta
                btn.text = "Quelques erreurs, malheureusement... à bientôt"
                # todo: after timeout, move to start screen

            btn.on_press = erase

        btn.on_press = submit
        layout.add_widget(btn)

    def check(self):
        done = True
        for q in self.qlayout.children:
            done &= q.done()
        if done:
            self.btn_submit.disabled = False
            self.btn_submit.text = "Appuyer pour vérifier, lorsque tu es prêt."


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


class ImageF(Image):
    pass


# float layout for draggable elements management
class FloatGameScreen(BackKeyScreen):
    currentObj = ObjectProperty(None)
    points = 0

    def __init__(self, **kwargs):
        super(FloatGameScreen, self).__init__(**kwargs)
        self.quiz = Quiz()

        # todo: handle correctly category numbers
        self.categorynb = 1

        self.frame = FloatLayout(size_hint=(1, 1))
        self.init_static_UI()
        self.init_dynamic_UI()

        # add main layout to root
        self.add_widget(self.frame)

        # init categories and game
        self.init_welcome_tuto()
        self.init_category_struct()

    # create and add all static UI elements (non-movable, non-changeable, only background and scenery)
    def init_static_UI(self):
        f = self.frame

        # garden background and large borders left/right
        f.add_widget(ImageWrap(pos=(sizes.width_ref, sizes.height_ref),
                               size=(sizes.width_left_margin, sizes.height),
                               source='images/scenery/nav_fond_gauche_200x768px.png'))
        f.add_widget(ImageWrap(pos=(sizes.width_left_margin, sizes.height_ref),
                               size=(sizes.width_game, sizes.height),
                               source='images/fond/fond_jardin_v5-3.jpg'))
        f.add_widget(ImageWrap(pos=(sizes.width_right_game, sizes.height_ref),
                               size=(sizes.width_right_margin, sizes.height),
                               source='images/scenery/nav_fond_droite_142x768px.png'))

        f.add_widget(ImageWrap(pos=sizes.table_pos,
                               size=(130, 119),
                               source='images/non_animes/table_chaise_de_jardin.png'))

        # right elements
        # smiles and points scale (gauge)
        f.add_widget(ImageWrap(pos=(sizes.gauge_left_margin, sizes.gauge_bottom_margin),
                               size=(77, 459),
                               source='images/scenery/score_77x459px.png'))
        f.add_widget(ImageWrap(pos=(sizes.gauge_smiley_left, sizes.gauge_smiley_top),
                               size=(29, 29),
                               source='images/scenery/smile_positif_210x200px.png'))
        f.add_widget(ImageWrap(pos=(sizes.gauge_smiley_left, sizes.gauge_smiley_bottom),
                               size=(29, 29),
                               source='images/scenery/smile_negatif_210x200px.png'))

        # left elements
        f.add_widget(ImageWrap(pos=(sizes.border_small + 2, sizes.height_button_small + sizes.border_small),
                               size=(sizes.category_width, sizes.category_height),
                               source='images/scenery/niveau_avancement_186x23px.png'))

        # buttons
        f.add_widget(ButtonImage(on_press=self.category_forward,
                                 pos=(sizes.width_ref, sizes.border_small),
                                 size=(sizes.width_left_margin, sizes.height_button_small),
                                 size_img=(75, 44),
                                 src="images/scenery/fleche_suite_75x44px.png"))
        f.add_widget(ButtonImage(on_press=self.stop_game,
                                 pos=(sizes.width_right_game, sizes.border_small),
                                 size=(sizes.width_right_margin, sizes.height_button_small),
                                 size_img=(57, 57),
                                 src="images/scenery/bouton_eteindre_200x200px.png"))

        # nice ui elements
        f.add_widget(ImageWrap(pos=(sizes.width_border_left, sizes.height_left_category_title - sizes.border_small),
                               size=(sizes.width_left_elements, sizes.border_small),
                               source='images/scenery/filet_souligne_144x6px.png'))
        f.add_widget(ImageWrap(pos=(
            sizes.width_right_game + sizes.width_border_left, sizes.height_left_category_title - sizes.border_small),
            size=(sizes.width_right_margin - 2 * sizes.width_border_left, sizes.border_small),
            source='images/scenery/filet_souligne_144x6px.png',
            allow_stretch=True,
            keep_ratio=False)
        )
        f.add_widget(ImageWrap(pos=(sizes.width_border_left, sizes.height_left_category_desc - sizes.border_small),
                               size=(sizes.width_left_elements, sizes.border_small),
                               source='images/scenery/filet_souligne_144x6px.png'))

        f.add_widget(ImageWrap(size=(sizes.width_left_elements, sizes.width_left_elements),
                               pos=(sizes.width_border_left, sizes.height_left_first),
                               source='images/scenery/fond_menu_gauche_144x144px.png'))
        f.add_widget(ImageWrap(size=(sizes.width_left_elements, sizes.width_left_elements),
                               pos=(sizes.width_border_left, sizes.height_left_second),
                               source='images/scenery/fond_menu_gauche_144x144px.png'))

        f.add_widget(LabelWrap(size=(sizes.width_right_margin, sizes.height_button_small),
                               pos=(sizes.width_right_game, sizes.height_left_category_title),
                               text=Text(fr='Score', de='TODE', en='Score'),
                               font_size=sizes.font_size_subtitle, bold=True))

    # create and add all dynamic UI elements (some movable, some resizabée, some text or image changeable, no background, some scenery)
    def init_dynamic_UI(self):
        f = self.frame

        # colored score gauge
        self.gauge = ImageWrap(pos=(sizes.gauge_left_start, sizes.gauge_bottom_start),
                               size=(sizes.gauge_width, sizes.gauge_height(sizes.gauge_number)),
                               source='images/scenery/score_vert.png',
                               allow_stretch=True,
                               keep_ratio=False)
        f.add_widget(self.gauge)

        # cursor
        self.cursor = ImageWrap(pos=(sizes.cursor_left, sizes.cursor_pos_y(sizes.gauge_number)),
                                size=(38, 20),
                                source='images/scenery/curseur_38x20px.png')
        f.add_widget(self.cursor)

        # colored score gauge
        self.category_scale = ImageWrap(pos=(sizes.border_small, sizes.height_button_small + sizes.border_small),
                                        size=(sizes.category_width_progress(self.categorynb), sizes.category_height),
                                        source='images/scenery/niveau_avancement_curseur.png',
                                        allow_stretch=True,
                                        keep_ratio=False)
        f.add_widget(self.category_scale)

        # tree with bird (at first)
        self.tree = ImageWrap(pos=sizes.tree_pos,
                              size=sizes.tree_size,
                              source='images/non_animes/arbre_oiseau.png')
        f.add_widget(self.tree)

        # textual description elements
        self.elem_first_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_title),
                                         pos=(sizes.border_text_min, sizes.height_left_first_desc),
                                         text=Text(fr="FR", de='DE', en='EN'),
                                         vAlignTop=True)
        f.add_widget(self.elem_first_desc)

        self.elem_second_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_title),
                                          pos=(sizes.border_text_min, sizes.height_left_second_desc),
                                          text=Text(fr="FR", de='DE', en='EN'),
                                          vAlignTop=True)
        f.add_widget(self.elem_second_desc)

        self.category_text = LabelWrap(size=(sizes.width_left_margin, sizes.height_left_category_element),
                                       pos=(sizes.width_ref, sizes.height_left_category_title),
                                       text=Text(fr='Catégorie', de='Kategorie', en='Category'),
                                       font_size=sizes.font_size_subtitle, bold=True)
        f.add_widget(self.category_text)
        self.category_text.update_cat(self.categorynb)

        self.category_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_left_category_element),
                                       pos=(sizes.border_text_min, sizes.height_left_category_desc),
                                       text=Text(fr="FR", de='DE', en='EN'),
                                       font_size=sizes.font_size_large)
        f.add_widget(self.category_desc)

    # welcome tutorial: happy guy speaking
    def init_welcome_tuto(self):
        # todo: add this to demo /tuto
        anim = Animation(y=sizes.cursor_pos_y(0), duration=1)
        anim += Animation(y=sizes.cursor_pos_y(2 * sizes.gauge_number), duration=2)
        anim += Animation(y=sizes.cursor_pos_y(sizes.gauge_number), duration=1)
        anim.start(self.cursor.image)

        # welcoming guy
        animated = ImageWrap(pos=sizes.human_pos,
                             size=sizes.human_size,
                             source='images/animations/bonhomme/homme_positif_content_2.gif')
        animated.image.anim_delay = 0.1
        animated.image.anim_loop = 5
        self.frame.add_widget(animated)

        self.speach = LabelWrap(size=(sizes.speach_width, sizes.speach_height),
                                pos=sizes.speach_pos,
                                text=Text(fr="FR", de='DE', en='EN'),
                                font_size=sizes.font_size_large)
        self.speach.label.text = txt_tutorial_welcome()
        self.speach.label.background_color = 1, 1, 1, 0.8
        self.frame.add_widget(self.speach)

    def init_category_struct(self):
        positif = ElementScatter(name=Text("fr", "de", "en"), positive=True, first=True,
                                 img='images/non_animes/haie_diverses_especes.png')
        negatif = ElementScatter(name=Text("fr", "de", "en"), positive=False, first=False,
                                 img='images/non_animes/haie_de_thuya.png')

        target = ImageWrap(pos=(sizes.width_left_margin, 0),
                           size=(175, 175),
                           source='images/zones_de_depot/haies.zip')
        target.image.anim_delay = 1
        category = Category(name=Text("haies et bordures", "de", "en"), el1=positif, el2=negatif, target=target)
        self.gameturn_setup(category)

    def category_forward(self, touch):
        if (self.categorynb < sizes.category_number):
            self.speach.label.text = txt_game_move_pass()
            self.anim_points(0, 0, 0, self.category_next)
            print self.quiz.next_question()
        else:
            self.category_next(touch)

    def category_next(self, screen):
        if (self.categorynb >= sizes.category_number):
            print 'TODO: end of game, see results before leaving'
            self.back()
        category = self.current_category
        # todo: reactivate , just easier to test
        # self.frame.remove_widget(category.target)
        # self.frame.remove_widget(category.element1)
        # self.frame.remove_widget(category.element2)

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
        points_image = ImageWrap(size=(size, size),
                                 pos=(x_start, y_start),
                                 source='images/scenery/points_neutre_500x500px.png')
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

    # update the cursor placement and gauge filling/color depending on points
    def update_cursor(self):
        anim = Animation(y=sizes.cursor_pos_y(self.points + sizes.gauge_number), duration=1)
        anim.start(self.cursor.image)
        self.gauge.image.size = (sizes.gauge_width, sizes.gauge_height(self.points + sizes.gauge_number))
        if (self.points >= 0):
            self.gauge.image.source = 'images/scenery/score_vert.png'
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
                static = ImageWrap(pos=(sizes.width_left_margin, 0), size=(175, 175), source=element.image.source)
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
                animated = ImageWrap(pos=(790 + sizes.width_left_margin, 386), size=(75, 152),
                                     source='images/animations/bonhomme/homme_positif_content_2.gif')
                animated.image.anim_delay = 0.1
                animated.image.anim_loop = 5
                if (element.positive):
                    animated.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
                else:
                    # TODO: put the negative animation, remove the placement, remove the non-moving guy
                    animated.image.source = 'images/animations/bonhomme/homme_positif_content_2.gif'
                    animated.image.pos = (890 + sizes.width_left_margin, 186)

                element.parent.add_widget(animated)

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

                # animation of animals
                # TODO: real animals!
                animal = AnimatedScatter()
                animal.image.anim_delay = 0.1
                animal.image.size = (75, 152)
                animal.pos = (sizes.width, sizes.height / 2)
                animal.image.source = 'images/animations/haies/mesange_vole.zip'
                animal.image.anim_delay = 0.2
                element.parent.add_widget(animal)
                anim = Animation(x=175 / 2 + sizes.width_left_margin, y=175 / 2, duration=2)
                heart = ImageWrap(pos=(175 / 2 + 200, 175 / 2), size=(46, 50),
                                  source='images/animations/eaux/coeur.zip')

                def after_anim():
                    self.anim_points(m, 175 / 2 + sizes.width_left_margin, 175 / 2, fct_next=after)

                def after_bad(t, r):
                    anim = Animation(x=100 + sizes.width, y=sizes.height / 2, duration=2)
                    anim.start(animal)
                    after_anim()

                def remove_heart(t, r):
                    element.parent.remove_widget(heart)

                def add_heart(t, r):
                    element.parent.add_widget(heart)
                    anim = Animation(x=250, y=200, duration=1)
                    anim += Animation(x=-100, y=175, duration=2)
                    anim.start(animal)
                    anim.bind(on_complete=remove_heart)
                    after_anim()

                if (element.positive):
                    anim.bind(on_complete=add_heart)
                else:
                    anim.bind(on_complete=after_bad)
                anim.start(animal)
                # todo: remove the animal or make sure it disappear
                # element.parent.remove_widget(animal)

                anim_wid = Animation(x=element.x_orig, y=element.y_orig)
                anim_wid.start(element)

                # todo: always remove the widget
                # todo: why does selection doesn't work well ??
                # if (not element.positive):
                #   element.parent.remove_widget(element)
                self.currentObj = ObjectProperty(None)

                if (element.positive):
                    self.points += 1
                else:
                    self.points -= 1

                # todo : disable all other widget!


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

        def y(_y):
            return _y + sizes.win_dy

        window_frame = FloatLayout(size_hint=(1, 1), pos=(0, 0))

        window_frame.add_widget(ImageWrap(
            pos=(x(-2), y(-22)),
            size=(923, 624),
            source='images/scenery/fenetre_infos_923x624px.png'))

        window_frame.add_widget(ImageWrap(pos=(x(0), y(sizes.win_height - sizes.win_header)),
                                          size=(sizes.win_width, sizes.win_header),
                                          source='images/scenery/bandeau_gris_fenetre_choix_898x80px.png'))

        window_frame.add_widget(
            LabelWrap(pos=(x(0), y(sizes.win_height - sizes.win_header)),
                      size=(sizes.win_width - sizes.win_width_infos, sizes.win_header),
                      text=Text(fr="Ce n'est pas le bon choix...", de="TODE", en="TOEN"),
                      font_size=sizes.font_size_title,
                      bold=True))

        # todo: separate the text for internationalizazion !
        window_frame.add_widget(ButtonImage(
            on_press=self.more_infos,
            pos=(x(sizes.win_width - sizes.win_width_infos), y(sizes.win_height - sizes.win_header)),
            size=(sizes.win_width_infos, sizes.win_header),
            size_img=(sizes.win_width_infos, sizes.win_header),
            src='images/scenery/bouton_plus_d_infos_183x80px.png'))

        # todo: react to clicks
        def replace(screen):
            print 'replace'
            self.points += 2

            self.static.image.source = 'images/non_animes/haie_diverses_especes.png'

            # todo: better
            animal = AnimatedScatter()
            animal.image.anim_delay = 0.1
            animal.image.size = (75, 152)
            animal.pos = (0 + sizes.width_left_margin, 768)
            animal.image.source = 'images/animations/haies/mesange_vole.zip'
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

            # todo: correction, instead, in right position
            self.static.image.source = 'images/non_animes/haie_diverses_especes.png'
            self.static.image.pos = (400, 0)

            # todo: better
            animal = AnimatedScatter()
            animal.image.anim_delay = 0.1
            animal.image.size = (75, 152)
            animal.pos = (0 + sizes.width_left_margin, 768)
            animal.image.source = 'images/animations/haies/mesange_vole.zip'
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
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=recover.negative))

        class ButtonImageChoicesRemove(ButtonImageChoices):
            def __init__(self, recover):
                pos = (x(sizes.win_choice_right), y(sizes.win_choice_up))
                text = Text(fr="Enlever", de="TODE", en="TOEN")
                super(ButtonImageChoicesRemove, self).__init__(remove, pos, text)

                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=recover.negative))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source='images/scenery/picto_croix_112x112px.png'))

        class ButtonImageChoicesReplace(ButtonImageChoices):
            def __init__(self, recover):
                pos = (x(sizes.win_choice_left), y(sizes.win_choice_up))
                text = Text("Remplacer", "TODE", "TOEN")
                super(ButtonImageChoicesReplace, self).__init__(replace, pos, text)

                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source='images/scenery/fleche_seule_23x44px.png'))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=recover.negative))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source='images/scenery/picto_croix_112x112px.png'))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_right, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=recover.positive))

        class ButtonImageChoicesCorrect(ButtonImageChoices):
            def __init__(self, recover):
                pos = (x(sizes.win_choice_right), y(sizes.win_choice_down))
                text = Text("Corriger", "TODE", "TOEN")
                super(ButtonImageChoicesCorrect, self).__init__(correct, pos, text)

                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source='images/scenery/fleche_seule_23x44px.png'))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=recover.negative))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_right, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=recover.correction))

        # initiate a correct recover
        recover = Recover('images/non_animes/haie_diverses_especes.png', 'images/non_animes/haie_de_thuya.png', True,
                          'images/non_animes/haie_de_thuya.png')
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
