"""
    Server core and API handdle
"""
from flask import Flask
from flask_cors import CORS, cross_origin
from markupsafe import escape
from report import get_first_summoner_info, update_summoner_info

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

    summoner_info = get_first_summoner_info(summoner_name, region)

    #Pop _id from DB
    print(summoner_info)
    summoner_info.pop('_id')

    return summoner_info

@APP.route('/updateSummoner/<region>/<summoner_name>')
def update_summoner(region, summoner_name):
    """
        Esta ruta actualiza el invcador dado.
    """

    summoner_name = escape(summoner_name)
    region = escape(region)
    region = region.upper()

    updated_summoner_info = update_summoner_info(summoner_name, region)

    if update_summoner_info != "Error":

        return updated_summoner_info
    else:
        updated_summoner_info.pop('_id')
        return update_summoner_info

if __name__ == "__main__":
    APP.run()
