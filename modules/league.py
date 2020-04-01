"""
    Obtiene las entrafas de liga de un invodador
    Además, las añade al JSON
    TODO: Agregar un metodo que se encargue de añadir al JSON,
        Para segregar dependencias.
"""
import cassiopeia as cass
from cassiopeia import Summoner, Queue

def get_summoner_league_entries(summoner: Summoner, json_summoner: dict):
    """
        Esta función hace una llamada a Cassiopeia,
        pidiendo las entradas de un invocador
    """
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
