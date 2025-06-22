# services/match_detail.py

from config import REGION_MATCH
from utils.http_client import get

def get_match_detail(match_id):
    url = f"{REGION_MATCH}/val/match/v1/matches/{match_id}"
    return get(url)
