import sys
import traceback
from fastapi import FastAPI

import web_parser

app = FastAPI()

@app.get("/series/{series_id}/episodes")
def get_episodes(series_id: str, season_num: int = 1):
    """ Returns number of episodes and episodes ID 
    in  season by series id and season num
    in IMDB format (example: tt0701194)
    """
    try:
        episode_ids = web_parser.parse_episodes_ids(series_id, season_num)
        parsed_episodes_count = len(episode_ids)
        web_meta_episodes_count = web_parser.parse_episodes_count(series_id, season_num) # web-meta based count
        result = {
            "parsed_episodes_count": parsed_episodes_count,
            "episode_ids": episode_ids
            }
        if parsed_episodes_count == web_meta_episodes_count:
            return result
        else:
            return {"exception_type": "totalEpisodes not equals web_meta_episodes_count"}
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}

@app.get("/top_250")
def get_top_250():
    """ Returns top 250 series ids rated by users
    in IMDB format (example: tt0701194)
    """
    try:
        top_250_series_ids = web_parser.parse_top_250_series()
        result = {
            "top_250_series_ids": top_250_series_ids
            }
        return result
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}
    
@app.get("/series/most_popular/{n}")
def get_most_popular_series(n: int):
    """ Returns most popular series ids 
    in IMDB format (example: tt0096697) 
    sorted by Rating
    maximum entities: 200
    """
    try:
        most_popular_series_ids = web_parser.parse_most_popular_series()
        result = {
            "most_popular_series_ids": most_popular_series_ids[:n],
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
        newest_series_ids = web_parser.parse_newest_series()
        result = {
            "newest_series_ids": newest_series_ids[:n],
            }
        return result
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}
