import requests
import json
respond = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=ae357682672146ca889a4f745f71bd1f")
print(respond.json());

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(respond.json())