import requests

url = "https://api.jikan.moe/v4/anime"
url2 = ""

response = requests.get(url=url)
data = response.json()

print(data)