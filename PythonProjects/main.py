import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '46b8443032dd3923c5ca951ccf6c3109'
HEADER = {'Content_Type' :'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_new_name = {
    "pokemon_id": "270948",
    "name": "sasha",
    "photo_id": 1
}

body_pokeball = {
    "pokemon_id": "270948"
}

#Создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER , json = body_create)
print(response_create.text)
#Смена имени покемона
response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER , json = body_new_name)
print(response_new_name.text)
#Поймать покемона в покебол
response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER , json = body_pokeball)
print(response_pokeball.text)