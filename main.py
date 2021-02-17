import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="",
                                                           client_secret=""))

pl_id = 'spotify:playlist:7pEHQIFPFnELcHSIYSyzsP'
offset = 0

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.artists.name,total',
                                 additional_types=['track'])
    
    if len(response['items']) == 0:
        break
    
    pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])
