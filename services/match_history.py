# services/match_history.py

from config import REGION_MATCH
from utils.http_client import get


def get_match_list(puuid):
    url = f"{REGION_MATCH}/val/match/v1/matchlists/by-puuid/{puuid}"
    data = get(url)
    if data and "history" in data:
        return data["history"]
    return []
