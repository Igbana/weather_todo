import threading
from bs4 import BeautifulSoup
from requests import get

class Weather:
    def __init__(self):
        self.days = ['today', 'tomorrow', 'in+two+days', 'in+three+days', 'in+four+days', 'in+five+days', 'in+six+days']
        print("Weather app initializing")

    def get_weather(self, location, day):
        bs = BeautifulSoup(get(f'https://google.com/search?q=weather+in+{location.lower().replace(" ", "+")}+{day}').content, 'html.parser')
        weather = tuple(bs.find('div', class_ = 'BNeawe tAd8D AP7Wnd').div.div.text.split('\n'))
        self.weather_list.append(weather)

    def get_week_list(self, location):
        self.weather_list = []
        t1 = threading.Thread(target = self.get_weather, args=(location, self.days[0]))
        t2 = threading.Thread(target = self.get_weather, args=(location, self.days[1]))
        t3 = threading.Thread(target = self.get_weather, args=(location, self.days[2]))
        t4 = threading.Thread(target = self.get_weather, args=(location, self.days[3]))
        t5 = threading.Thread(target = self.get_weather, args=(location, self.days[4]))
        t6 = threading.Thread(target = self.get_weather, args=(location, self.days[5]))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()

        return self.weather_list


print(Weather().get_week_list('Makurdi'))