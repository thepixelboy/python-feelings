import glob
import json
import random
from datetime import datetime
from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager

from hoverable import HoverBehavior

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)

        if (username in users) and (users[username]["password"] == password):
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_failed.text = (
                "Wrong username or password. Please, try again."
            )


class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        feelings = glob.glob("quotes/*.txt")
        feelings = [Path(filename).stem for filename in feelings]

        if feel in feelings:
            with open(f"quotes/{feel}.txt") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling: happy, sad, unloved"


class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open("users.json") as file:
            users = json.load(file)

        users[username] = {
            "username": username,
            "password": password,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        }

        with open("users.json", "w") as file:
            json.dump(users, file)

        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login_screen(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):
    ...


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    ...


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
