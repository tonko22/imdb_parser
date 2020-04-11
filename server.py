import sys
import traceback
from fastapi import FastAPI
from web_parser import IMDBSeriesIDParser

app = FastAPI()

@app.get("/series/{series_id}/episodes/")
def read_series(series_id: str, season_num: str = 1):
    try:
        parser = IMDBSeriesIDParser(series_id, season_num)
        result = {
            "totalEpisodes": parser.episodes_num,
            "episodeIds": parser.episodes_ids
            }
        return result
    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        return {"exception_type": str(exc_type), "exception_value": str(exc_value)}
