"""
    Este modulo es el central de todo Report.gg
    Aqué se hacen las llamadas a los demás mdulos
    y funciones.
"""
from console_logging.console import Console
from modules import summoner

CONSOLE = Console()

def get_first_summoner_info(name: str, region: str):
    """
        Cuando es por primera vez, retorna la información
        básica de un invocador.
    """
    summoner_info = summoner.get_basic_summoner_info(name, region)

    return summoner_info

def update_summoner_info(name: str, region: str):
    """
        Actualiza la actualiza la informacion
        del invocador dato.
    """

    summoner_info_updated = summoner.get_updated_summoner_info(name, region)

    return summoner_info_updated