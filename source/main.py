from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import StringProperty
import darkdetect
import login_screen

# TODO: Replace logo.png with a real logo for the app

# Hierarchy:
#   LocationApp (MDApp)
#   |- ScreenManager (MDScreenManager)
#      |- LoginScreen (Screen)

Window.size = (300, 500)


class ScreenManager(MDScreenManager):
    def screen_manager(self):
        pass


class LocationApp(MDApp):
    screen = None

    def build(self):
        # Set theme of the app to the set theme of the device, default theme in Kivy is 'Light'
        if darkdetect.theme() == "Dark":
            self.theme_cls.theme_style = 'Dark'

        return self.screen


#LocationApp().run()
