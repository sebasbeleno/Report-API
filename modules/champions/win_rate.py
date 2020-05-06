"""
    Este modulo retorna el winrate de todos los campeones
"""
from cassiopeia import  Champions

def myFunc(e):
  return e['win_rate']

def get_champions_win_rate(region):
    """
        Retorna el nombre, imagén y el winrate de cada campeón
    """

    champions = Champions(region=region)
    campeones = []

    for champion in champions:
        
        win_rates = champion.win_rates
        win_rates_views = win_rates.values()
        win_rates_iterator = iter(win_rates_views)
        primer_win = next(win_rates_iterator)
        primer_win = primer_win*100

        campeon = {
            "nombre": champion.name,
            "imagen": champion.image.url,
            "win_rate": round(primer_win, 2)

        }

        campeones.append(campeon)

    campeones.sort(key=myFunc)


    return campeones


