import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7bc2abaff81b4091ef3523bc7e0f287b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
        "name": "generate",
        "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
print(response_create.status_code) 

message = response_create.json()['message']
print(message)

name_change = {
    "pokemon_id": "116400",
    "name": "Плюшевый",
    "photo_id": 5
}

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = name_change)
print(response_create.text)
print(response_create.status_code)

message = response_create.json()['message']
print(message)


cath = {
    "pokemon_id": "116623"
}

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = cath)
print(response_create.text)
print(response_create.status_code)

message = response_create.json()['message']
print(message)