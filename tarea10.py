import requests

url="https://pokeapi.co/api/v2/pokemon?limit=151"
response=requests.get(url)
list=response.json()["results"]
for pokemon in list:
    print(pokemon["name"])