import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from pprint import pprint
import collections

class Stats:
    def __init__(self, CLIENTID, CLIENTSECRET):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                CLIENTID,
                CLIENTSECRET
            )
        )

    def artist_stats(self, pl_id):
        artists = []
        offset = 0

        while True:
            response = self.sp.playlist_items(
                playlist_id=pl_id,
                offset=offset,
                fields="items.track.artists.name,total",
                additional_types=["track"]
            )

            # print(len())

            if len(response['items']) == 0:
                break

            for i in range(len(response['items'])):
                for j in range(len(response['items'][i]['track']['artists'])):
                    artists.append(response['items'][i]['track']['artists'][j]['name'])
                    pprint(response['items'][i]['track']['artists'][j]['name'])



            offset += len(response['items'])
            print(offset, "/", response['total'])

            x = collections.Counter(artists)
            freqGreaterThanOne = {key:val for key, val in x.items() if val != 1 and key != ''}

        return freqGreaterThanOne

