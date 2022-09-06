from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from souper import Weather

class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    #weather_info = ListProperty(Weather().get_day_weather('Makurdi', 'tomorrow'))
    day = StringProperty()
    location = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.day)


class HomeScreen(MDScreen):
    Builder.load_file('home.kv')
    def __init__(self, **kw):
        super().__init__(**kw)



class MainApp(MDApp):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    MainApp().run()