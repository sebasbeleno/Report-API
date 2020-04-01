"""
    Este modulo establece una conección
    con la base de datos en MongoDB
"""
import os
import pymongo
SERVER_KEY = os.environ['SERVER_KEY']
DATA_URI = "mongodb+srv://admin:{server_key}@reportgg-4mkhr.gcp.mongodb.net/test?retryWrites=true&w=majority".format(server_key=SERVER_KEY)
MY_CLIENT = pymongo.MongoClient(DATA_URI)

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
