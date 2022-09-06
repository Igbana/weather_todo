from random import randint
from time import sleep
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder


class SplashScreen(MDScreen):
    Builder.load_file('splash.kv')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ListItem(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_y = None
        self.height = '60dp'
        self.radius = 10
        self.pos_hint = {'center_x': 0.5}
        # self.md_bg_color = [randint(0,255)/255, randint(0,255)/255, randint(0,255)/255, 0.2]

class HomeScreen(MDScreen):
    Builder.load_file('home.kv')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MainApp(MDApp):
    def build(self):
        return HomeScreen()

if __name__=="__main__":
    MainApp().run()