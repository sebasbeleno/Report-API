"""
    Este moculo se encarga de
    obtejer la list de paridas de un
    invocador.
"""
import cassiopeia as cass
from itertools import islice
from cassiopeia import Summoner
from cassiopeia.data import Season
from collections import Counter
import json

matchs_number = 10

def get_match_list(summoner: Summoner, json_summoner: dict):
    """
        Obtiene información detallada del numero de
        partidas dados por paramatro de un invidaro en
        especifico, También dado por paramatro.
    """

    match_history = summoner.match_history
    match_history(seasons={Season.season_9})

    match_count = 0
    id_list_of_matchs = []

    while match_count <= 10:
        match = match_history[match_count]
        id_list_of_matchs.append(match)
        match_count += 1

    win_ratio = 0

    list_of_match = []
    for match in islice(id_list_of_matchs, matchs_number):

        summoner_participant = match.participants[summoner]
        match1 = {}

        if summoner_participant.team.win == True:
            win_ratio += 1
        elif summoner_participant.team.win == False:
            win_ratio += 0

        
    
        match1 = {
            "campeon": {
                "nombre": str(summoner_participant.champion.name),
                "image":  str(summoner_participant.champion.image.url),
                "habilidades": {
                    "habilidad_f": {
                        "nombre": str(summoner_participant.summoner_spell_f.name),
                        "imagen": str(summoner_participant.summoner_spell_f.image.url),
                    },
                    "habilidad_d": {
                        "nombre": str(summoner_participant.summoner_spell_d.name),
                        "imagen": str(summoner_participant.summoner_spell_d.image.url),
                    }
                }
            },
            "duracion": str(match.duration),
            "win": str(summoner_participant.team.win),
            "linea": str(summoner_participant.lane),
            "rol": str(summoner_participant.role),
            "kda": str(summoner_participant.stats.kda),
            "asesinatos": str(summoner_participant.stats.kills),
            "muertes": str(summoner_participant.stats.deaths),
            "asistencias": str(summoner_participant.stats.assists),
            "nivel": str(summoner_participant.stats.level),
            "cs": str(summoner_participant.stats.total_minions_killed),
            "puntaje de vision: ": str(summoner_participant.stats.vision_score),
        }

        items = []
        for item in summoner_participant.stats.items:
            if item is not None:
                item_selected = {
                    "name": str(item.name),
                    "image": str(item.image.url)
                }
                items.append(item_selected)
            else:
                item_selected = {
                    "name": "None",
                    "image": "None"
                }
                items.append(item_selected)


        match1['items'] = items

        runes = summoner_participant.runes
        summoner_runes_from_cassio = []

        for rune in runes:
            summoner_runes_from_cassio.append(rune.name)
            summoner_runes_from_cassio.append(rune.image.url)
        
        summoner_runes = []


        for i in range(0, int(len(summoner_runes_from_cassio)), 2):
            rune_selected = {
                "nombre": str(summoner_runes_from_cassio[i]),
                "imagen": str(summoner_runes_from_cassio[i+1])
            }
            summoner_runes.append(rune_selected)


        match1['runas_principales'] = summoner_runes


        equipo_rojo_desde_cassio = match.red_team.participants

        equipo_rojo = []

        for participante_equipo_rojo in equipo_rojo_desde_cassio:
            participante = {
                "invocador": str(participante_equipo_rojo.summoner.name),
                "campeon": str(participante_equipo_rojo.champion.name),
                "icono_campeon": str(participante_equipo_rojo.champion.image.url)
            }

            equipo_rojo.append(participante)

        equipo_azul_desde_cassio = match.blue_team.participants
        equipo_azul = []

        for participante_equipo_azul in equipo_azul_desde_cassio:
            participante = {
                "invocador": str(participante_equipo_azul.summoner.name),
                "campeon": str(participante_equipo_azul.champion.name),
                "icono_campeon": str(participante_equipo_azul.champion.image.url)
            }

            equipo_azul.append(participante)

        match1['equipo_rojo'] = equipo_rojo
        match1['equipo_azul'] = equipo_azul

        list_of_match.append(match1)

    json_summoner['matchs'] = list_of_match

    region = "LAN"

    champion_id_to_name_mapping = {champion.id: champion.name for champion in cass.get_champions(region=region)}
    champion_id_to_icon_mapping = {champion.id: champion.image.url for champion in cass.get_champions(region=region)}
    

    played_champions_name = Counter()

    for match in match_history:
        champion_id = match.participants[summoner.name].champion.id
        played_champions_name[champion_id] += 1 

    most_played_champions = []

    for champion_id, count in played_champions_name.most_common(10):

        champion_name = champion_id_to_name_mapping[champion_id]
        champion_icon = champion_id_to_icon_mapping[champion_id]

        campion_played = {
            "campeon": {
                "nombre": str(champion_name),
                "icon": str(champion_icon)
            },
            "cantidad": str(count)
        }

        most_played_champions.append(campion_played)

    json_summoner['campeones_mas_jugados'] = most_played_champions
    json_summoner['numero_de_partidas'] = len(match_history)
    win_ratio = win_ratio/matchs_number
    win_ratio = win_ratio*100
    json_summoner['win_ratio'] = str(win_ratio)
    
    return json_summoner
