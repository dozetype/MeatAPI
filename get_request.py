#not used for the project
import requests
import json

def get_data():
    url = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
    response = requests.get(url)

    if response.status_code == 200:
        for post in response.json()['items']:
            data = post['title']
            pretty_data = json.dumps(data, indent=4)
            print(pretty_data)
            print()

get_data()
