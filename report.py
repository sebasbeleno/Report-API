"""
    Este modulo es el central de todo Report.gg
    Aqué se hacen las llamadas a los demás mdulos
    y funciones.
"""
from console_logging.console import Console
from modules import summoner
from modules.champions import champions, win_rate, play_rate

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

def get_champions_win_rate(region: str):

    champions_win_rate = win_rate.get_champions_win_rate(region)

    return champions_win_rate

def get_champions_play_rate(region: str):

    champions_play_rate = play_rate.get_champions_play_rate(region)

    return champions_play_rate

def get_champions(region: str):

    champions_info = champions.get_champions(region)

    return champions_info

