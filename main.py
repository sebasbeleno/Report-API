"""
    Server core and API handdle
"""
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from markupsafe import escape
from report import get_first_summoner_info, update_summoner_info
import report as report

def create_app():
        
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app

app = create_app()
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route('/')
def hello_world():
    """
        Mensaje al entrar en la ruta /
    """
    return "Report.gg"

@app.route('/summoner')
def fetch_summoner_info():
    """
        Hacer fetch de la información básica
        de un invocador
    """
    summoner_name  = request.args.get('summoner_name') 
    region = request.args.get('region')
    region = region.upper()

    summoner_info = get_first_summoner_info(summoner_name, region)

    #Pop _id from DB
    summoner_info.pop('_id')

    return jsonify(summoner_info)

@app.route('/updateSummoner')
def update_summoner():
    """
        Esta ruta actualiza el invcador dado.
    """

    summoner_name  = request.args.get('summoner_name') 
    region = request.args.get('region')
    region = region.upper()

    updated_summoner_info = update_summoner_info(summoner_name, region)

    if update_summoner_info != "Error":

        return jsonify(updated_summoner_info)
    else:
        updated_summoner_info.pop('_id')
        return jsonify(update_summoner_info)

@app.route('/championswinrate')
def champions_winrate():
    """
        Esta ruta devuelve el winrate de todos los campones de una región dada.
    """

    region = request.args.get('region')
    region = region.upper()

    champions_winrates = report.get_champions_win_rate(region)

    print(champions_winrates)

    return jsonify(champions_winrates)


@app.route('/championsplayrate')
def champions_playrate():
    """
        Esta ruta devuelve el playrate de todos los campones de una región dada.
    """

    region = request.args.get('region')
    region = region.upper()

    champions_playrates = report.get_champions_play_rate(region)

    return jsonify(champions_playrates)

@app.route('/champions')
def champions():
    """
        Esta ruta devuelve la imágen y nombre de un campeón dado.
    """

    region = request.args.get('region')
    region = region.upper()

    champions_info = report.get_champions(region)

    return jsonify(champions_info)