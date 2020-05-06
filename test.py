import datetime as date

if __name__ == "__main__":

    now = date.datetime.now()
    last_update = date.datetime.strptime("06/04/2020 00:00:00", "%d/%m/%Y %H:%M:%S") #24

    delta = now - date.timedelta(minutes=30)

    print(last_update)
    print(now)
    print(delta)

    if delta >= last_update:
        print("Han pasado 30 mins :d")

    #tct = DT.datetime.strptime("05/04/2021 01:4:40", "%d/%m/%Y %H:%M:%S") #24



    champion = Champion(region=region, name=champion_name)

    print(champion.name)
    print(champion.title)
    for spell in champion.spells:
        print(spell.name, spell.keywords)

    print(champion.info.difficulty)
    print(champion.passive.name)
    print(champion.enemy_tips)
    print(champion.stats.armor_per_level)
    print({item.name: count for item, count in champion.recommended_itemsets[0].item_sets[0].items.items()})
    print(champion.free_to_play)
    
    print(champion.win_rates)
