from collections import OrderedDict
import requests
from bs4 import BeautifulSoup

urls = {
    "episodes": 'https://www.imdb.com/title/{0}/episodes?season={1}',
    "most_popular_series": 'https://www.imdb.com/chart/tvmeter?sort=ir,desc&mode=simple&page=1',
    "newest_series": 'https://www.imdb.com/chart/tvmeter?sort=us,desc'
}

def parse_ids(url: str):
    """ Extracts IMDB series/episodes IDs from web page """
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="lxml")
        
    series_ids = []
    for link in soup.findAll('a'):
        if link.get('href'):
            if link.get('href').startswith("/title/tt") and link.get('href').endswith("/"):
                series_ids.append(link.get('href').split("/")[-2])
    return list(OrderedDict.fromkeys(series_ids)) # drop duplicates while preserving 