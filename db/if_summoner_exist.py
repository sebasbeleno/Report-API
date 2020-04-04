"""
    Este modulo verifica si un invocador ya
    eviste en la base de datos.
"""
from .mongo import get_summoner_collection

SUMMONER_COLLECTION = get_summoner_collection()

def if_summoner_exist(summoner_name):
    """
        Esta función verifica en la base de datos
        si un invocador ya existe.
        Retorta True si existe, False si no.
    """

    summoner_name = summoner_name.lower()

    if SUMMONER_COLLECTION.count_documents({'name': summoner_name}, limit = 1) != 0:
        print("Ya existe un invocador con ese nombre :D")
        return True
    else:
        print("No existe un invocador con ese nombre :D")
        return False
