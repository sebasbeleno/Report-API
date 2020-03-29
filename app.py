from flask import Flask
from markupsafe import escape
from flask import jsonify

app = Flask(__name__)

from summoner import print_basic_summoner_info

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

    return {
        "summonerName": summoner_info.name,
        "iconUrl": summoner_info.profile_icon.url,
        "uid": summoner_info.account_id,
        "level": summoner_info.level,
        "rank": summoner_info.ranks
    }

