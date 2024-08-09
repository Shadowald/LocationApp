from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
import darkdetect

# TODO: Replace logo.png with a real logo for the app
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
        id: user_email
        hint_text: "Enter Email"
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: self.parent.width / 1.5
        
    MDTextField:
        id: user_password
        hint_text: "Enter Password"
        helper_text_mode: "on_error"
        password: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint_x: None
        width: self.parent.width / 1.5
    
    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .35}
        pos: user_password.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            user_password.password = False if user_password.password is True else True
    
    MDRectangleFlatButton:
        id: login_button
        text: 'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
"""

Window.size = (300, 500)


class LocationApp(MDApp):
    email = StringProperty("")
    password = StringProperty("")
    screen = None
    users_map = {}

    def build(self):
        # Set theme of the app to the set theme of the device, default theme in Kivy is 'Light'
        if darkdetect.theme() == "Dark":
            self.theme_cls.theme_style = 'Dark'

        self.screen = Builder.load_string(helper)

        # Bind widgets to login function
        self.screen.ids.user_email.bind(
            on_text_validate=self.login
        )
        self.screen.ids.user_password.bind(
            on_text_validate=self.login
        )
        self.screen.ids.login_button.bind(
            on_release=self.login
        )

        return self.screen

    def login(self, args):

        # Confirm the TextField for user_email and user_password are not empty
        if self.screen.ids.user_email.text == "":
            self.screen.ids.user_email.helper_text = "Please enter an email address"
            self.screen.ids.user_email.error = True
            return 1

        # Else there is no error, helper_text is cleared as it persists when an error is raised
        self.screen.ids.user_email.helper_text = ""

        if self.screen.ids.user_password.text == "":
            self.screen.ids.user_password.helper_text = "Please enter your password"
            self.screen.ids.user_password.error = True
            return 1

        # Else there is no error, helper_text is cleared as it persists when an error is raised
        self.screen.ids.user_password.helper_text = ""

        # Confirm user_email and user_password exist in the users_map, ie is a registered user
        if self.users_map.get(self.screen.ids.user_email.text) is None:
            self.screen.ids.user_email.helper_text = "Your email was incorrect"
            self.screen.ids.user_email.error = True
            return 2
        elif self.users_map[self.screen.ids.user_email.text] != self.screen.ids.user_password.text:
            self.screen.ids.user_password.helper_text = "Your password was incorrect"
            self.screen.ids.user_password.error = True
            return 2

        # Login successful
        self.email = self.screen.ids.user_email.text
        self.password = self.screen.ids.user_password.text
        return 0

# LocationApp().run() TODO: Refactor code for main to only run app and to build in a separate file for testing purposes
