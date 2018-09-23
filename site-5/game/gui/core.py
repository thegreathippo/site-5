from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ..session import Session


class GameApp(App):
    session = None
    manager = None

    def build(self):
        self.manager = MainWindow()
        return self.manager

    def new_game(self):
        self.session = Session()
        self.manager.current = "game_screen"

    def quit(self):
        self.stop()


class MainWindow(ScreenManager):
    pass


