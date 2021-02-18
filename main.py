import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from dotenv import load_dotenv
import os
import json
from collections import Counter

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

    pprint(response)
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])
