from flask import Flask, request
from Stats import *

sp = Stats()
app = Flask(__name__)

@app.route('/<pl_id>/artists')
def countArtists(pl_id):
    return sp.artist_stats(pl_id)
