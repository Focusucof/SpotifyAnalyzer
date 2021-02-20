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

#requests section
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
        
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])

print(artists)

def countFreq(arr):
    return collections.Counter(arr)

x = countFreq(artists)
pprint(x)

freqGreaterThanOne = {key:val for key, val in x.items() if val != 1}

labels = []
size = []

#splits labels and values into sperate arrays for the graph
for x, y in freqGreaterThanOne.items():
    labels.append(x)
    size.append(y)


#chart section
colors = ['#ff9999', '#ffcc99', '#85E3FF', '#B28DFF', '#F6A6FF', '#ffe079', '#00ffaa']

plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
plt.axis('equal')
legend = plt.legend(title = "artists", prop={'size': 15}, loc=(0.9, 0.5), labels=labels, frameon=False)
plt.setp(legend.get_title(), fontsize='xx-large')

fig = plt.gcf()
fig.set_size_inches(16, 10.8)

centre_circle = plt.Circle((0,0),0.30,fc='white')
fig.gca().add_artist(centre_circle)
plt.tight_layout()

fig.savefig('pie.png', dpi=100, transparent=False)

plt.show()