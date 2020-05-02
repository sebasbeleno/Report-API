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

        runes = summoner_participant.runes

        summoner_runes = []

        for rune in runes:
            summoner_runes.append(rune.name)
            summoner_runes.append(rune.image.url)



        match1 = {
            "campeon": {
                "nombre": str(summoner_participant.champion.name),
                "image":  str(summoner_participant.champion.image.url),
                "runas_principales": {
                    "1": {
                        "nombre": summoner_runes[0],
                        "imagen": summoner_runes[1]
                    },
                    "2": {
                        "nombre": summoner_runes[2],
                        "imagen": summoner_runes[3]
                    },
                    "3": {
                        "nombre": summoner_runes[4],
                        "imagen": summoner_runes[5]
                    },
                    "4": {
                        "nombre": summoner_runes[6],
                        "imagen": summoner_runes[7]
                    },
                    "5": {
                        "nombre": summoner_runes[8],
                        "imagen": summoner_runes[9]
                    },
                    "6": {
                        "nombre": summoner_runes[10],
                        "imagen": summoner_runes[11]
                    },
                },
                "runas_adicionales": {
                    "runa_adicionales_1": {
                        "nombre": str(summoner_participant.stat_runes[0].name),
                        "imagen": str(summoner_participant.stat_runes[0].image.url),
                    },
                    "runa_adicionales_2": {
                        "nombre": str(summoner_participant.stat_runes[1].name),
                        "imagen": str(summoner_participant.stat_runes[1].image.url),
                    },
                    "runa_adicionales_3": {
                        "nombre": str(summoner_participant.stat_runes[2].name),
                        "imagen": str(summoner_participant.stat_runes[2].image.url),
                    },
                },
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
            "equipo_rojo": {
                "participante1": {
                    "nombre_de_invocador": str(match.red_team.participants[0].summoner.name),
                    "nombre_de_campeon": str(match.red_team.participants[0].champion.name),
                    "icono_de_campeon": str(match.red_team.participants[0].champion.image.url),
                },
                "participante2": {
                    "nombre_de_invocador": str(match.red_team.participants[1].summoner.name),
                    "nombre_de_campeon": str(match.red_team.participants[1].champion.name),
                    "icono_de_campeon": str(match.red_team.participants[1].champion.image.url),
                },
                "participante3": {
                    "nombre_de_invocador": str(match.red_team.participants[2].summoner.name),
                    "nombre_de_campeon": str(match.red_team.participants[2].champion.name),
                    "icono_de_campeon": str(match.red_team.participants[2].champion.image.url),
                },
                "participante4": {
                    "nombre_de_invocador": str(match.red_team.participants[3].summoner.name),
                    "nombre_de_campeon": str(match.red_team.participants[3].champion.name),
                    "icono_de_campeon": str(match.red_team.participants[3].champion.image.url),
                },
                "participante5": {
                    "nombre_de_invocador": str(match.red_team.participants[4].summoner.name),
                    "nombre_de_campeon": str(match.red_team.participants[4].champion.name),
                    "icono_de_campeon": str(match.red_team.participants[4].champion.image.url),
                },
            },
            "equipo_azul": {
                "participante1": {
                    "nombre_de_invocador": str(match.blue_team.participants[0].summoner.name),
                    "nombre_de_campeon": str(match.blue_team.participants[0].champion.name),
                    "icono_de_campeon": str(match.blue_team.participants[0].champion.image.url),
                },
                "participante2": {
                    "nombre_de_invocador": str(match.blue_team.participants[1].summoner.name),
                    "nombre_de_campeon": str(match.blue_team.participants[1].champion.name),
                    "icono_de_campeon": str(match.blue_team.participants[1].champion.image.url),
                },
                "participante3": {
                    "nombre_de_invocador": str(match.blue_team.participants[2].summoner.name),
                    "nombre_de_campeon": str(match.blue_team.participants[2].champion.name),
                    "icono_de_campeon": str(match.blue_team.participants[2].champion.image.url),
                },
                "participante4": {
                    "nombre_de_invocador": str(match.blue_team.participants[3].summoner.name),
                    "nombre_de_campeon": str(match.blue_team.participants[3].champion.name),
                    "icono_de_campeon": str(match.blue_team.participants[3].champion.image.url),
                },
                "participante5": {
                    "nombre_de_invocador": str(match.blue_team.participants[4].summoner.name),
                    "nombre_de_campeon": str(match.blue_team.participants[4].champion.name),
                    "icono_de_campeon": str(match.blue_team.participants[4].champion.image.url),
                },
            },
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

    print(win_ratio)

    win_ratio = win_ratio/matchs_number

    print(win_ratio)

    win_ratio = win_ratio*100

    json_summoner['win_ratio'] = str(win_ratio)
    
    return json_summoner
