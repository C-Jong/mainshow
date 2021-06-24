import requests
import json

url = 'https://www.runoob.com/python/python-json.html'

response = requests.get(url)

print(type(response.text))

# print(response.text)

