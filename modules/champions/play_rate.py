"""
    Este modulo retorna el playrate de todos los campeones
"""
from cassiopeia import  Champions

def myFunc(e):
  return e['play_rates']
    
def get_champions_play_rate(region):
    """
        Retorna el nombre, imagén y el play_rate de cada campeón
    """

    champions = Champions(region=region)
    campeones = []

    for champion in champions:
        
        play_rates = champion.play_rates
        play_rates_views = play_rates.values()
        play_rates_iterator = iter(play_rates_views)
        primer_play = next(play_rates_iterator)
        primer_play = primer_play*100

        campeon = {
            "nombre": champion.name,
            "imagen": champion.image.url,
            "play_rates": round(primer_play, 2)

        }

        campeones.append(campeon)

    campeones.sort(key=myFunc)

    return campeones
