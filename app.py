from flask import Flask
from markupsafe import escape
from flask import jsonify
from flask_cors import CORS, cross_origin

from report import print_basic_summoner_info

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, support_credentials=True)

@cross_origin(supports_credentials=True)



@app.route('/')
def hello_world():
    return "Hi! This is a internal server. Please if you dont know what is this, please close this window. Thanks"

@app.route('/summoner/<region>/<summonerName>')
def fetch_summoner_info(region, summonerName):

    summonerName = escape(summonerName)
    region = escape(region)
    region = region.upper()

    summoner_info = print_basic_summoner_info(summonerName, region)

    #TODO: Terminar de jugar con los datos xd

    return summoner_info

