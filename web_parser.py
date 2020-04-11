import requests
from bs4 import BeautifulSoup

def get_episode_ids_and_count(series_id: str, season_num: str):
    """ Returns number of episodes and episodes ID 
    in  season by series id and season num
    in IMDB format (example: tt0701194)
    """
    url = 'https://www.imdb.com/title/{0}/episodes?season={1}'.format(series_id, season_num)
    print("Parsing URL: ", url)
        
    html = requests.get(url).text
    soup = BeautifulSoup(html)
        
    episodes_ids = []
    for link in soup.findAll('a'):
        if link.get('href'):
            if link.get('href').startswith("/title/tt") and link.get('href').endswith("/"):
                episodes_ids.append(link.get('href').split("/")[-2])
    return len(episodes_ids), episodes_ids

def get_most_popular_series_ids():
    """ Returns most popular series ids 
    in IMDB format (example: tt0096697) 
    sorted by Rating
    maximum entities: 200
    """
    url = 'https://www.imdb.com/chart/tvmeter?sort=ir,desc&mode=simple&page=1'
    print("Parsing URL: ", url)
        
    html = requests.get(url).text
    soup = BeautifulSoup(html)
        
    top_series_ids = []
    for link in soup.findAll('a'):
        if link.get('href'):
            if link.get('href').startswith("/title/tt") and link.get('href').endswith("/"):
                top_series_ids.append(link.get('href').split("/")[-2])
    return top_series_ids

    