"""
    API handdler that gives
    all endpoints from Cassiopeia
"""
from console_logging.console import Console
from modules import summoner

CONSOLE = Console()

def print_basic_summoner_info(name: str, region: str):
    """
        Print summoner basic info.
    """
    summoner_info = summoner.get_basic_summoner_info(name, region)

    return summoner_info
