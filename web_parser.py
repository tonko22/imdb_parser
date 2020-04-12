from collections import OrderedDict
import requests
from bs4 import BeautifulSoup

urls = {
    "episodes": 'https://www.imdb.com/title/{0}/episodes?season={1}',
    "top_250": "https://www.imdb.com/chart/toptv?sort=ir,desc&mode=simple&page=1",
    "most_popular_series": 'https://www.imdb.com/chart/tvmeter?sort=ir,desc&mode=simple&page=1',
    "newest_series": 'https://www.imdb.com/chart/tvmeter?sort=us,desc'
}

def parse_episodes_ids(series_id: str, season_num: int):
    """ Extracts IMDB episode IDs """
    url = urls["episodes"].format(series_id, season_num)
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="lxml")
        
    episode_ids = []
    eplist = soup.findAll("div", {"itemprop": "episodes"})
    for link in eplist:
        for el in link.find_all("a"):
            tag = el.get('href')
            if tag.startswith("/title/tt") and tag.endswith("/"):
                episode_ids.append(tag.split("/")[-2])
    
    # Some episodes are unrated, count rating widgets
    rated_episodes_count = len(soup.findAll("div", {"class": "ipl-rating-widget"}))
    return episode_ids[:rated_episodes_count]

def parse_episodes_count(series_id: str, season_num: int):
    """ Parse website meta to get episode count for parse_episodes_ids method
    for later validation """
    url = urls["episodes"].format(series_id, season_num)
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="lxml")
    web_meta_episodes_count = int(soup.findAll("meta", {"itemprop": "numberofEpisodes"})[0].get("content"))
    return web_meta_episodes_count

def parse_top_250_series():
    """ Extracts top rated IMDB series IDs
    max: 250 
    """
    html = requests.get(urls["top_250"]).text
    soup = BeautifulSoup(html, features="lxml")
    
    series_ids = []
    series = soup.findAll("td", {"class": "titleColumn"})
    for s in series:
        for el in s.findAll("a"):
            series_ids.append(el.get("href").split("/")[-2])
    return series_ids

def parse_most_popular_series():
    """ Extracts most popular IMDB series IDs as determined by IMDb Users
    max: 100 
    """
    html = requests.get(urls["most_popular_series"]).text
    soup = BeautifulSoup(html, features="lxml")
    
    series_ids = []
    series = soup.findAll("td", {"class": "titleColumn"})
    for s in series:
        for el in s.findAll("a"):
            series_ids.append(el.get("href").split("/")[-2])
    return series_ids

def parse_newest_series():
    """ Extracts top IMDB series IDs
    max: 100
    """
    html = requests.get(urls["newest_series"]).text
    soup = BeautifulSoup(html, features="lxml")
    
    series_ids = []
    series = soup.findAll("td", {"class": "titleColumn"})
    for s in series:
        for el in s.findAll("a"):
            series_ids.append(el.get("href").split("/")[-2])
    return series_ids
