import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


kivy.require("1.10.0")
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class GameApp(App):

    def build(self):
        window = MainWindow()
        return window

    def quit(self):
        print("Quit code goes here!")


class MainWindow(ScreenManager):
    pass


