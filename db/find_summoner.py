"""
    Este modulo busca en la base de datos
    el invocador que se le pida
"""
from .mongo import get_summoner_collection

SUMMONER_COLLECTION = get_summoner_collection()

def find_summuner(summoner_name):
    """
        Esta función bsca en la base de datos
        el invocador que sea enviado por parametro.
    """

    summoner_name = summoner_name.lower()

    return SUMMONER_COLLECTION.find_one({'name': summoner_name})
