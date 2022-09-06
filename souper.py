from bs4 import BeautifulSoup
from requests import get

class Weather:
    def __init__(self):
        self.days = ['today', 'tomorrow', 'in+two+days', 'in+three+days', 'in+four+days', 'in+five+days', 'in+six+days', 'in+seven+days']
        

    def get_week_weather(self, location):
        self.weather_list = []
        print("Weather app initializing")
        try:
            for day in self.days:
                weather = tuple(BeautifulSoup(get(f'https://google.com/search?q=weather+in+{location.lower().replace(" ", "+")}+{day}').content, 'html.parser').find('div', class_ = 'BNeawe tAd8D AP7Wnd').div.div.text.split('\n'))
                self.weather_list.append(weather)
            return self.weather_list
        except:
            return "No Internet"

    def get_day_weather(self, location, day):
        try:
            weather = tuple(BeautifulSoup(get(f'https://google.com/search?q=weather+in+{location.lower().replace(" ", "+")}+{day}').content, 'html.parser').find('div', class_ = 'BNeawe tAd8D AP7Wnd').div.div.text.split('\n'))
            return weather
        except:
            return "No Internet"

#print(Weather().get_day_weather('Makurdi', 'in three days'))