import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title': 'Change title',
    'price': 124323,
}
get_response = requests.put(endpoint, json=data)
# print(get_response.text)
print(get_response.json())
