import requests

url = 'https://vk.com/ru/method/photos.get'
params = {
    'user_ids' : '110168',
    'fields' : 'bdate',
    'access_token' : '...',
    'v' : '5.199 HTTP/1.1'
}

response = requests.get(url, params=params)
print(response.status_code)