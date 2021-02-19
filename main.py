import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from dotenv import load_dotenv
import os
import json
import collections
from matplotlib import pyplot as plt
import matplotlib

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

artists = []

while True:
    response = sp.playlist_items(
        pl_id,
        offset=offset,
        fields='items.track.artists.name,total',
        additional_types=['track']
    )
    
    if len(response['items']) == 0:
        break

    
    for count in range(len(response['items'])):
        print(response['items'][count]['track']['artists'][0]['name'])
        artists.append(response['items'][count]['track']['artists'][0]['name'])
    
    
    #for i in range(len(response['items'])):
    #    print(response['items'][0]['track']['artists'][0]['name'])
        
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])

print(artists)

def countFreq(arr):
    return collections.Counter(arr)

x = countFreq(artists)
pprint(x)

labels = []
size = []


for x, y in x.items():
    labels.append(x)
    size.append(y)

plt.pie(size, labels=size, colors=None)
plt.axis('equal')
plt.legend(title = "artists", prop={'size': 15}, loc=(0.9, -0.1), labels=labels, frameon=False)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16, 10.8)
fig.savefig('pie.png', dpi=100, transparent=False)

plt.show()

