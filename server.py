import sys
import traceback
from fastapi import FastAPI

import web_parser

app = FastAPI()

@app.get("/series/{series_id}/episodes/")
def get_episodes(series_id: str, season_num: str = 1):
    """ Returns number of episodes and episodes ID 
    in  season by series id and season num
    in IMDB format (example: tt0701194)
    """
    try:
        episodes_num, episodes_ids = web_parser.get_episode_ids_and_count(series_id, season_num)
        result = {
            "totalEpisodes": episodes_num,
            "episodeIds": episodes_ids
            }
        return result
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}

@app.get("/get_top_{top_n}_series")
def get_top_series(top_n: int):
    """ Returns most popular series ids 
    in IMDB format (example: tt0096697) 
    sorted by Rating
    """
    try:
        top_series_ids = web_parser.get_most_popular_series_ids()
        result = {
            "top_series_ids": top_series_ids[:top_n],
            }
        return result
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}