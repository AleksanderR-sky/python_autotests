import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '46b8443032dd3923c5ca951ccf6c3109'
HEADER = {'Content_Type' :'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '22458'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Aleks'