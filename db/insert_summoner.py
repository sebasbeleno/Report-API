"""
    Este modulo inserta en la base de datos el
    registro de un invocador
"""
from .mongo import get_summoner_collection

SUMMONER_COLLECTION = get_summoner_collection()

def insert_summoner(summoner):
    """
        Esta función inserta en la base de datos
        el invocador que sea dado por parametro.
    """
    return SUMMONER_COLLECTION.insert_one(summoner)

def update_summoner(summoner: dict):
    """
        Esta funnción actualiza un invocador
        que sea dado por parametro.
    """

    summoner_name = summoner.get('name')

    query = {"name": summoner_name}

    return SUMMONER_COLLECTION.update_one(query, {"$set": summoner})