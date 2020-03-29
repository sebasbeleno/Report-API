
#Imports
import cassiopeia as cass
import os
from cassiopeia import Summoner

api_key = os.environ["API_KEY"]

#Cassiopeia settings
cass.set_riot_api_key(api_key)
cass.set_default_region("LAN")



def print_basic_summoner_info(name: str, region: str):
    summoner = Summoner(name= name, region= region)
    print(summoner.profile_icon.url)

if __name__ == "__main__":
    print_basic_summoner_info("Justbel", "LAN")