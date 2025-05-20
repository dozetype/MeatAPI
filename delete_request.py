#using this as a replacement for cURL
import requests

index = 8
url = f"http://localhost:5000/meat/{index}"
r = requests.delete(url)