import requests
from config import BASE_URL

def fetch_data(endpoint,limit,skip):
    urls=f"{BASE_URL}/{endpoint}?limit={limit}&skip={skip}"
    response=requests.get(url=urls,timeout=30)
    response.raise_for_status()
    return response.json()


def get_total(endpoint):
    response=fetch_data(endpoint,limit=1,skip=0)
    
    return response["total"]
