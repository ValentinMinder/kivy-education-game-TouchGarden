# must be imported first to prevent issues
from kivy.config import Config
Config.set('graphics', 'width', 1366)
Config.set('graphics', 'height', 768)

from kivy.app import App
from kivy.uix.button import Button

from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

# loading widget instructions
Builder.load_file('screens.kv')
Builder.load_file('widgets.kv')

# ease-of-access for the only screenmanager in use
MANAGER = None

# pre-load game music
music = SoundLoader.load("audio/garden_base.wav")

# specialized version of screen that handles keyboard presses and has a cursor system,
# used for all the screens outside the loading screen
class KeyScreen(Screen):
    pass

# screen corresponding to the main menu
class MainMenuScreen(KeyScreen):
    pass

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
        #return Button(text='Hello World')

# launch the app
if __name__ == '__main__':
    TouchGardenApp().run()