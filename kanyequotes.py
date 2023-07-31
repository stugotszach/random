import requests
import json

r = requests.get("https://api.kanye.rest")
j = json.loads(r.content)
print(j['quote'])