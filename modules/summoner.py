"""
    Este modulo obtinene la información basica de un
    invocador, haciendo una llamada a Cassiopiea.
"""
import os
import cassiopeia
from cassiopeia import Summoner
from db import mongo, find_summoner, if_summoner_exist, insert_summoner
from .league import get_summoner_league_entries
from . import match_list, add_last_update, time_between
API_KEY = os.environ["API_KEY"]
cassiopeia.apply_settings({
    "logging": {
        "print_calls": False,
    }
})
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
    else:
        summoner = call_api_summoner(name, region)

        json_summoner = {
            "name": str(summoner.name),
            "level": str(summoner.level),
            "iconUrl": str(summoner.profile_icon.url),
            "accountId": str(summoner.account_id),
            "uid": str(summoner.id),
        }

        json_summoner = call_api_summoner_entries(json_summoner, summoner)
        json_summoner = call_api_match_list(json_summoner, summoner)
        json_summoner = add_last_update.update_last_update(json_summoner)
        insert_summoner.insert_summoner(json_summoner)

        return json_summoner

def get_updated_summoner_info(name, region):

    """
        Esta función actualiza los datos de un invocador
    """

    result = find_summoner.find_summuner(name)

    last_update = result['last_update']

    if time_between.time_between(last_update):
        summoner = call_api_summoner(name, region)

        json_summoner = {
            "name": str(summoner.name),
            "level": str(summoner.level),
            "iconUrl": str(summoner.profile_icon.url),
            "accountId": str(summoner.account_id),
            "uid": str(summoner.id),
        }

        json_summoner = call_api_summoner_entries(json_summoner, summoner)
        json_summoner = call_api_match_list(json_summoner, summoner)
        json_summoner = add_last_update.update_last_update(json_summoner)
        insert_summoner.update_summoner(json_summoner)

        return json_summoner
    else:
        return "Error"

def call_api_match_list(json_summoner, summoner):
    """
        Esta funcion llama returna la la lista
        detallada de las últimas partidas del invocador
    """
    json_summoner = match_list.get_match_list(summoner, json_summoner)

    return json_summoner

def call_api_summoner_entries(json_summoner, summoner):
    """
        "Esta funcion retorna las entradas de liga
        del invocador dado.
    """
    json_summoner = get_summoner_league_entries(summoner, json_summoner)

    json_summoner['name'] = json_summoner['name'].lower()

    return json_summoner

def call_api_summoner(name, region):
    """
        Esta función retorna la información básica
        de un invocador. Se neceita el nombre de invocador
        y la región a la que pertenece.
    """
    summoner = Summoner(name=name, region=region)

    return summoner
