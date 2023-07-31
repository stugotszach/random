import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


cid = 'cid'

secret = 'secret'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#playlist id
pl_id = 'spotify:playlist:2boJbb5FgGj7GqKwkT37oj'

results = sp.playlist(pl_id)

print('')

for item in results['tracks']['items'][:10]:
    print(
    	item['track']['artists'][0]['name'] + " -",
        item['track']['name'] + " -",
        item['track']['album']['name']
    )
print('')