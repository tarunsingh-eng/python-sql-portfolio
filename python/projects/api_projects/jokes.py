import requests


url_api = 'https://official-joke-api.appspot.com/random_joke'

response = requests.get(url_api)

data = response.json()


# Do something with the json response to prove it works. 

print(data["setup"])
print(data["punchline"])