
#Imports
import cassiopeia as cass
import os
from cassiopeia import Summoner, LeagueSummonerEntries, Queue
#Prtteir loggin
from console_logging.console import Console
console = Console()

api_key = os.environ["API_KEY"]

#Cassiopeia settings
cass.set_riot_api_key(api_key)
cass.set_default_region("LAN")



def print_basic_summoner_info(name: str, region: str):
    summoner = Summoner(name= name, region= region)



    #TODO: Terminar de retornar la liga.
    for key, val in summoner.ranks.items():
        print(key, '=>', val)
        console.info("Tipo de valores")
        print(type(key), '=>', type(val))

    print(summoner.ranks[Queue.ranked_solo_fives])

    return summoner


if __name__ == "__main__":
    console.success(print_basic_summoner_info("JustBel", "LAN"))
