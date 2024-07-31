from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

helper = """
Screen:

    Image:
        source: 'logo.png'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        allow_stretch: True
        keep_ratio: True
        size_hint_x: None
        size_hint_y: None
        width: self.parent.width / 2
        height: self.parent.height / 3
        
    MDTextField:
        hint_text: "Enter Username"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: self.parent.width / 1.5
        
    MDTextField:
        hint_text: "Enter Password"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: self.parent.width / 1.5
    
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
"""

Window.size = (300, 500)


class LocationApp(MDApp):

    def build(self):
        screen = Builder.load_string(helper)

        return screen


LocationApp().run()
