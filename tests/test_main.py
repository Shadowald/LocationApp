import pytest
import source.main as main
from kivymd.app import MDApp


class TestLocationApp:

    def setup_method(self, method):
        self.app = main.LocationApp()
        self.app.build()
        self.app.users_map['email@address.com'] = 'password'

    def test_login_empty_email_field(self):
        self.app.screen.ids.user_email.text = ""
        result = self.app.login(None)
        assert result == 1

    def test_login_empty_password_field(self):
        self.app.screen.ids.user_email.text = "a"
        self.app.screen.ids.user_password.text = ""
        result = self.app.login(None)
        assert result == 1

    def test_login_incorrect_email_field(self):
        self.app.screen.ids.user_email.text = "a"
        self.app.screen.ids.user_password.text = "a"
        result = self.app.login(None)
        assert result == 2

    def test_login_incorrect_password_field(self):
        self.app.screen.ids.user_email.text = "email@address.com"
        self.app.screen.ids.user_password.text = "a"
        result = self.app.login(None)
        assert result == 2

    def test_login_successful_login(self):
        self.app.screen.ids.user_email.text = "email@address.com"
        self.app.screen.ids.user_password.text = "password"
        result = self.app.login(None)
        assert result == 0
