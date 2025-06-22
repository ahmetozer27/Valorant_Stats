# utils/http_client.py

import requests
from config import HEADERS


def get(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"[HTTP ERROR] {err}")
    except Exception as e:
        print(f"[ERROR] {e}")
    return None
