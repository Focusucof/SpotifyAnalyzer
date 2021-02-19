import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from dotenv import load_dotenv
import os
import json
import collections

load_dotenv()
CLIENTID = os.getenv('CLIENTID')
CLIENTSECRET = os.getenv('CLIENTSECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENTID,
    client_secret=CLIENTSECRET
    )
)

pl_id = 'spotify:playlist:7pEHQIFPFnELcHSIYSyzsP'
offset = 0



while True:
    response = sp.playlist_items(
        pl_id,
        offset=offset,
        fields='items.track.artists.name,total',
        additional_types=['track']
    )
    
    if len(response['items']) == 0:
        break

    artists = []
    
    for count in range(len(response['items'])):
        print(response['items'][count]['track']['artists'][0]['name'])
        artists.append(response['items'][count]['track']['artists'][0]['name'])
    
    print(artists)
    
    
    #for i in range(len(response['items'])):
    #    print(response['items'][0]['track']['artists'][0]['name'])
        
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])


def countFreq(arr):
    return collections.Counter(arr)

x = countFreq(artists)
print(x)






