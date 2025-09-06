import requests

url = "http://localhost:8000/admin/add"
data = {
    "username": "undergr0undp",
    "password": "jarvis2023"
}

response = requests.post(url, json=data)
print(response.json())