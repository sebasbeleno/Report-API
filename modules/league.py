import cassiopeia as cass

from cassiopeia import Queue, Position
#Cassiopeia
import cassiopeia as cass
from cassiopeia import Summoner, LeagueSummonerEntries, Queue

def get_summoner_league_entries(summoner: Summoner, json_summoner: dict):

    league_entries = cass.get_league_entries(summoner=summoner)


    if Queue.ranked_solo_fives in league_entries:
        json_summoner['ranked_solo_fives'] = {
            "tier": str(league_entries[Queue.ranked_solo_fives].tier),
            "division": str(league_entries[Queue.ranked_solo_fives].division),
            "league_points": league_entries[Queue.ranked_solo_fives].league_points
        }
    else:
        json_summoner['ranked_solo_fives'] = {
            "tier": "unranked",
            "division": 0,
            "league_points": 0
        }

    if Queue.ranked_flex_fives in league_entries:
        json_summoner['ranked_flex_fives'] = {
            "tier": str(league_entries[Queue.ranked_flex_fives].tier),
            "division": str(league_entries[Queue.ranked_flex_fives].division),
            "league_points": league_entries[Queue.ranked_flex_fives].league_points
        }
    else:
        json_summoner['ranked_flex_fives'] = {
            "tier": "unranked",
            "division": 0,
            "league_points": 0
        }


    return json_summoner