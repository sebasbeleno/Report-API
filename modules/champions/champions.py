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

def get_champions(champion_name):

    champion = Champion(region="LAN", name=champion_name)

    print(champion.name)
    print(champion.title)
    for spell in champion.spells:
        print(spell.name, spell.keywords)

    print(champion.info.difficulty)
    print(champion.passive.name)
    print({item.name: count for item, count in champion.recommended_itemsets[0].item_sets[0].items.items()})
    print(champion.free_to_play)
    
    print(champion.win_rates)


if __name__ == "__main__":
    get_champions("Lux")
