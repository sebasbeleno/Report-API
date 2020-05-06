"""
"""

from cassiopeia import Champions

def get_champions(region):
    """
        Retorna el nombre, imagén de cada campeón
    """

    champions = Champions(region=region)
    campeones = []

    for champion in champions:
    
        campeon = {
            "nombre": champion.name,
            "imagen": champion.image.url,
        }

        campeones.append(campeon)

    return campeones

