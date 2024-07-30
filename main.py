from kivymd.app import MDApp
from kivy.lang.builder import Builder


class LocationApp(MDApp):

    def build(self):
        screen = Builder.load_string('')

        return screen


LocationApp().run()
