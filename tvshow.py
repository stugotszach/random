import requests
import json


show = input("Enter the name of the show: ")
r = requests.get(f"http://api.tvmaze.com/singlesearch/shows?q=:{show}")
j = json.loads(r.content)
try:
    print("Official Site: "+j['officialSite'])
except:
    pass
try:
    print("Image: "+j['image']['medium'])
except:
    pass
try:
    print("Network: "+j['network']['name'])
except:
    pass
try:
    print("Summary: "+j['summary'])
except:
    pass


    



