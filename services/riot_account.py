# services/riot_account.py

from config import REGION_ACCOUNT
from utils.http_client import get

def get_puuid(game_name, tag_line):
    url = f"{REGION_ACCOUNT}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    data = get(url)
    if data:
        print(data["puuid"])
        return data["puuid"]
    return None
