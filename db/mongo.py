"""
    Este modulo establece una conección
    con la base de datos en MongoDB
"""
import pymongo

MY_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")

REPORT_DB = MY_CLIENT["report"]

SUMMONER_COLLECTION = REPORT_DB.summoners

def get_summoner_collection():
    """
        Esta función retorna la coleción de "Summoner"
    """
    return SUMMONER_COLLECTION

def insert_summoner(summoner):
    """
        Esta función inserta en la base de datos
        el invocador que sea dado por parametro.
    """
    SUMMONER_COLLECTION.insert_one(summoner)
    return True
