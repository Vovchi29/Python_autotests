import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7bc2abaff81b4091ef3523bc7e0f287b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '10033'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Твердыня'

    '{"status":"success","data":[{"id":"10033","trainer_name":"Твердыня","level":"1","pokemons":["116259","116265","116258","116264","116260","116269","116400"],"pokemons_alive":["116269","116400"],"pokemons_in_pokeballs":[],"get_history_battle":"0","is_premium":false,"premium_duration":0,"avatar_id":2,"city":"Самара"}]}'