#using this as a replacement for cURL
import requests

url = "http://localhost:5000/meat"
new_data = {
    "name": "mutton",
    "description": "mehhhh"
}

r = requests.post(url, json=new_data)