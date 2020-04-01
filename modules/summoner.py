"""
    Este modulo obtinene la información basica de un
    invocador, haciendo una llamada a Cassiopiea.
"""
import os
import cassiopeia
from cassiopeia import Summoner
from db import mongo, find_summoner, if_summoner_exist
from .league import get_summoner_league_entries

API_KEY = os.environ["API_KEY"]
cassiopeia.set_riot_api_key(API_KEY)

def get_basic_summoner_info(name: str, region: str):
    """
        Esta función hace una llamada a casiopiea
        para obtener los datos básicos de un summoner.
        A su vez, hace una llamada al modulo "League",
        para obtener las entradas de dicho summoner.
    """
    if if_summoner_exist.if_summoner_exist(name):
        result = find_summoner.find_summuner(name)
        return result

    summoner = Summoner(name=name, region=region)

    json_summoner = {
        "name": str(summoner.name),
        "level": str(summoner.level),
        "iconUrl": str(summoner.profile_icon.url),
        "accountId": str(summoner.account_id),
        "uid": str(summoner.id),
    }

    json_summoner = get_summoner_league_entries(summoner, json_summoner)
    mongo.insert_summoner(json_summoner)

    return json_summoner
