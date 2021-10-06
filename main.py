#external dependencies
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from matplotlib import pyplot as plt
from flask import Flask, render_template, request, Response

#built-in dependencies
import os
import json
import collections
import shutil
from pprint import pprint

#load client credentials from .env file
load_dotenv()

#constants
app = Flask(__name__)
CLIENTID = os.getenv('CLIENTID')
CLIENTSECRET = os.getenv('CLIENTSECRET')

#create a new spotify object and authenticate with the WebAPI
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=CLIENTID,
        client_secret=CLIENTSECRET
    )
)

def getChart(pl_id, offset = 0):    # request and chart section

    # I don't think I will ever understand this fully but...
    # response can only hold 100 tracks, so if the tracks gotten is less than the 
    # total expected, another request is made until the reponse is equal to 0.
    # 
    # The main artist from each track is added to the artists array, then sorted by frequency
    # and added to freqGreaterThanOne if the artist appears more than 1 time

    # TODO: 
    #   - count artist features and collabs
    #   - add more colours for the pie chart
    #   - order pie chart from greatest to least
    #   - order legend
    #   - rework css and create a theme for the app

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
            
        offset = offset + len(response['items'])
        print(offset, "/", response['total'])

    #print(artists)


    x = countFreq(artists)
    #pprint(x)

    freqGreaterThanOne = {key:val for key, val in x.items() if val != 1}

    labels = []
    size = []

    #splits labels and values into sperate arrays for the graph
    for x, y in freqGreaterThanOne.items():
        labels.append(x)
        size.append(y)


    #chart section
    colors = ['#ff9999', '#ffcc99', '#85E3FF', '#B28DFF', '#F6A6FF', '#00ffaa', '#ffe079', '#efff9e', '#ff99bd']

    plt.pie(size, labels=None, colors=colors, startangle=90) #removed autopct='%1.1f%%' and pctdistance=0.85
    plt.axis('equal')
    legend = plt.legend(title = "Artists", prop={'size': 15}, loc=(0.9, 0.5), labels=labels, frameon=False)
    plt.setp(legend.get_title(), fontsize='xx-large')

    fig = plt.gcf()
    fig.set_size_inches(16, 10.8)

    centre_circle = plt.Circle((0,0),0.30,fc='white')
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()

    fig.savefig('pie.png', transparent=False)
    shutil.move('./pie.png', './static/pie.png')

def countFreq(arr):
    return collections.Counter(arr)