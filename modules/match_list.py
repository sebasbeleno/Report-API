"""
    Este moculo se encarga de
    obtejer la list de paridas de un
    invocador.
"""
from itertools import islice
from cassiopeia import Summoner
from cassiopeia.data import Season

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

    list_of_match = []
    for match in islice(id_list_of_matchs, 3):

        summoner_participant = match.participants[summoner]
        match1 = {}

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
            "items": {
                "item1": {
                    "nombre": summoner_participant.stats.items[0].name,
                    "imagen": summoner_participant.stats.items[0].image.url,
                },
                "item2": {
                    "nombre": summoner_participant.stats.items[1].name,
                    "imagen": summoner_participant.stats.items[1].image.url,
                },
                "item3": {
                    "nombre": summoner_participant.stats.items[2].name,
                    "imagen": summoner_participant.stats.items[2].image.url,
                },

            },
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

        list_of_match.append(match1)

    json_summoner['matchs'] = list_of_match

    return json_summoner
