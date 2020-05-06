import cassiopeia as cass
import os
from cassiopeia import Champion, Champions

API_KEY = os.environ["API_KEY"]
cass.apply_settings({
    "logging": {
        "print_calls": False,
    }
})
cass.set_riot_api_key(API_KEY)

def main(region):
    champions = Champions(region=region)

    campeones = get_champions(region, champions)

    mejores_win = get_most_win_rates(campeones)
    
    print(mejores_win)


def get_champions(region, champions):
    
    campeones = []

    for champion in champions:
        
        campeon = {
            "nombre": champion.name,
            "imagen": champion.image.url,

        }

        campeones.append(campeon)

    return campeones

def get_most_win_rates(champions):
    
    win_rate  = []


    for champion in champions:

        campe = Champion(name=champion['nombre'], region="LAN")

        win_ratio = campe.win_rates.get('UTILITY')

        print(type(win_ratio))

        campeon = {
            "nombre": str(campe.name),
            "win_rate": win_ratio
        }

        win_rate.append(campeon)
    
    return win_rate

if __name__ == "__main__":
    main('LAN')
