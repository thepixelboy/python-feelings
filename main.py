from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("design.kv")


class LoginScreen(Screen):
    ...


class RootWidget(ScreenManager):
    ...


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
