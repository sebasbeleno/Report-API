#Prtteir loggin
from console_logging.console import Console
console = Console()


from modules import summoner, league



def print_basic_summoner_info(name: str, region: str):

    summoner_info = summoner.get_basic_summoner_info(name, region)

    return summoner_info


if __name__ == "__main__":
     console.success(print_basic_summoner_info("JustBel", "LAN")) #PaARrDOo10
