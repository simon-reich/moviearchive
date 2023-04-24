import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.post(BASE + 'imdbapi/search', {"title": "Prey 2022", "year": 2022})
response = requests.get(BASE + 'imdbapi/tt11866324')

print(response.json())