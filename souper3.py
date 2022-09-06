from multiprocessing import Pool
from bs4 import BeautifulSoup
from requests import get

class Weather:
    def __init__(self):
        self.days = ['today', 'tomorrow', 'in+two+days', 'in+three+days', 'in+four+days', 'in+five+days', 'in+six+days']
        print("Weather app initializing")

    def get_weather(self, day):
        bs = BeautifulSoup(get(f'https://google.com/search?q=weather+in+{self.location.lower().replace(" ", "+")}+{day}').content, 'html.parser')
        weather = tuple(bs.find('div', class_ = 'BNeawe tAd8D AP7Wnd').div.div.text.split('\n'))
        self.weather_list.append(weather)
        print(weather)

    def get_week_list(self, location):
        self.location = location
        self.weather_list = []
        with Pool(6) as p:
            p.map(self.get_weather, [self.days[0],self.days[1],self.days[2],self.days[3],self.days[4],self.days[5],self.days[6]])
        #t1 = Process(target = self.get_weather, args=(location, self.days[0])).start()
        #t2 = Process(target = self.get_weather, args=(location, self.days[1])).start()
        #t3 = Process(target = self.get_weather, args=(location, self.days[2])).start()
        #t4 = Process(target = self.get_weather, args=(location, self.days[3])).start()
        #t5 = Process(target = self.get_weather, args=(location, self.days[4])).start()
        #t6 = Process(target = self.get_weather, args=(location, self.days[5])).start()

        return self.weather_list


print(Weather().get_week_list('Makurdi'))