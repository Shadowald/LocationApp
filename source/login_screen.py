from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty

# Window.size = (300, 500)
# users_map = {}
users_map = {'email@address.com': 'password'}


class LoginScreen(Screen):
    email = ObjectProperty("")
    password = ObjectProperty("")

    def login(self):

        # Confirm the TextField for user_email and user_password are not empty
        if self.ids.user_email.text == "":
            self.ids.user_email.helper_text = "Please enter an email address"
            self.ids.user_email.error = True
            return 1

        # Else there is no error, helper_text is cleared as it persists when an error is raised
        self.ids.user_email.helper_text = ""

        if self.ids.user_password.text == "":
            self.ids.user_password.helper_text = "Please enter your password"
            self.ids.user_password.error = True
            return 1

        # Else there is no error, helper_text is cleared as it persists when an error is raised
        self.ids.user_password.helper_text = ""

        # Confirm user_email and user_password exist in the users_map, ie is a registered user
        if users_map.get(self.ids.user_email.text) is None:
            self.ids.user_email.helper_text = "Your email was incorrect"
            self.ids.user_email.error = True
            return 2
        elif users_map[self.ids.user_email.text] != self.ids.user_password.text:
            self.ids.user_password.helper_text = "Your password was incorrect"
            self.ids.user_password.error = True
            return 2

        # Login successful
        self.email = self.ids.user_email.text
        self.password = self.ids.user_password.text
        return 0

    def set_email_text(self, email):
        self.ids.user_email.text = email

    def set_password_text(self, password):
        self.ids.user_password.text = password



