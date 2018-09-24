from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from ..session import Session

INTERVAL = 0.05


class GameApp(App):
    session = Session()
    manager = None

    def build(self):
        self.manager = MainWindow()
        return self.manager

    def new_game(self):
        self.manager.current = "game_screen"
        Clock.schedule_interval(self.update, INTERVAL)

    def update(self, *args):
        if self.manager.current == "game_screen":
            self.session.advance()
            self.manager.current_screen.ids.lbl_time.text = self.session.time

    def quit(self):
        self.stop()


class MainWindow(ScreenManager):
    pass


