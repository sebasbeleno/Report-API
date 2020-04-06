"""
    Este modulo añade la ultima actualización de datos
    que se le realizó a un invocador.
"""
from datetime import datetime

def update_last_update(json_summoner):
    """
        Esta función añade del summoner dado,
        la fecha y hora actual.
    """
    now = datetime.now()

    now_string = now.strftime("%d/%m/%Y %H:%M:%S")

    json_summoner['last_update'] = now_string

    return json_summoner
