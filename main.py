# coding=utf-8
# UTF-8 MUST be imported FIRST to prevent issues

# TODO: disable the watermark (False) for actual production at client's premise (Pro Natura). Leave it enabled (True) for distribution and ANY other use.
watermarked = True
# TODO: enable the quiz (True) on the computer whre the quizz is wanted (otherwise, False, it will launch the garden game)
quiz_enabled = True
# TODO: True if it should enable the English langage (False for client, True for demo / distribution)
english_enabled = True
# general reset timeout in seconds
timeout = 60
#timeout of warning window (timeout/stop game)
timeout_window_conf = 15
max_darkness_idle = 0.70 # 0 -> 1.0 scale, 1.0 the darker

from kivy.config import Config

from utils import sizes

if watermarked:
    Config.set('graphics', 'fullscreen', 'auto')  # Keep the width * width size for distribution
else:
    Config.set('graphics', 'fullscreen', 'auto')  # take full screen for production
Config.set('graphics', 'width', sizes.width)  # 1366
Config.set('graphics', 'height', sizes.height)  # 768

Config.set('graphics', 'position', 'custom')  # 'auto'
Config.set('graphics', 'top', 0)
Config.set('graphics', 'left', 0)

Config.set('graphics', 'show_cursor', 0)
Config.set('graphics', 'borderless', 1)
Config.set('graphics', 'resizable', 0)

import os
import random
import settings
import time
from subprocess import call

from kivy.animation import Animation

from kivy.core.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, Clock
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.core.text import LabelBase

from utils.texts import *
from utils import texts as txt
from utils.category import ElementScatter, init_category_struct
from utils.gui import ImageWrap, ButtonImage, ButtonImageText, ButtonImageChoices, LabelWrap
from utils.quiz import Quiz

# loading widget instructions
Builder.load_file('screens.kv')
Builder.load_file('widgets.kv')

# pre-load game music
# started when game is started and stopped when game is stopped or idled back to start screen
# no music for quiz
music = SoundLoader.load("audio/garden_base.wav")
music_alt = SoundLoader.load("audio/garden_alt.wav")
# load and start playing game audio
music.loop = music_alt.loop = True
music.volume = music_alt.volume = 0.8 # 0 -> 1 scale, 1=100%, default to 1 for others sounds


# Creating a backgroundable label (by default a blank background)
# http://robertour.com/2015/07/15/kivy-label-or-widget-with-background-color-property/
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
        self.parent.parent.parent.parent.check(self)


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


# windows utilities (pop-up window that come over other screens)
def win_dx(_x):
    return _x + sizes.win_dx


def win_dy(_y):
    return _y + sizes.win_dy


def win_generate(text_title, size=(sizes.win_width + 26, sizes.win_height + 23)):
    window_frame = FloatLayout(size_hint=(1, 1), pos=(0, 0))

    window_frame.add_widget(ImageWrap(
        pos=(win_dx(-2), win_dy(-22)),
        size=size,
        source='images/scenery/fenetre_infos_923x624px.png'))

    def none(*any):
        pass

    # fake & invisible & no effects button to disabled behing contents
    fakebutton = ButtonImage(on_press=none,
                             pos=(win_dx(-2), win_dy(-22)),
                             size=size,
                             size_img=size,
                             allow_strech=True,
                             source="images/scenery/transparency.png")
    fakebutton.background_down = fakebutton.background_normal
    window_frame.add_widget(fakebutton)

    # title
    window_frame.add_widget(
        LabelWrap(pos=(win_dx(0), win_dy(sizes.win_height - sizes.win_header)),
                  size=(sizes.win_width - sizes.win_width_infos, sizes.win_header),
                  text=text_title,
                  font_size=sizes.font_size_title,
                  hAlignLeft=True,
                  padding=(10, 0),
                  bold=True))

    padding = 10
    im = ImageWrap(pos=(win_dx(padding), win_dy(padding)),
                   size=(sizes.win_width - 2 * padding, (sizes.win_height - sizes.win_header) / 2.4),
                   source="images/scenery/transparency.png")
    window_frame.image = im.image
    window_frame.add_widget(im)

    size = sizes.font_size_win

    window_frame.label = LabelWrap(pos=(win_dx(sizes.win_text_margin), win_dy(0)),
                                   size=(
                                       sizes.win_width - sizes.win_text_margin, sizes.win_height - sizes.win_header),
                                   text=txt_scenery_notxt,
                                   font_size=size,
                                   padding=(padding, padding),
                                   vAlignTop=True,
                                   hAlignLeft=True)
    window_frame.add_widget(window_frame.label)

    # add dots at anchors
    window_frame.try_again = True

    def add_dots(*any):
        anchors = window_frame.label.label.anchors
        if window_frame.try_again & (anchors == {}):
            # should 'try again' to add anchors
            window_frame.try_again = False
            Clock.schedule_once(add_dots, 1 / 4.0)
        for key in anchors:
            v = anchors[key]
            # start of new lines for dots
            if 'dot' in key:
                window_frame.add_widget(LabelWrap(
                    pos=(win_dx(0), win_dy(sizes.win_height - sizes.win_header) - v[1] - size),
                    size=(sizes.win_text_margin + padding, size * 3 / 4),
                    text=txt_dot,
                    font_size=size,
                    hAlignLeft=True))
            # end of text for image sizes and positioning
            if 'end' in key:
                im.image.size[1] = sizes.win_height - sizes.win_header - v[1] - size - 2 * padding

    # this should be done by waiting for the end of rendering. 99.9% fo times it will be finished before the 1/25 (40ms) threshold,
    # and 1/25 is not perpectible by eye. In the worst case it's tried a second time after 1/4 second. (250 ms)
    Clock.schedule_once(add_dots, 1 / 25.0)

    return window_frame


