import kivy
from kivy.config import Config
from . import core

kivy.require("1.10.0")
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

app = core.GameApp


