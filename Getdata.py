from bs4 import BeautifulSoup
import requests

class data:
    def __init__(self):
        site = requests.get(
            "https://www.msn.com/tr-tr/havadurumu/bugun/K%c4%b1r%c5%9fehir,K%c4%b1r%c5%9fehir,T%c3%bcrkiye/we-city?iso=TR&savedegree=true&weadegreetype=C&el=NiUxJbaGme%2B3jauW51qnqQ%3D%3D")
        source = BeautifulSoup(site.content, "html.parser")
        self.linkler = source.find('span', {'class': 'current'}).text
    def goster(self):
        sicaklik =  f'{self.linkler}°'
        return sicaklik
