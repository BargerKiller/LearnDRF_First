import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,
                             json={'title': "Some", "price": 234})

# print(get_response.text)
print(get_response.json())
