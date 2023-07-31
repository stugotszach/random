import requests
import json
from time import sleep


r = requests.get("https://official-joke-api.appspot.com/random_joke")
j = json.loads(r.content)
print(j['setup'])
sleep(1)
print(j['punchline'])
