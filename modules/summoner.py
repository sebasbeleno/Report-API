import os

#Env
api_key = os.environ["API_KEY"]
region = "LAN"

#Cassiopeia
import cassiopeia as cass
from cassiopeia import Summoner, LeagueSummonerEntries, Queue

#Cassiopeia settings
cass.set_riot_api_key(api_key)

from .league import get_summoner_league_entries


def get_basic_summoner_info(name: str, region: str):
    summoner = Summoner(name= name, region= region)


    json_summoner = {
        "name": summoner.name,
        "level": summoner.level,
        "iconUrl": summoner.profile_icon.url,
        "accountId": summoner.account_id,
        "uid": summoner.id,
    }

    json_summoner = get_summoner_league_entries(summoner,json_summoner)


    return json_summoner
