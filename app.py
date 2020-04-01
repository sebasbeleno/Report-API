"""
    Server core and API handdle
"""
from flask import Flask
from flask_cors import CORS, cross_origin
from markupsafe import escape
from report import print_basic_summoner_info

APP = Flask(__name__)
APP.debug = True
APP.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
APP.config['CORS_HEADERS'] = 'Content-Type'

CORS(APP, support_credentials=True)
@cross_origin(supports_credentials=True)

@APP.route('/')
def hello_world():
    """
        Mensaje al entrar en la ruta /
    """
    return "Report.gg"

@APP.route('/summoner/<region>/<summoner_name>')
def fetch_summoner_info(region, summoner_name):
    """
        Hacer fetch de la información básica
        de un invocador
    """
    summoner_name = escape(summoner_name)
    region = escape(region)
    region = region.upper()

    summoner_info = print_basic_summoner_info(summoner_name, region)

    #Pop _id from DB
    summoner_info.pop('_id')

    return summoner_info


if __name__ == "__main__":
    APP.run(debug=True)
