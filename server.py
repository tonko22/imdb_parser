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
        
        episodes_ids = web_parser.parse_ids(web_parser.urls["episodes"].format(series_id, season_num))
        result = {
            "totalEpisodes": len(episodes_ids),
            "episodeIds": episodes_ids
            }
        return result
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}

@app.get("/series/top_rated/{n}")
def get_top_rated_series(n: int):
    """ Returns most popular series ids 
    in IMDB format (example: tt0096697) 
    sorted by Rating
    maximum entities: 200
    """
    try:
        top_series_ids = web_parser.parse_ids(web_parser.urls["most_popular_series"])
        result = {
            "top_series_ids": top_series_ids[:n],
            }
        return result
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}

@app.get("/series/newest/{n}")
def get_newest_series(n: int):
    """ Returns most popular series ids 
    in IMDB format (example: tt0096697) 
    sorted by Rating
    maximum entities: 200
    """
    try:
        newest_series_ids = web_parser.parse_ids(web_parser.urls["newest_series"])
        result = {
            "newest_series_ids": newest_series_ids[:n],
            }
        return result
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}
