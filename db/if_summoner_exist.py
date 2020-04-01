"""
    Este modulo verifica si un invocador ya
    eviste en la base de datos.
"""
from .mongo import get_summoner_collection

SUMMONER_COLLECTION = get_summoner_collection()

def if_summoner_exist(summoner_namme):
    """
        Esta función verifica en la base de datos
        si un invocador ya existe.
        Retorta True si existe, False si no.
    """
    if SUMMONER_COLLECTION.count_documents({'name': summoner_namme}, limit=1):
        print("Ya existe un invocador con ese nombre :D")
        return True

    print("No existe un invocador con ese nombre :D")
    return False
