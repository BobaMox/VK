import requests
from pprint import pprint


url = 'https://api.vk.com/method/photos.get?'
params = {
    'owner_id' : '324267239',
    'album_id' : 'profile',
    'access_token' : access_token,
    'v' : '5.199'
}

response = requests.get(url, params=params)
pprint(response.json())
