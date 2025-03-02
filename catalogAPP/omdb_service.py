import requests
from django.conf import settings

#criei estar pasta com minha api pq a outra estar com muito codigo (views)

def procurafilme(title):
    url = f"http://www.omdbapi.com/?apikey=f279f0ed&t={title}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None
