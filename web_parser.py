import requests
from bs4 import BeautifulSoup

class IMDBSeriesIDParser:
    def __init__(self, series_id: str, season_num: str):
        self.url = 'https://www.imdb.com/title/{0}/episodes?season={1}'.format(series_id, season_num)
        print("Parsing URL:", self.url)
        
        html = requests.get(self.url).text
        soup = BeautifulSoup(html)
        
        self.episodes_ids = []
        for link in soup.findAll('a'):
            if link.get('href'):
                if link.get('href').startswith("/title/tt") and link.get('href').endswith("/"):
                    self.episodes_ids.append(link.get('href').split("/")[-2])
        self.episodes_num = len(self.episodes_ids)
        

        