# start screen to choose language and see credits
class StartScreen(KeyScreen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.frequency_idle_light = 0.01
        self.step_idle_light = 0.01
        self.dark_continue = True
        self.button_click = True

        impressum_txt = txt.txt_impressum

        # for the impressum, shift the window up
        dy = 50
        sizes.win_dy += dy

        window_frame = win_generate(text_title=impressum_txt)
        window_frame.label.label.text = txt_impressum_full
        self.visible = False

        def impressum(*any):
            if self.visible:
                close(any)
            else:
                self.visible = True

                def remove_impressum_win(*any):
                    if self.visible:
                        self.visible = False
                        self.remove_widget(window_frame)

                def add_impressum_win(*any):
                    self.add_widget(window_frame)
                    Clock.schedule_once(remove_impressum_win, timeout*2)

                if self.dim_element.background_color[3] > 0:
                    Clock.schedule_once(add_impressum_win, (
                    self.dim_element.background_color[3] / self.step_idle_light - 10) * self.frequency_idle_light)
                else:
                    add_impressum_win()

        def close(*any):
            self.visible = False
            self.remove_widget(window_frame)
            self.resume()

        # add the close button of window
        window_frame.add_widget(ButtonImageText(
            on_press=close,
            pos=(win_dx(sizes.win_width - sizes.win_header), win_dy(sizes.win_height - sizes.win_header)),
            size=(sizes.win_header, sizes.win_header),
            source_back='images/scenery/back_80x183px_red.png',
            size_img=(sizes.win_header, sizes.win_header),
            source='images/scenery/picto_croix_150x150px.png',
            text=txt_scenery_notxt,
            left=0))

        self.cal_ct = 0
        def terminate(btn):
            self.cal_ct += 1
            if self.cal_ct == 1:
                def reset_cal_ct(*any):
                    self.cal_ct = 0
                Clock.schedule_once(reset_cal_ct, 2)
            if self.cal_ct == 5:
                def calib(*any):
                    App.get_running_app().stop()
                Clock.schedule_once(calib, 0.5)
                self.cal_ct = 0


        window_frame.add_widget(ButtonImage(
            on_press=terminate,
            pos=(win_dx(sizes.win_width - sizes.win_header - 10), win_dy(70)),
            size=(79, 164),
            size_img=(79, 164),
            source='images/credits/HEIG-VD_Logo 14x29_RVB ROUGE.png'))

        # reverse invisible button
        window_frame.add_widget(ButtonImage(
            on_press=terminate,
            pos=(sizes.width - 79 - win_dx(sizes.win_width -  sizes.win_header - 10), sizes.height - 164 - win_dy(70)),
            size=(79, 164),
            size_img=(79, 164),
            source='images/scenery/transparency.png'))

        h = 100.0
        l = h / 305.0 * 771.0
        window_frame.add_widget(ButtonImage(
            on_press=terminate,
            pos=(win_dx(sizes.win_width - l - 10), win_dy(sizes.win_height - sizes.win_header - h - 10)),
            size=(l, h),
            size_img=(l, h),
            source='images/credits/pronatura.png'))

        #reverse invisible button
        window_frame.add_widget(ButtonImage(
            on_press=terminate,
            pos=(sizes.width - l - win_dx(sizes.win_width - l - 10), sizes.height - h - win_dy(sizes.win_height - sizes.win_header - h - 10)),
            size=(l, h),
            size_img=(l, h),
            source='images/scenery/transparency.png'))

        # add logos with impressum buttum
        self.add_widget(ButtonImageText(
            on_press=impressum,
            pos=(2 * sizes.width_left_margin, 0),
            size=(624, 100),
            source_back='images/scenery/impressum.png',
            size_img=(1, 1),
            source='images/scenery/transparency.png',
            text=impressum_txt,
            left=624,
            vAlignTop=True))

        # add start buttons in 2 or 3 languages
        w_lang_elem = 200
        poxy_lang_elem = 295
        nb_elem = 2
        if english_enabled:
            nb_elem += 1

        total_spaces = nb_elem + 1 + 2  # + last elem + 2 elem at each end)
        index = 0

        def pos_x_lang():
            return sizes.width_left_margin \
                   + (sizes.width_game - nb_elem * w_lang_elem) / total_spaces * (2 + index) \
                   + index * w_lang_elem

        self.add_widget(ButtonImageText(
            on_press=self.french,
            pos=(pos_x_lang(), poxy_lang_elem),
            size=(w_lang_elem, 97),
            source_back='images/scenery/fenetre_infos_200x97px_green.png',
            size_img=(23, 30),
            source='images/scenery/fleche_seule_23x44px_white.png',
            text=txt_lang_choice_fr,
            left=170,
            font_size=sizes.font_size_title))
        index += 1

        self.add_widget(ButtonImageText(
            on_press=self.german,
            pos=(pos_x_lang(), poxy_lang_elem),
            size=(w_lang_elem, 97),
            source_back='images/scenery/fenetre_infos_200x97px_green.png',
            size_img=(23, 30),
            source='images/scenery/fleche_seule_23x44px_white.png',
            text=txt_lang_choice_de,
            left=170,
            font_size=sizes.font_size_title))
        index += 1

        if english_enabled:
            self.add_widget(ButtonImageText(
                on_press=self.english,
                pos=(pos_x_lang(), poxy_lang_elem),
                size=(w_lang_elem, 97),
                source_back='images/scenery/fenetre_infos_200x97px_green.png',
                size_img=(23, 30),
                source='images/scenery/fleche_seule_23x44px_white.png',
                text=txt_lang_choice_en,
                left=170,
                font_size=sizes.font_size_title))

        # add titles in 2 or 3 languages
        self.add_widget(LabelWrap(
            pos=(sizes.width_left_margin, 560),
            size=(sizes.width_game, 40),
            text=txt_main_title_fr,
            font_size=sizes.font_size_title,
            bold=True
        ))

        self.add_widget(LabelWrap(
            pos=(sizes.width_left_margin, 560 - 1 * 40),
            size=(sizes.width_game, 40),
            text=txt_main_title_de,
            font_size=sizes.font_size_title,
            bold=True
        ))

        if english_enabled:
            self.add_widget(LabelWrap(
                pos=(sizes.width_left_margin, 560 - 2 * 40),
                size=(sizes.width_game, 40),
                text=txt_main_title_en,
                font_size=sizes.font_size_title,
                bold=True
            ))

        sizes.win_dy -= dy

        self.dim_element = LabelB()
        self.dim_element.background_color = 0,0,0,0
        self.add_widget(self.dim_element)
        self.on_touch_up()

        #reverse impressum -> calibrate the screen with 5 second timeout if pressed
        # if the screen is inversed (not calibrated), then the calibration will launch when "it's like" impressum is pressed
        self.cal_ct = 0
        def calibrate(btn):
            if self.dim_element.background_color[3] < 0.05:
                self.cal_ct += 1

            if self.cal_ct == 1:
                def reset_cal_ct(*any):
                    self.cal_ct = 0
                Clock.schedule_once(reset_cal_ct, 2)

            if self.cal_ct == 5:
                def calib(*any):
                    call(["/etc/opt/elo-usb/elova", "--nvram", "--caltargettimeout=5"])
                Clock.schedule_once(calib, 0.5)
                self.cal_ct = 0


        self.add_widget(ButtonImage(
            on_press=calibrate,
            pos=(sizes.width - (2 * sizes.width_left_margin) - 624, sizes.height - 0 - 100),
            size=(624, 100),
            size_img=(624, 100),
            source='images/scenery/transparency.png'))

    def on_touch_up(self, *any):
        self.dark_continue = False
        self.resume()
        self.last_click = time.time()
        Clock.schedule_once(self.check_idle, timeout + 1)

    def check_idle(self, *any):
        current = time.time()
        if (current - self.last_click) > timeout:
            self.dark_continue = True
            self.idle()

    def idle (self, *any):
        self.dim_element.background_color = 0, 0, 0, self.dim_element.background_color[3] + self.step_idle_light
        if self.dim_element.background_color[3] < max_darkness_idle and self.dark_continue:
            Clock.schedule_once(self.idle, self.frequency_idle_light * 10)

    def resume (self, *any):
        self.dim_element.background_color = 0, 0, 0, self.dim_element.background_color[3] - self.step_idle_light
        if self.dim_element.background_color[3] > 0:
            Clock.schedule_once(self.resume, self.frequency_idle_light)

    def french(self, *any):
        lang.current = lang.fr
        self.forward()

    def german(self, *any):
        lang.current = lang.de
        self.forward()

    def english(self, *any):
        lang.current = lang.en
        self.forward()

    def forward(self):
        if self.button_click:
            self.button_click = False
            self.dark_continue = False
            self.on_touch_up()

            def forward(*any):
                save_entry(file="~/Desktop/garden.csv", opt = "start")
                self.manager.switch_to(FloatGameScreen(name=txt_main_title_short, previous=self), direction='left')

            if self.dim_element.background_color[3] > 0:
                Clock.schedule_once(forward, (self.dim_element.background_color[3] / self.step_idle_light - 10) * self.frequency_idle_light)
            else:
                forward()

    #should be called by next screen when they come back to restore the timeout
    def return_to_screen(self):
        self.button_click = True
        self.dark_continue = True
        self.on_touch_up()


def save_entry(file, opt = ""):
    time_sec = time.time()
    time_utf = time.ctime(time_sec)
    os.system("echo " + str(time_sec) + ", " + time_utf + ", " + lang_str() + ", " + opt + " >> " + file)

# screen for picking training mode difficulty
class StatsScreen(KeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()
    max = 5
    should_forward = True

    def __init__(self, **kwargs):
        super(StatsScreen, self).__init__(**kwargs)

        def add_star(widget, lang):
            widget.add_widget(Label())
            for i in range(1, self.max + 1):
                bs = ButtonStar()
                bs.lang = lang
                bs.text = bs.id = str(i)
                widget.add_widget(bs)
                widget.add_widget(Label())

        add_star(self.star_fr, lang = lang.fr)
        add_star(self.star_de, lang = lang.de)

        self.until_run = 0
        self.until_run_up = True
        Clock.schedule_interval(self.check_run, 0.5)


    def check_run(self, *any):
        if (self.should_forward):
            self.check_stars(self.star_fr, self.until_run)
            self.check_stars(self.star_de, self.until_run)
        self.until_run +=1 if self.until_run_up else -1

        if (self.until_run == self.max + 1):
            self.until_run_up = False
        if (self.until_run < -self.max):
            self.until_run_up = True


    def check(self, btn):
        nb = int(btn.id)
        self.rate = nb

        # change language
        lang.current = btn.lang

        save_entry(file = "~/Desktop/rates.csv", opt = str(nb))

        self.check_stars(self.star_fr, nb)
        self.check_stars(self.star_de, nb)
        if (self.should_forward):
            self.should_forward = False
            Clock.schedule_once(self.forward, 0.5)

    def validate_fr(self):
        lang.current = lang.fr
        self.forward()

    def validate_de(self):
        lang.current = lang.de
        self.forward()

    def check_stars(self, widget, until):
        for i in widget.children:
            if (i.id):
                if int(i.id) <= until:
                    i.state = 'down'
                else:
                    i.state = 'normal'

    def reset_stars(self, *any):
        def reset_star(widget):
            for i in widget.children:
                if (i.id):
                    i.state = 'normal'

        reset_star(self.star_fr)
        reset_star(self.star_de)

    def forward(self, *any):
        self.manager.switch_to(ContestIntroScreen(name="Quiz", previous=self,quiz = Quiz()), direction='up')
        self.should_forward = True
        Clock.schedule_once(self.reset_stars, 1)


    def switch_color(self, *any):
        print 'hello'
        if self.logo.source == 'images/credits/pronatura.png':
            self.logo.source = 'images/credits/pronatura_nb.png'
        else:
            self.logo.source = 'images/credits/pronatura.png'

    cal_ct = 0
    def calibrate(self):
        self.cal_ct += 1
        if self.cal_ct == 1:
            def reset_cal_ct(*any):
                self.cal_ct = 0
            Clock.schedule_once(reset_cal_ct, 2)
        if self.cal_ct == 5:
            def calib(*any):
                call(["/etc/opt/elo-usb/elova", "--nvram", "--caltargettimeout=5"])
            Clock.schedule_once(calib, 0.5)
            self.cal_ct = 0
    stop_ct = 0
    def check_stop(self):
        self.stop_ct += 1
        if self.stop_ct == 1:
            def reset_stop_ct(*any):
                self.stop_ct = 0
            Clock.schedule_once(reset_stop_ct, 2)
        if self.stop_ct == 5:
            def stop(*any):
                App.get_running_app().stop()
                App.get_running_app().stop()
            call(["/etc/opt/elo-usb/elova", "--nvram", "--caltargettimeout=5"])
            Clock.schedule_once(stop, 0.5)
            self.stop_ct = 0

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
                t.text = q.replies[i].text.get()
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
    def __init__(self, quiz, **kwargs):
        super(ContestIntroScreen, self).__init__(**kwargs)
        self.current_question = 0
        self.quiz = quiz
        self.all_correct = True

        self.correct = ['replies']
        self.correct_nb = 0
        self.public = "U"
        self.quest_corr = ""
        self.nbimg = quiz.question_images.__len__()
        self.nbtxt = quiz.questions.__len__()
        self.max = 2 + self.nbimg + self.nbtxt

        self.fwd(rm=False)
        self.timeout_running = True
        self.timeout_touch()

    def check(self):
        self.next()


    def fwd(self, rm = True, *any):
        if rm:
            self.l.remove_widget(self.im)
        if (self.current_question < self.max):
            #quest 1->nbimg are images questions
            if (self.current_question != 0 and self.current_question < self.nbimg + 1):
                q = self.quiz.question_images[self.current_question - 1]
                self.im = QuestionWidget(q, image=True)
            else:
                #first (0) question is corridors biologiques
                if (self.current_question == 0):
                    q = self.quiz.question_corridors
                #last question is public distinction
                elif (self.current_question == self.max - 1):
                    q = self.quiz.question_public
                #x-> before last are text questions
                else:
                    q = self.quiz.questions[self.current_question - self.nbimg - 1]
                self.im = QuestionWidget(q, image=False)

            self.l.add_widget(self.im)
            self.current_question += 1
            # questions counter
            self.timer.text = txt_quiz_question.get() + str(self.current_question) + "/" + str(self.max)
        else:
            self.forward()

    def next(self):
        self.im.block()
        is_correct = self.im.correct()
        if (self.current_question < self.max):
            self.all_correct &= is_correct
            if (self.current_question == 1):
                self.quest_corr = is_correct
            else: #the last question is public distinction, not counted for all_correct
                self.correct_nb += 1 if is_correct else 0
        else:
            # children (E=Enfant) is True, Adult is False
            self.public = 'E' if is_correct else 'A'
        self.correct.append(is_correct)
        Clock.schedule_once(self.fwd, 0.5)

    def end_stats(self):
        # all_correct T/F, corridors T/F, #nb_correct (max 3), total_question(max 5), #public A/E/U, no details of questions
        save_entry(file="~/Desktop/stats.csv", opt=str(self.all_correct) + ", " + str(self.quest_corr) + ", " + str(self.correct_nb) + "," + str(self.current_question) + ", " + self.public)

    def forward(self):
        self.timeout_running = False
        self.end_stats()
        self.manager.switch_to(ContestScreen(name="Contest", previous=self.previous, all_correct = self.all_correct), direction='left')

    # triggered for EVERY touch MOVE on any element of this screen
    def on_touch_move(self, touch):
        self.timeout_touch()
        return False

    # triggered for EVERY touch UP on any element of this screen
    def on_touch_up(self, touch):
        self.timeout_touch()

    # should be called anywhere a touch is made, to update last_lcik and schedule the timeout check
    def timeout_touch(self):
        self.last_click = time.time()
        Clock.schedule_once(self.timeout_check, timeout + 1)

    # check if timeout has expired and expire
    def timeout_check(self, dt):
        current = time.time()
        if (current - self.last_click) > timeout:
            if self.timeout_running:
                self.timeout_running = False
                self.end_stats()
                self.back()

# screen for picking training mode difficulty
class ContestScreen(BackKeyScreen):
    # layout containing the screen's buttons, used for cursor function
    layout = ObjectProperty()

    def __init__(self, all_correct, **kwargs):
        super(ContestScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', size_hint=(1, 1), padding=10, spacing=10)
        self.add_widget(layout)

        text = txt_quiz_end_positive if all_correct else txt_quiz_end_negative

        layout.add_widget(
            Label(
                text=text.get(),
                size_hint=(1, 0.2)))

        if all_correct:
            summary = Label(
                text=txt_quiz_tombola_start.get(),
                size_hint=(1, 0.2))
            layout.add_widget(summary)
            summary.font_size = sizes.font_size_title

            counter = Label(
                text="-",
                size_hint=(1, 1))
            layout.add_widget(counter)
            counter.font_size = 100

            self.i = 5 + 1
            def retract(*any):
                self.i -= 1
                counter.text = str(self.i)
                if (self.i > 0):
                    Clock.schedule_once(retract, 1)
                else:

                    win = False
                    winners = {1654, 2478, 3745, 4536, 5937}
                    my_win = random.randint(1, 9999)

                    reset_txt.text = txt_quiz_tombola_reset.get()
                    if my_win in winners:
                        win = True

                    def reset(*any):
			if self.timeout_running:
			    self.timeout_running = False
                	    self.back()

                    if win:
                        summary.text = txt_quiz_tombola_win.get()
                        counter.text = str(my_win)
                        Clock.schedule_once(reset, timeout + 10)
                    else:
                        summary.text = txt_quiz_tombola_loose.get()
                        Clock.schedule_once(reset, timeout)
		    self.timeout_touch()

            retract()

        reset_txt = Label(
            size_hint=(1, 0.1))
        layout.add_widget(reset_txt)
        if not all_correct:
            reset_txt.text = txt_quiz_tombola_reset.get()

	self.timeout_running = True
	self.timeout_touch()

    # triggered for EVERY touch MOVE on any element of this screen
    def on_touch_move(self, touch):
        self.timeout_touch()
        return False

    # triggered for EVERY touch UP on any element of this screen
    def on_touch_up(self, touch):
        self.timeout_touch()

    # should be called anywhere a touch is made, to update last_lcik and schedule the timeout check
    def timeout_touch(self):
        self.last_click = time.time()
        Clock.schedule_once(self.timeout_check, timeout + 1)

    # check if timeout has expired and expire
    def timeout_check(self, dt):
        current = time.time()
        if (current - self.last_click) > timeout:
            if self.timeout_running:
                self.timeout_running = False
                self.back()



# float layout for draggable elements management
class FloatGameScreen(BackKeyScreen):
    currentObj = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(FloatGameScreen, self).__init__(**kwargs)
        music.play()
        self.quiz = Quiz()
        self.game_running = True
        self.timeout_warning_off = True

        # handles category numbers (start at 0)
        self.nb_current_category = 0
        self.nb_current_category__used = 0
        self.points = 0

        #auto-detect and help people that have problems with placement
        self.fail_interact_trial = 0
        self.easy_interact_mode = False

        self.frame = FloatLayout(size_hint=(1, 1))
        self.init_static_UI()
        self.init_pseudo_static_UI()
        self.init_dynamic_UI()

        # add main layout to root
        self.add_widget(self.frame)

        # init categories and game
        self.init_welcome_tuto()
        self.start_game_tuto()

        #trigger timeout at start already
        self.timeout_touch()


    # create and add all static UI elements (non-movable, non-changeable, only background and scenery)
    def init_static_UI(self):
        f = self.frame
        self.frame.cat_reverse = False

        # garden background and large borders left/right
        f.add_widget(ImageWrap(pos=(sizes.width_ref, sizes.height_ref),
                               size=(sizes.width_left_margin, sizes.height),
                               source='images/scenery/nav_fond_gauche_200x768px.png'))
        f.add_widget(ImageWrap(pos=(sizes.width_left_margin, sizes.height_ref),
                               size=(sizes.width_game, sizes.height),
                               source='images/fond/fond_jardin_v7a.png'))
        f.add_widget(ImageWrap(pos=(sizes.width_right_game, sizes.height_ref),
                               size=(sizes.width_right_margin, sizes.height),
                               source='images/scenery/nav_fond_droite_142x768px.png'))

        f.add_widget(ImageWrap(pos=sizes.table_pos,
                               size=(130, 119),
                               source='images/non_animes/table_chaise_de_jardin.png'))

        # right elements
        # smiles and points scale (gauge)
        f.add_widget(ImageWrap(pos=(sizes.gauge_left_margin, sizes.gauge_bottom_margin),
                               size=(77, 493),
                               source='images/scenery/score_77x493px.png'))
        f.add_widget(ImageWrap(pos=(sizes.gauge_smiley_left, sizes.gauge_smiley_top),
                               size=(29, 29),
                               source='images/scenery/smile_positif_210x200px.png'))
        f.add_widget(ImageWrap(pos=(sizes.gauge_smiley_left, sizes.gauge_smiley_bottom),
                               size=(29, 29),
                               source='images/scenery/smile_negatif_210x200px.png'))

        # left elements
        f.add_widget(ImageWrap(pos=(sizes.border_small, sizes.border_small + sizes.height_button_small),
                               size=(sizes.category_width, sizes.category_height),
                               source='images/scenery/niveau_avancement_186x23px.png',
                               keep_ratio=False, allow_stretch=True), )

        # buttons
        f.add_widget(ButtonImage(on_press=self.category_forward,
                                 pos=(sizes.width_ref, sizes.border_small),
                                 size=(sizes.width_left_margin, sizes.height_button_small),
                                 size_img=(75, 44),
                                 source="images/scenery/fleche_suite_75x44px.png"))
        f.add_widget(ButtonImage(on_press=self.stop_game_ask,
                                 pos=(sizes.width_right_game, sizes.border_small),
                                 size=(sizes.width_right_margin, sizes.height_button_small),
                                 size_img=(57, 57),
                                 source="images/scenery/bouton_eteindre_200x200px.png"))

        # nice ui elements and score text
        f.add_widget(LabelWrap(size=(sizes.width_right_margin, sizes.height_button_small),
                               pos=(sizes.width_right_game, sizes.height_left_score),
                               text=txt.txt_scenery_score,
                               font_size=sizes.font_size_subtitle, bold=True))
        f.add_widget(ImageWrap(pos=(
            sizes.width_right_game + sizes.width_border_left, sizes.height_left_score - sizes.border_small),
            size=(sizes.width_right_margin - 2 * sizes.width_border_left, sizes.border_small),
            source='images/scenery/filet_souligne_144x6px.png',
            allow_stretch=True,
            keep_ratio=False)
        )

        if (watermarked):
            watermark = LabelWrap(
                pos=(sizes.width_left_margin, sizes.height_ref),
                size=(sizes.width_game, sizes.height_button_small),
                text=txt_watermark_heig,
                font_size=sizes.font_size_large,
                bold=True
            )

            f.add_widget(watermark)
            if (sizes.pos_c2[1] == 0):
                sizes.pos_c2 = (sizes.pos_c2[0], sizes.pos_c2[1] + sizes.height_button_small)
                sizes.event_c2 = (sizes.event_c2[0], sizes.event_c2[1] + sizes.height_button_small)

            watermark.label.background_color = 1, 1, 1, 0.5

    # static in category left layout elements that need to disappear at the end of game
    def init_pseudo_static_UI(self):
        f = self.frame
        # nice ui elements for categories
        f1 = ImageWrap(pos=(sizes.width_border_left, sizes.height_left_category_title_filet - sizes.border_small),
                       size=(sizes.width_left_elements, sizes.border_small),
                       source='images/scenery/filet_souligne_144x6px.png')
        f2 = ImageWrap(pos=(sizes.width_border_left, sizes.height_left_category_desc - sizes.border_small),
                       size=(sizes.width_left_elements, sizes.border_small),
                       source='images/scenery/filet_souligne_144x6px.png')

        m1 = ImageWrap(size=(sizes.width_left_elements, sizes.width_left_elements),
                       pos=(sizes.width_border_left, sizes.height_left_first),
                       source='images/scenery/fond_menu_gauche_144x144px.png')
        m2 = ImageWrap(size=(sizes.width_left_elements, sizes.width_left_elements),
                       pos=(sizes.width_border_left, sizes.height_left_second),
                       source='images/scenery/fond_menu_gauche_144x144px.png')
        f.add_widget(f1)
        f.add_widget(f2)
        f.add_widget(m1)
        f.add_widget(m2)

        f.category_layout_f1 = f1
        f.category_layout_f2 = f2
        f.category_layout_m1 = m1
        f.category_layout_m2 = m2

    # remove left elements at the end
    def delete_pseudo_static_UI(self):
        f = self.frame
        # f.remove_widget(f.category_layout_f1)
        f.remove_widget(f.category_layout_f2)
        f.remove_widget(f.category_layout_m1)
        f.remove_widget(f.category_layout_m2)

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
                                        size=(
                                            sizes.category_width_progress(self.nb_current_category),
                                            sizes.category_height),
                                        source='images/scenery/niveau_avancement_curseur.png',
                                        allow_stretch=True,
                                        keep_ratio=False)
        f.add_widget(self.category_scale)

        # tree with bird (at first)
        self.tree = ImageWrap(pos=sizes.tree_pos,
                              size=sizes.tree_size,
                              source='images/non_animes/arbre_oiseau.png')
        f.add_widget(self.tree)
        f.tree = self.tree

        # textual description elements
        # fake mock text, actual real text will be loaded afterwards when categories are set up
        self.elem_first_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_title),
                                         pos=(sizes.border_text_min, sizes.height_left_first_desc),
                                         text=txt.txt_scenery_notxt,
                                         vAlignTop=True)
        f.add_widget(self.elem_first_desc)

        self.elem_second_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_title),
                                          pos=(sizes.border_text_min, sizes.height_left_second_desc),
                                          text=txt.txt_scenery_notxt,
                                          vAlignTop=True)
        f.add_widget(self.elem_second_desc)

        self.category_text = LabelWrap(size=(sizes.width_left_margin, sizes.height_left_category_element),
                                       pos=(sizes.width_ref, sizes.height_left_category_title),
                                       text=txt.txt_scenery_category,
                                       font_size=sizes.font_size_subtitle, bold=True)
        f.add_widget(self.category_text)
        self.category_text.update_cat(self.nb_current_category)

        self.category_desc = LabelWrap(size=(sizes.width_text_max, sizes.height_left_category_element),
                                       pos=(sizes.border_text_min, sizes.height_left_category_desc),
                                       text=txt.txt_scenery_notxt,
                                       font_size=sizes.font_size_large, bold=True)
        f.add_widget(self.category_desc)

        self.shadow = LabelWrap(size=(sizes.width, sizes.height),
                                pos=(sizes.width_ref, sizes.height_ref),
                                text=txt.txt_scenery_notxt)
        self.shadow.label.background_color = 1, 1, 1, 0.0
        f.add_widget(self.shadow)
        self.button_enabled = True
        self.button_cat_enabled = True

    def init_end_of_game_UI(self):
        f = self.frame

        end_height_element = sizes.end_height_element
        size = (end_height_element, end_height_element)

        start = sizes.end_start
        margin = sizes.end_margin

        def fct(**any):
            self.current_elem = None
        fct()

        i = 0
        for category in self.categories:
            i += 1

            self.end_window_frame = ObjectProperty(None)

            def pressed(button):
                if (self.current_elem != None):
                    f.remove_widget(self.end_window_frame)

                if (self.current_elem == button.element):
                    fct()
                else:
                    self.current_elem = button.element
                    self.end_window_frame = self.more_infos(button.element, fct=fct, negative=True, alternate=True)

            b = ButtonImage(on_press=pressed, source=category.element1.source, size=size, size_img=size,
                            pos=(margin, start - end_height_element * i))
            b.element = category.element1
            f.add_widget(b)

            b2 = ButtonImage(on_press=pressed, source=category.element2.source, size=size, size_img=size,
                             pos=(2 * margin + end_height_element, start - end_height_element * i))
            b2.element = category.element2
            f.add_widget(b2)

    # disable background (visually and programmatically)
    def background_enable(self):
        self.button_enabled = True
        self.shadow.label.background_color = 1, 1, 1, 0.0

    def background_disable(self):
        self.button_enabled = False
        self.shadow.label.background_color = 1, 1, 1, 0.5
        self.frame.remove_widget(self.shadow)
        self.frame.add_widget(self.shadow)

    # welcome tutorial: happy guy speaking
    def init_welcome_tuto(self):
        # at the very start, animate add the point gauge
        speed = 1
        anim = Animation(y=sizes.cursor_pos_y(0), duration=speed)
        anim += Animation(y=sizes.cursor_pos_y(2 * sizes.gauge_number), duration=2 * speed)
        anim += Animation(y=sizes.cursor_pos_y(sizes.gauge_number), duration=speed)
        anim.start(self.cursor.image)

        # welcoming guy
        self.guy = ImageWrap(pos=sizes.human_pos,
                             size=sizes.human_size,
                             source='images/animations/human/hipster_sways.zip')
        self.guy.image.anim_delay = 0.3
        self.guy.image.anim_loop = 0
        self.frame.add_widget(self.guy)

        self.speach = LabelWrap(size=(sizes.speach_width, sizes.speach_height),
                                pos=sizes.speach_pos,
                                text=txt.txt_scenery_notxt,
                                font_size=sizes.font_size_large)
        self.speach.label.text = txt_game_move_play.get()
        self.speach.label.padding = (4, 0)
        self.speach.label.background_color = 1, 1, 1, 0.8
        self.frame.add_widget(self.speach)

        self.frame.add_widget(ImageWrap(source='images/non_animes/speach_bubble.png',
                                        pos=(sizes.speach_pos[0] - 4, sizes.speach_pos[1] - 50 - 4),
                                        size=(sizes.speach_width + 8, sizes.speach_height + 50 + 8)))

    def init_category_struct(self):
        self.categories = init_category_struct(self.frame)
        #re-schuffle
        self.categories = random.sample(self.categories, self.categories.__len__())
        self.gameturn_setup(self.categories[self.nb_current_category])

    def category_forward(self, *any):
        if (self.button_enabled & self.button_cat_enabled):
            if (self.nb_current_category < sizes.category_number):
                self.speach.label.text = txt_game_move_pass.get()
                self.anim_points(0, 0, 0, self.none)
                self.category_clean()
                self.category_next(any)

    def category_clean(self):
        self.frame.remove_widget(self.current_category.target)
        self.frame.remove_widget(self.current_category.element1)
        self.frame.remove_widget(self.current_category.element2)

    def category_next(self, *any):
        if (self.nb_current_category < sizes.category_number):
            self.nb_current_category += 1
            self.category_scale.image.size = (
                sizes.category_width_progress(self.nb_current_category), sizes.category_height)

        if (self.nb_current_category < sizes.category_number):
            # update text and forward to next category
            self.category_text.update_cat(self.nb_current_category)
            self.gameturn_setup(self.categories[min(self.nb_current_category, self.categories.__len__() - 1)])

        elif (self.nb_current_category == sizes.category_number):
            # end of game, see results and get a feedback before leaving'
            self.category_clean()

            self.category_desc.label.text = txt_scenery_notxt.get()
            self.elem_first_desc.label.text = txt_scenery_notxt.get()
            self.elem_second_desc.label.text = txt_scenery_notxt.get()
            self.category_text.label.text = txt_scenery_notxt.get()

            self.category_text.label.text = txt_end_category.get()
            txt_score = txt_end_score
            txt_point = txt_end_points

            if self.points >= -1 & self.points <= 1:
                txt_point = txt_end_point

            txt = txt_end_level3
            if self.points < 0:
                txt_score.color = color.magenta
                txt_point.color = color.magenta
            if self.points >= 0:
                txt = txt_end_level2
                txt_score.color = color.orange
                txt_point.color = color.orange
            if self.points >= 3:
                txt = txt_end_level1
                txt_score.color = color.green
                txt_point.color = color.green
            watermark = LabelWrap(
                pos=(sizes.width_left_margin, sizes.pos_c2[1]),
                size=(sizes.width_game, sizes.height_button_small * 2),
                text=txt,
                font_size=sizes.font_size_large
            )

            self.speach.label.text = txt_score.get() + str(self.points) + txt_point.get()

            self.frame.add_widget(watermark)
            watermark.label.background_color = 1, 1, 1, 0.25

            self.delete_pseudo_static_UI()
            self.init_end_of_game_UI()

            music_alt.play()
            music.stop()

    # does nothing, used for no action after animation
    def none(self, *any):
        pass

    # animates a smile (and not a points mark) towards scale from the happening area
    def anim_points(self, points, x_start, y_start, fct_next):
        size = 20
        size_final = 200
        x_final = sizes.width - size_final
        y_final = (sizes.height - size_final) / 2
        y_shift = 300
        points_image = ImageWrap(size=(size, size),
                                 pos=(x_start, y_start),
                                 source='images/scenery/points_neutre_500x500px.png')
        d = 1
        if (points > 0):
            points_image.image.source = 'images/scenery/smile_positif_210x200px.png'
            y_final += y_shift
            d *= 2
        elif (points < 0):
            points_image.image.source = 'images/scenery/smile_negatif_210x200px.png'
            y_final -= y_shift
            d *= 2

        self.frame.add_widget(points_image)

        def remove(anim, widget):
            # update cursor at the end of smiley movement
            self.update_cursor()
            self.frame.remove_widget(points_image)
            fct_next(self)

        anim_points = Animation(size=(size_final, size_final), duration=d)
        anim_points &= Animation(x=x_final, y=y_final, duration=d, t='in_quad')
        anim_points.bind(on_complete=remove)
        anim_points.start(points_image.image)

    def start_game_tuto(self):
        window_frame = win_generate(text_title=txt.txt_tutorial_welcome_p0)

        def on_press(*any):
            self.frame.remove_widget(window_frame)
            self.init_category_struct()
            self.background_enable()

        window_frame.add_widget(ButtonImageText(
            on_press=on_press,
            pos=(win_dx(sizes.win_width - sizes.win_width_infos), win_dy(sizes.win_height - sizes.win_header)),
            size=(sizes.win_width_infos, sizes.win_header),
            source_back='images/scenery/back_80x183px_green.png',
            size_img=(sizes.win_header / 2, sizes.win_header),
            source='images/scenery/fleche_seule_23x44px_white.png',
            text=txt_tutorial_play,
            left=sizes.win_width_infos - sizes.win_header / 2))

        window_frame.label.label.text = txt.txt_tutorial_welcome_p1.get()

        self.background_disable()
        self.frame.add_widget(window_frame)

    def more_infos(self, element, fct, negative=True, alternate=False):
        window_frame = win_generate(text_title=element.name)

        def close(screen):
            self.frame.remove_widget(window_frame)
            if negative:
                fct()
            else:
                self.background_enable()
                self.category_next(None)
                # forward category allowed after positive animation!
                self.button_cat_enabled = True

        button_switch = not negative if alternate else negative
        if button_switch:
            window_frame.add_widget(ButtonImageText(
                on_press=close,
                pos=(win_dx(sizes.win_width - sizes.win_header), win_dy(sizes.win_height - sizes.win_header)),
                size=(sizes.win_header, sizes.win_header),
                source_back='images/scenery/back_80x183px_red.png',
                size_img=(sizes.win_header, sizes.win_header),
                source='images/scenery/picto_croix_150x150px.png',
                text=txt_scenery_notxt,
                left=0))
        else:
            window_frame.add_widget(ButtonImageText(
                on_press=close,
                pos=(
                    win_dx(sizes.win_width - sizes.win_width_infos), win_dy(sizes.win_height - sizes.win_header)),
                size=(sizes.win_width_infos, sizes.win_header),
                source_back='images/scenery/back_80x183px_green.png',
                size_img=(sizes.win_header / 2, sizes.win_header),
                source='images/scenery/fleche_seule_23x44px_white.png',
                text=txt_interact_forward,
                left=sizes.win_width_infos - sizes.win_header / 2))

        window_frame.label.label.text = element.txt_info.get()
        window_frame.image.source = element.info_img

        # special cat case
        if (element.name == txt.txt_cat_animal_cat):
            # re-adapt image size (but not dots....)
            def after(*any):
                v = window_frame.label.label.anchors['end']
                window_frame.image.size[1] = sizes.win_height - sizes.win_header - v[1] - sizes.font_size_large - 2 * 10

            def next_solutions(any):
                window_frame.label.label.text = element.txt_info_alt.get()
                window_frame.image.source = element.info_img_alt
                window_frame.remove_widget(solutions)
                Clock.schedule_once(after, 1 / 4)

            solutions = ButtonImageText(
                on_press=next_solutions,
                pos=(win_dx((sizes.win_width - 200) / 2), win_dy(sizes.win_header * 1.5)),
                size=(200, 97),
                source_back='images/scenery/fenetre_infos_200x97px_green.png',
                size_img=(23, 44),
                source='images/scenery/fleche_seule_23x44px_white.png',
                text=txt_interact_solutions,
                font_size=sizes.font_size_subtitle,
                left=160)
            window_frame.add_widget(solutions)

        if (not negative):
            self.background_disable()
        self.frame.add_widget(window_frame)
        return window_frame

    def stop_game_ask(self, *any):
        if (self.button_enabled & self.button_cat_enabled):
            # open window to ask confirmation to reset/stop game', except if game is finished => stop immediately
            if (self.nb_current_category == self.categories.__len__()):
                self.stop_game()
            else:
                self.stop_game_warning(timeout=False)

    def stop_game(self, timeout=False, *any):
        if self.game_running:
            t = 'timeout' if timeout else 'quit'
            # end, end_reason, points, category_seen, category_used
            save_entry(file="~/Desktop/garden.csv", opt="end, " + t +", " + str(self.points) + "," + str(self.nb_current_category) + "," + str(self.nb_current_category__used))

            self.game_running = False
            if self.frame.cat_reverse:
                self.frame.cat.flip()

            self.fail_interact_trial = 0
            self.easy_interact_mode = False

            # stop the music
            music.stop()
            music_alt.stop()
            self.previous.return_to_screen()
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

    # setup for category game turn, tear down is handled somewhere else
    def gameturn_setup(self, category):
        self.current_category = category

        # target area to carry elements
        self.frame.add_widget(category.target)
        self.frame.remove_widget(self.guy)
        self.frame.add_widget(self.guy)

        # positive and negative elements to drag & drop
        self.frame.add_widget(category.element1)
        self.frame.add_widget(category.element2)
        self.category_desc.label.text = category.name.get()
        self.category_desc.bolden()
        if (category.element1.first):
            t1 = category.element1.name.get()
            t2 = category.element2.name.get()
        else:
            t2 = category.element1.name.get()
            t1 = category.element2.name.get()
        self.elem_first_desc.label.text = t1
        self.elem_second_desc.label.text = t2

    # animated guy: happy, wrath, sways
    def hipster(self, points):
        if (points < 0):
            self.guy.image.source = 'images/animations/human/hipster_wrath.zip'
            self.guy.image.anim_delay = 0.2
            self.guy.image.anim_loop = 5
        elif (points > 0):
            self.guy.image.source = 'images/animations/human/hipster_happy.zip'
            self.guy.image.anim_delay = 0.1
            self.guy.image.anim_loop = 5
        else:
            self.guy.image.source = 'images/animations/human/hipster_sways.zip'
            self.guy.image.anim_delay = 0.3
            self.guy.image.anim_loop = 0

    def hipster_sways_after(self):
        def after(*any):
            self.hipster(0)

        anim = Animation(duration=4)
        anim.bind(on_complete=after)
        anim.start(self.static.image)

    def anim_animal(self, element, points, alt=False):
        #trigger no timeout during animation
        self.timeout_touch()
        def after(*any):
            # remove the animal or make sure it disappear
            self.frame.remove_widget(animal)
            #trigger timeout from END of animation
            self.timeout_touch()

            # self.hipster(0)
            if (points > 0):
                self.after_positive(element)
            else:
                self.after_negative(element)

        # animation of animals
        self.frame.static = self.static
        animal = element.anim_setup()
        animal.static = self.static

        def after_start(*any):
            # trigger no timeout during animation
            self.timeout_touch()
            if (alt):
                anim_end = element.anim_end_alt(animal)
            else:
                anim_end = element.anim_end(animal)
            anim_end.bind(on_complete=after)
            anim_end.start(animal.image)

            self.anim_points(points, element.event_pos[1], element.event_pos[1], fct_next=self.none)

        anim_start = element.anim_start()
        anim_start.bind(on_complete=after_start)
        anim_start.start(animal.image)

    # should be called anywhere a touch is made, to update last_lcik and schedule the timeout check
    def timeout_touch(self):
        self.last_click = time.time()
        Clock.schedule_once(self.timeout_check, timeout + 1)

    #check if timeout has expired and launch the warning
    def timeout_check(self, dt):
        current = time.time()
        if (current - self.last_click) > timeout:
            # goes to warning ONLY if no other timeout warning is running
            if self.timeout_warning_off:
                self.stop_game_warning(timeout=True)

    #warns the user about timeout, and end game after timeout_window_conf if no action taken
    def stop_game_warning(self, timeout=False):
        self.timeout_warning_off = False
        window_frame = win_generate(text_title=txt_interact_stop_title)

        should_stop = True
        def stop_game(*any):
            if should_stop:
                self.timeout_warning_off = True
                self.stop_game(timeout)

        event = Clock.schedule_once(stop_game, timeout_window_conf)

        def forward(*any):
            should_stop = False
            event.cancel()
            self.frame.remove_widget(window_frame)
            self.timeout_touch()
            self.background_enable()
            self.timeout_warning_off = True

        if timeout:
            window_frame.label.label.text = txt_interact_timeout.get()
        else:
            window_frame.label.label.text = txt_interact_confirm.get()

        window_frame.add_widget(ButtonImageText(
            on_press=forward,
            pos=(win_dx(sizes.win_width - sizes.win_width_infos), win_dy(sizes.win_height - sizes.win_header)),
            size=(sizes.win_width_infos, sizes.win_header),
            source_back='images/scenery/back_80x183px_green.png',
            size_img=(33, sizes.win_header),
            source='images/scenery/fleche_seule_23x44px_white.png',
            text=txt_interact_forward,
            left=sizes.win_width_infos - 33))


        # add a stop and continue buttons in timeout window
        left = win_dx((sizes.win_width - 2 * sizes.win_width_infos) / 3)
        right = win_dx((sizes.win_width - 2 * sizes.win_width_infos) / 3 * 2) + sizes.win_width_infos
        up = win_dy((sizes.win_height - 2 * sizes.win_header) / 2) + sizes.win_header
        down = up - sizes.win_header

        window_frame.add_widget(LabelWrap(
            pos=(left,up),
            size=(sizes.win_width_infos, sizes.win_header),
            text=txt_interact_continue))

        window_frame.add_widget(ButtonImageText(
            on_press=forward,
            pos=(left, down),
            size=(sizes.win_width_infos, sizes.win_header),
            source_back='images/scenery/back_80x183px_green.png',
            size_img=(35, sizes.win_header),
            source='images/scenery/fleche_seule_23x44px_white.png',
            text=txt_interact_forward,
            left=sizes.win_width_infos - 35))

        window_frame.add_widget(LabelWrap(
            pos=(right, up),
            size=(sizes.win_width_infos, sizes.win_header),
            text=txt_interact_stop))

        window_frame.add_widget(ButtonImageText(
            on_press=stop_game,
            pos=(right, down),
            size=(sizes.win_width_infos, sizes.win_header),
            source_back='images/scenery/back_80x183px_red.png',
            size_img=(sizes.win_header,sizes.win_header),
            source='images/scenery/picto_croix_150x150px.png',
            text=txt_interact_stop_short,
            left=sizes.win_width_infos - sizes.win_header))

        # add 3-language information
        window_frame.add_widget(LabelWrap(
            pos=(left, down - 3 * sizes.win_header),
            size=(sizes.win_width - 2 * sizes.win_width_infos, sizes.win_width_infos),
            text=txt_interact_confirm_lang_multi))


        self.background_disable()
        self.frame.add_widget(window_frame)

    # triggered for EVERY touch MOVE on any element of this screen
    def on_touch_move(self, touch):
        self.timeout_touch()
        return False

    # triggered for EVERY touch UP on any element of this screen
    def on_touch_up(self, touch):
        self.timeout_touch()
        element = self.currentObj
        # react only to element scatter moves ended to right target area
        if (self.button_enabled & isinstance(element, ElementScatter)):
            target = self.current_category.target
            # automatize placement for detection, static image & animation
            # check collision, object placed OR EAZY mode and no placement needed
            self.currentObj = ObjectProperty(None)
            if (target.image.collide_widget(element) or self.easy_interact_mode):
                # don't forward category during animation!
                self.button_cat_enabled = False
                # put the real object in place of target (suppose both elements have same size!)
                self.static = ImageWrap(size=target.image.size,
                                        pos=target.image.pos,
                                        source=element.image.source)
                self.frame.add_widget(self.static)
                self.frame.remove_widget(self.guy)
                self.frame.add_widget(self.guy)

                # text speach update
                if (not element.positive):
                    self.speach.label.text = txt_game_move_negative.get()
                else:
                    self.speach.label.text = txt_game_move_positive.get()
                    self.hipster_sways_after()

                points = 1 if element.positive else -1
                self.points += points
                self.hipster(points)

                # does the animation
                # after the aniamtion, will move to text info + other category
                self.anim_animal(element, points)

                anim_wid = Animation(x=element.x_orig, y=element.y_orig)
                anim_wid.start(element)

                # disable all other widget in category selection
                self.category_clean()
                self.nb_current_category__used += 1

                if not self.easy_interact_mode:
                    self.fail_interact_trial = 0
            else:
                # object not placed, return to place and text changed
                anim = Animation(x=element.x_orig, y=element.y_orig)
                anim.start(element)
                self.speach.label.text = txt_game_move_unreached.get()

                #after 3 failed trials IN A ROW, activate the "easy_selection" mode, and the 3rd, 4st and all subsequent trials will be "EAZY"
                self.fail_interact_trial += 1
                if (self.fail_interact_trial >= 2):
                    self.easy_interact_mode = True
                    self.on_touch_up(touch)

    # after negative scenario
    def after_positive(self, element):
        self.more_infos(element, fct=self.none, negative=False)

    # after negative scenario
    def after_negative(self, element):
        window_frame = win_generate(text_title=txt.txt_recover_header)

        #if info window was optionnally opened during the choices, then no pop-up. Otherwise, forec the use to see it.
        self.win_neg_open_more_infos = False
        def more_infos(screen):
            self.win_neg_open_more_infos = True
            self.more_infos(element, fct=self.none)

        window_frame.add_widget(ButtonImageText(
            on_press=more_infos,
            pos=(win_dx(sizes.win_width - sizes.win_width_infos), win_dy(sizes.win_height - sizes.win_header)),
            size=(sizes.win_width_infos, sizes.win_header),
            source_back='images/scenery/back_80x183px_green.png',
            size_img=(sizes.win_header, sizes.win_header),
            source='images/scenery/picto_info_63x63px.png',
            text=txt_recover_infos,
            left=sizes.win_width_infos - sizes.win_header))

        # replace by positive element
        def replace(screen):
            def fct(**any):
                pt = 2
                self.points += pt
                self.static.image.source = element.positive_ref.source
                self.anim_animal(element.positive_ref, pt)

                # text speach update
                self.speach.label.text = txt_game_move_positive.get()
                self.hipster(pt)
                after_all_choices()


            if self.win_neg_open_more_infos:
                fct()
            else:
                self.more_infos(element, fct=fct, negative=True, alternate=True)

        # add a correction to negative elements
        def correct(screen):
            pt = 1
            self.points += pt
            # add the correcting element and run the altenative negative animation
            self.frame.add_widget(element.correction_img)
            self.anim_animal(element, pt, alt=True)

            # text speach update
            self.speach.label.text = txt_game_move_positive.get()
            self.hipster(pt)
            after_all_choices()

        # keep and remove have no animation
        def remove(screen):
            def fct(**any):
                self.points += 1
                self.frame.remove_widget(self.static)

                # special cat case
                if (self.static.image.source == 'images/animations/animaux/chat_couche_loop.zip'):
                    self.tree.image.source = 'images/non_animes/arbre_oiseau.png'

                # text speach update
                self.speach.label.text = txt_game_move_play.get()
                self.hipster(0)
                self.update_cursor()
                after_all_choices()
                self.category_next(None)
                # forward category allowed after positive animation!
                self.button_cat_enabled = True

            if self.win_neg_open_more_infos:
                fct()
            else:
                self.more_infos(element, fct=fct, negative=True, alternate=True)

        # keep the object
        def keep(screen):
            def fct(**any):
                # text speach update
                self.speach.label.text = txt_game_move_play.get()
                self.hipster(0)
                after_all_choices()
                self.category_next(None)
                # forward category allowed after positive animation!
                self.button_cat_enabled = True

            if self.win_neg_open_more_infos:
                fct()
            else:
                self.more_infos(element, fct=fct, negative=True, alternate=True)

        # remove the recover window and update cursor
        def after_all_choices():
            self.frame.remove_widget(window_frame)
            self.hipster_sways_after()
            self.background_enable()
            self.win_neg_open_more_infos = False

        class ButtonImageChoicesKeep(ButtonImageChoices):
            def __init__(self, element, pos):
                self.pos = pos
                text = txt.txt_recover_keep
                super(ButtonImageChoicesKeep, self).__init__(keep, pos, text)

                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=element.source))

        class ButtonImageChoicesRemove(ButtonImageChoices):
            def __init__(self, element, pos):
                self.pos = pos
                text = txt.txt_recover_remove
                super(ButtonImageChoicesRemove, self).__init__(remove, pos, text)

                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=element.source))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source='images/scenery/picto_croix_112x112px.png'))

        class ButtonImageChoicesReplace(ButtonImageChoices):
            def __init__(self, element, pos):
                self.pos = pos
                text = txt.txt_recover_replace
                super(ButtonImageChoicesReplace, self).__init__(replace, pos, text)

                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source='images/scenery/fleche_seule_23x44px.png'))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=element.image.source))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source='images/scenery/picto_croix_112x112px.png'))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_right, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=element.positive_ref.image.source))

        class ButtonImageChoicesCorrect(ButtonImageChoices):
            def __init__(self, element, pos):
                self.pos = pos
                text = txt.txt_recover_correct
                super(ButtonImageChoicesCorrect, self).__init__(correct, pos, text)

                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_center, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source='images/scenery/fleche_seule_23x44px.png'))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_left, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=element.correction_no))
                self.add_widget(
                    ImageWrap(pos=(pos[0] + sizes.win_choice_inner_right, pos[1] + sizes.win_choice_inner_margin),
                              size=(sizes.win_choice_img_size, sizes.win_choice_img_size),
                              source=element.correction_yes))

        # random placement of windows
        pos1 = (win_dx(sizes.win_choice_right), win_dy(sizes.win_choice_down))
        pos2 = (win_dx(sizes.win_choice_left), win_dy(sizes.win_choice_up))
        pos3 = (win_dx(sizes.win_choice_right), win_dy(sizes.win_choice_up))
        pos4 = (win_dx(sizes.win_choice_left), win_dy(sizes.win_choice_down))
        pos = {pos1, pos2, pos3, pos4}
        pos = random.sample(pos, pos.__len__())

        # initiate a correction recover
        window_frame.add_widget(ButtonImageChoicesReplace(element, pos[0]))
        window_frame.add_widget(ButtonImageChoicesRemove(element, pos[1]))
        window_frame.add_widget(ButtonImageChoicesKeep(element, pos[2]))
        if (element.correction):
            window_frame.add_widget(ButtonImageChoicesCorrect(element, pos[3]))

        self.background_disable()
        self.frame.add_widget(window_frame)


# main application class
class TouchGardenApp(App):
    # changes window title
    title = txt.txt_main_title_short

    def __init__(self, **kwargs):
        super(TouchGardenApp, self).__init__(**kwargs)

        # initialize new ScreenManager for handling screens
        self.manager = ScreenManager()

    def build(self):
        # set starting screen, quiz or game
        if quiz_enabled:
            self.manager.switch_to(StatsScreen(name="QuizStartScreen"))
        else:
            self.manager.switch_to(StartScreen(name="TouchGarden StartScreen"))
        return self.manager


# launch the app
if __name__ == '__main__':
    TouchGardenApp().run()
