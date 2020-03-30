from cassiopeia import Champion, Role


lux = Champion(name="Lux", region="LAN")

print({item.name: count for item, count in lux.recommended_itemsets[1].item_sets[1].items.items()})

""" print(lux.win_rates)
print(lux.ban_rates)
print(lux.play_rates) """
#print(lux.free_to_play)

"""
 WARNING

 ESTO ES UAN PRUEBA, Y NO ES CÓDIGO FINAL.
"""
